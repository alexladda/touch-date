# A Script to correct the date timestamps when exporting from OS X Photos App

## Which problem does this Script solve?

When exporting from Photos App in OS X the original timestamp is not preserved. Instead a new timestamp (as in "now") is created for the new file.

I assume no one has ever been bothered by this. I can understand that one could argue the timestamp of the file should relate to the creation date of the file and not of the Photo.

But this has always bothered me. So that's why I wrote this Script.

## What does this Script do exactly?

This script restores the original timestamp to the media files after they are exported from the Photos Library:

- search the specified folder (and all subfolders) for xmp sidecar files
- extract their timestamps
- set the respective file's 'Date Created' and 'Date modified' to the value found in the xmp sidecar file

## Usage

### 1. Export
- in Photos: "File > Export unmodified Originals ..."
- select checkbox for XML files
- export to folder

### 2. run Script

`python3 touch-date.py <path to files>`

or

`./touch-date.py <path to files>`


- scan the specified folder (and all subfolders) for xmp sidecar files
- extract the timestamps
- if theres corresponding media files (photos or videos) it sets their 'Date Created' and 'Date modified' to the value found in the xmp sidecar file


***Word of caution:***

This might not work on your machine, could mess up things if used in the wrong way.
This has not been tested beyond a few files on my drive.

- Mac OS 11.2.3 (Big Sur)
- Photos 6.0
- Python 3.9.2
