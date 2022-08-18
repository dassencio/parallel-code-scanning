#!/usr/bin/env python3
#
# This script prints a JSON array containing all the supported CodeQL programming languages based on the file extension
#
# ["foo", "bar", "baz"]
#
import json

javascript = [".js", ".jsx", ".mjs", ".es", ".es6", ".htm", ".html", ".xhtm", ".xhtml", ".vue", ".hbs", ".ejs", ".njk", ".json", ".yaml", ".yml", ".raml", ".xml"]
typescript = [".ts", ".tsx", ".mts", ".cts"]
c_and_cplus = [".cpp", ".c++", ".cxx", ".hpp", ".hh", ".h++", ".hxx", ".c," ".cc", ".h"]
csharp = [".sln", ".csproj", ".cs", ".cshtml", ".xaml"]
golang = [".go"]
python_lang = [".py"]
java = [".java"]
ruby = [".rb", ".erb", ".gemspec", "Gemfile"]


lines = list(open("./.github/scripts/diff.txt").readlines())
outlines = set()

def find_in_list(list, string):
    for item in list:
        if item in string:
            return True
    return False

#only add items that are directories
for line in lines:
    if find_in_list(javascript, line):
        outlines.add("javascript")
    if find_in_list(typescript, line):
        outlines.add("javascript")
    if find_in_list(javascript, line):
        outlines.add("javascript")



print(json.dumps(list(outlines)))
