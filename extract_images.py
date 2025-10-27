import os
import sys
import shutil

"""
Takes all the images out of the specified folders and places them in
one place (images)

For example, "python3 extract_images.py 18-20 22" takes all the pngs
from sections 18, 19, 20, and 22
"""

destination_directory = "images"

# Quit if no arguments
if len(sys.argv) <= 1:
    print("Must pass in arguments")
    exit
args = sys.argv[1:]

numbers = []
for arg in args:
    # If there is a dash in the argument, add all the numbers to the list
    # So 18-20 adds 18, 19, and 20 to the list
    dash_index = arg.find("-")
    if dash_index > 0:
        start = int(arg[0:dash_index])
        end = int(arg[dash_index+1:])
        numbers += [str(i) for i in range(start, end+1)]
    # Otherwise just add the number
    else:
        numbers.append(arg)

# Get a list of folders to walk through
base_folders = []
for number in numbers:
    base_folders += [i for i in os.listdir() if os.path.isdir(i) and i.startswith(number)]

# Make a new directory (remove it if it already exists)
if os.path.exists(destination_directory) and os.path.isdir(destination_directory):
    shutil.rmtree(destination_directory)
os.mkdir(destination_directory)


for folder in base_folders:
    # Walk through every folder and copy all PNGs into the destination directory
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith("png"):
                source = os.path.join(root, file)
                dest = os.path.join(destination_directory, file)
                shutil.copy(source, dest)
    print(f"Copied images from {folder} into {destination_directory}")