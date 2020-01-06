#! python3

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r'''^(.*?)     #all text before the date
    ((0|1)?\d)-

    ''', re.VERBOSE)
