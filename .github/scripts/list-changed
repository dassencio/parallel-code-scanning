#!/usr/bin/env python3
#
# This script prints a JSON array containing all the supported CodeQL programming languages based on the file extension
#
# ["foo", "bar", "baz"]
#
from genericpath import isdir
import json
import os

javascript = [".js", ".jsx", ".mjs", ".es", ".es6", ".htm", ".html", ".xhtm", ".xhtml", ".vue", ".hbs", ".ejs", ".njk", ".json", ".yaml", ".yml", ".raml", ".xml"]
typescript = [".ts", ".tsx", ".mts", ".cts"]
c_and_cplus = [".cpp", ".c++", ".cxx", ".hpp", ".hh", ".h++", ".hxx", ".c," ".cc", ".h"]
csharp = [".sln", ".csproj", ".cs", ".cshtml", ".xaml"]
golang = [".go"]
python_lang = [".py"]
java = [".java"]
ruby = [".rb", ".erb", ".gemspec", "Gemfile"]

lines = list(open("./.github/scripts/diff.txt").readlines())
outlines = dict()
outlines["include"] = set()

def serialize_sets(obj):
    if isinstance(obj, set):
        l = list()
        for item in obj:
            if isinstance(item, tuple):
                l.append(dict((x, y) for x, y in item))
        return l

def find_in_list(list, string):
    for item in list:
        if item in string:
            return True
    return False

#only add items that are directories
for line in lines:
    path = line.split('/')[0]
    if find_in_list(javascript, line) and (os.path.isdir(path)):
        outlines["include"].add(tuple(dict({"target-dir": path, "languages": "javascript"}).items()))
    if find_in_list(typescript, line) and (os.path.isdir(path)):
        outlines["include"].add(tuple(dict({"target-dir": path, "languages": "javascript"}).items()))
    if find_in_list(c_and_cplus, line) and (os.path.isdir(path)):
        outlines["include"].add(tuple(dict({"target-dir": path, "languages": "cpp"}).items()))
    if find_in_list(csharp, line) and (os.path.isdir(path)):
        outlines["include"].add(tuple(dict({"target-dir": path, "languages": "csharp"}).items()))
    if find_in_list(golang, line) and (os.path.isdir(path)):
        outlines["include"].add(tuple(dict({"target-dir": path, "languages": "go"}).items()))
    if find_in_list(python_lang, line) and (os.path.isdir(path)):
        outlines["include"].add(tuple(dict({"target-dir": path, "languages": "python"}).items()))
    if find_in_list(java, line) and (os.path.isdir(path)):
        outlines["include"].add(tuple(dict({"target-dir": path, "languages": "java"}).items()))
    if find_in_list(ruby, line) and (os.path.isdir(path)):
        outlines["include"].add(tuple(dict({"target-dir": path, "languages": "ruby"}).items()))
    
print(json.dumps(outlines, default=serialize_sets))
