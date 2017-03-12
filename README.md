# pyexifsorter
Python 3 exif sorter

## Description
This script will sort files using the exif metadata.
The user can use any tag or more tags to sort the files, the files are moved to directories named by the value of tag or tags.
The name of the tags are same as printed by exiftool command.

## Usage
usage: pyexifsorter [-h] [-r] [-p PATH] -t TAGS [TAGS ...]

Python script for sorting files by exif data

optional arguments:
- h, --help            show this help message and exit
- r, --recursive       recursive mode
- p PATH, --path PATH  path to directory with files for sorting
- t TAGS [TAGS ...], --tags TAGS [TAGS ...]
 
 tag/s to use for sorting, the tags are the same as
 returned by exiftool command

## Example of usage
For example the folder **test** has several files in it.
- 1.jpg Image Size:1024x768
- 2.png Image Size:1024x768
- 3.avi Image Size:320x240

We will run **pyexifsorte**
```
./pyexifsorter -p test -t "Image Size"
```

The content of folder **test** will be:
- 1024x768 - directory containing files 1.jpg and 2.png
- 320x240 - directory containing 3.avi
