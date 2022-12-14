#!/usr/bin/env python3

#
# This script prints a JSON array containing all non-hidden subdirectories of
# the current working directory. As an example, if the current working
# directory contains the subdirectories "foo", "bar" and "baz", the output
# will be (the order of the directories is not necessarily alphabetical):
#
# ["foo", "bar", "baz"]
#

import glob
import json

print(json.dumps(glob.glob("*/")).replace("/", ""))
