#!/usr/bin/env python3

#
# This script prints a JSON array containing all non-hidden subdirectories of
# the current working directory. As an example, if the current working
# directory contains the subdirectories "foo", "bar" and "baz", the output
# will be (the order of the directories is not necessarily alphabetical):
#
# ["foo", "bar", "baz"]
#
from genericpath import isdir
import json
import os

lines = list(open('./.github/scripts/diff.txt').readlines())
outlines = set()

#only add items that are directories
for line in lines:
    path = line.split('/')[0]
    if (os.path.isdir(path)):
        outlines.add(path)

print(json.dumps(list(outlines)))
