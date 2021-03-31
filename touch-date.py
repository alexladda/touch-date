#!/usr/bin/env python

"""
1. Walk through directory
2. find matching pairs of media file and xmp sidecar
3. extract data from xmp sidecar
4. touch media file with timestamp

Syntax:
> touch-date.py path-to-media

"""


import sys
import os
import xml.etree.ElementTree as ET
import subprocess


def get_timestamp(file):
    tree = ET.parse(file)
    root = tree.getroot()
    extracted_timestamp = root[0][0][12].text
    return extracted_timestamp


def prep_timestamp(extracted_timestamp):
    """
    input has this format: 2021-03-21T19:50:28+08:00
    returns this format: 20210321195028
    """
    # TODO: preserve timezone info?
    # TODO: automatically detect integers
    # TODO: integrate in or call from get_timestamp() function
    modified_timestamp = extracted_timestamp[:-6]
    unwanted = ['-', 'T', ':']
    for item in range(len(unwanted)):
        modified_timestamp = modified_timestamp.replace(unwanted[item], '')
    modified_timestamp = modified_timestamp[:-2] + '.' + modified_timestamp[-2:]
    return modified_timestamp


def touch_date(file, timestamp):
    shellcommand = ["touch", "-t", timestamp, file]
    subprocess.run(shellcommand)


path = sys.argv[1]

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if os.path.splitext(filename)[1] == ".xmp":
            fullpath = os.path.join(os.getcwd(), dirpath, filename)
            timestamp = get_timestamp(fullpath)
            timestamp = prep_timestamp(timestamp)
            touch_date(fullpath, timestamp)
