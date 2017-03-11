#!/bin/python3
"""
Python script for sorting files by exif data.
Script goes through all files in directory and for every value of tag 
it creates new directory and move the file there.
"""

import argparse
import cus_logging 
import exiftool
import os
import logging

g_recursive = False
g_tags = []
g_path = os.getcwd()

def parse_arguments():
    """
    Parse arguments using argparse module
    """
    global g_recursive, g_tags, g_path

    parser = argparse.ArgumentParser(description='Python script for sorting files by exif data')
    parser.add_argument('-r', '--recursive', help='recursive mode', action='store_true')
    parser.add_argument('-p', '--path', help='path to directory with files for sorting')
    parser.add_argument('-t', '--tags', help='tag/s to use for sorting, the tags are\
            the same as returned by exiftool command', nargs='+', required=True)
    args = parser.parse_args()

    if args.recursive:
        g_recursive = True
    if args.tags:
        g_tags = args.tags
    if args.path:
        g_path = args.path

def read_exifdata(path):
    """
    Read exif metadata for files in directory

    Returns exif tags dictionary
    """
    files_tags = {}

    for f in os.listdir(path):
        file_path = os.path.join(path,f)

        # ignore directories
        if os.path.isfile(file_path):
            with exiftool.ExifTool() as et:
                tags_temp = et.get_metadata(file_path)
                tags = {}
                # Erase the group info from tags and leave only tag names
                for k,v in tags_temp.items():
                    newkey = k.split(':')[-1].lower()
                    tags[newkey] = v
                files_tags[f] = tags

    return files_tags

def sort_to_directories(files_tags, path, tags):
    """
    Move the files to directories by the value of the specified tags
    """

    directories = {}

    for file_name, file_tags in files_tags.items():
        #logging.debug("Current file: " + file_name)
        values = []
        for tag in tags:
            # find the tag in file tags
            try:
                value = file_tags[tag.replace(" ","").lower()]
                if value:
                    values.append(value)
            except:
                continue
        # Check if tags were found if file
        if values:
            directory_name = '_'.join(values)
            # if value was found previously, directory exists
            if not directory_name in directories:
                directory = os.path.join(path, directory_name)
                if not os.path.exists(directory):
                    os.mkdir(directory)
                directories[directory_name] = directory 
                #logging.debug(directories) 
            
            # always move the file to the directory
            os.rename(os.path.join(path, file_name), os.path.join(directories[directory_name],file_name))

def process_directories(path, tags, recursive):
    """
    Move through directories.
    This function is going only through one directory if recursive mode is not enabled.
    """
        
    #logging.debug("Current directory: " + path)
    if not recursive:
        files_tags = read_exifdata(path)
        sort_to_directories(files_tags, path, tags)
    else:
        directories = next(os.walk(path))[1]
        #logging.debug(directories)
        files_tags = read_exifdata(path)
        sort_to_directories(files_tags, path, tags)
        for directory in directories:
            process_directories(os.path.join(path, directory), tags, recursive)


if __name__ == "__main__":
    parse_arguments()
    process_directories(g_path, g_tags, g_recursive)
