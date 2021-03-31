# A Script to correct the date timestamps when exporting from OS X Photos App

When exporting from Photos App in OS X the original timestamp is not preserved. This script restores the original timestamp for Media exported from the Photos Library.

1. in Photos: "File > Export unmodified Originals ..."
2. select checkbox for XML files
3. run Script: python3 touch-date.py path-to-files
  - Walk through directory
  - find matching pairs of media file and xmp sidecar
  - extract data from xmp sidecar
  - touch media file with timestamp
4. relax.
