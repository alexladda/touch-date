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

path = sys.argv[1]
