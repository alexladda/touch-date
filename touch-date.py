#!/usr/bin/env python

"""
1. Walk through directory
2. find matching pairs of media file and xmp sidecar
3. extract data from xmp sidecar
4. touch media file with timestamp

Usage:
> python touch-date.py path-to-media
or:
> ./ touch-date.py path-to-media

This might not work on your machine, could mess up things if used in the wrong way.
This has not been tested beyond a few files on my drive.
Mac OS 11.2.3 (Big Sur)
Photos 6.0
Python 3.9.2
"""


import sys                          # get command line argument
import os                           # access files
import xml.etree.ElementTree as ET  # XML Parser
import subprocess                   # run Bash command


def get_timestamp(file):
    # parse XML file, Element Tree object
    tree = ET.parse(file)
    # get root Element (?)
    root = tree.getroot()
    # iterate through element tree
    for elem in root.iter():
        # find Date Tag
        if elem.tag.endswith("DateCreated"):
            # return text string of said Element
            return elem.text


def prep_timestamp(xmp_timestamp):
    """
    input (xmp_timestamp) has this format: 2021-03-21T19:50:28+08:00
    returns (timestamp) this format: 202103211950.28
    """
    # TODO: preserve timezone info?
    # TODO: automatically detect integers
    # TODO: integrate in or call from get_timestamp() function

    # cut off time zone
    timestamp = xmp_timestamp[:-6]
    # cut off unwanted characters
    unwanted = ['-', 'T', ':']
    for item in range(len(unwanted)):
        timestamp = timestamp.replace(unwanted[item], '')
    # add a '.' at the appropriate position
    timestamp = timestamp[:-2] + '.' + timestamp[-2:]
    return timestamp


def touch_date(timestamp, cwd, dirpath, filename):
    """
    This function takes a timestamp and the path to an xmp sidecar file.
    It will then touch all corresponding files and said xmp file with
    the specified timestamp.
    """
    # xmppath is the absolute file path of the xmp sidecar file:
    # /Users/<user>/export/IMG_1234.xmp

    # We want to run something like the following command to touch
    # all corresponding files:
    # Bash $> touch -t <timestamp> /Users/<user>/export/IMG_1234.*

    # assembling the argument for the touch command
    wildcardname = filename[:-4] + '.*'
    wildcardpath = os.path.join(cwd, dirpath, wildcardname)
    wildcardpath = wildcardpath.replace(" ", "\\ ")
    print("wildcardpath:", wildcardpath)
    shellcommand = 'touch -t {0} {1}'.format(timestamp, wildcardpath)

    # giving some feedback
    print(shellcommand)
    # running the shell command
    subprocess.run(shellcommand, shell=True)


# getting directory from command line argument
search_dir = sys.argv[1]

# walking search directory
for dirpath, dirnames, filenames in os.walk(search_dir):
    for filename in filenames:
        # check for xmp sidecar files
        if os.path.splitext(filename)[1] == ".xmp":
            # get the full path of .xmp files
            xmppath = os.path.join(os.getcwd(), dirpath, filename)
            # get and prep timestamp from xmp file
            timestamp = get_timestamp(xmppath)
            timestamp = prep_timestamp(timestamp)
            touch_date(timestamp, os.getcwd(), dirpath, filename)
