# Folder Compare Move (FCM) README
=====================================

## Introduction
---------------

The Folder Compare Move (FCM) script is a Python utility designed to compare two folders and move files that are present in the source folder but missing in the destination folder. The script is useful for synchronizing files between two folders, ensuring that all files from the source folder are copied to the destination folder.

## Features
------------

*   Compares files in the source and destination folders, including subdirectories
*   Moves files that are present in the source folder but missing in the destination folder
*   Creates a "Missed files" folder in the destination folder to store the moved files
*   Preserves the relative path structure of the source folder in the "Missed files" folder

## Requirements
---------------

*   Python 3.x
*   `os` and `shutil` modules (included in the Python standard library)

## Usage
-----

1.  Install Python 3.x on your system if you haven't already.
2.  Download the `fcm.py` script and save it to a location of your choice.
3.  Open a terminal or command prompt and navigate to the directory where you saved the script.
4.  Run the script using the command `python fcm.py`.
5.  Modify the `src` and `dest` variables in the script to specify the source and destination folders you want to compare.

### Example Usage

```python
src = r"src"
dest = r"dest"
move_missing_files(src, dest)
```

## Parameters
------------

*   `src`: The path to the source folder.
*   `dest`: The path to the destination folder.

## Output
--------

The script will print a message for each file that is moved, indicating the file name, source directory, and destination directory.

## Notes
-----

*   The script assumes that the source and destination folders are on the same file system.
*   The script does not handle file conflicts or overwrites. If a file with the same name already exists in the destination folder, it will be overwritten.
*   The script does not delete any files. It only moves files that are present in the source folder but missing in the destination folder.