import os
import tkinter as tk
from tkinter import filedialog

# create the GUI window
root = tk.Tk()

# hide the GUI window
root.withdraw()

# ask the user to select a directory containing the files
directory = filedialog.askdirectory()

# loop through all files in the directory
for filename in os.listdir(directory):
    if ' ' in filename or '_' in filename:
        # remove spaces and underscores from the filename
        new_filename = filename.replace(' ', '').replace('_', '')

        # rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
