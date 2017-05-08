# pyexifsorter
Python 3 exif sorter

## Description
This script will sort files using the exif metadata.
The user can use any tag or more tags to sort the files, the files are moved to directories named by the value of tag or tags.
The name of the tags are same as printed by exiftool command.

## Requirements
This script is based on PyExifTool library and needs [ExifTool](http://www.sno.phy.queensu.ca/~phil/exiftool/) command-line utility to be installed.

## Usage
usage: pyexifsorter [-h] [-r] [-p PATH] -t TAGS [TAGS ...]

Python script for sorting files by exif data

optional arguments:
- h, --help            show this help message and exit
- r, --recursive       recursive mode
- p PATH, --path PATH  path to directory with files for sorting (if not specified, the current directory is used)
- t TAGS [TAGS ...], --tags TAGS [TAGS ...] tag/s to use for sorting, the tags are the same as returned by exiftool command (for example Image Size or File Type)

## Example of usage
For example the folder **test** has several files in it.
- 1.jpg Image Size:1024x768
- 2.png Image Size:1024x768
- 3.avi Image Size:320x240

We will run **pyexifsorter**:
```
./pyexifsorter -p test -t "Image Size"
```

The content of folder **test** will be:
- 1024x768 - directory containing files 1.jpg and 2.png
- 320x240 - directory containing 3.avi
