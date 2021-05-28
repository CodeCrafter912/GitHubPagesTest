""" Build index from directory listing
Inspired by: https://stackoverflow.com/questions/39048654/how-to-enable-directory-indexing-on-github-pages

make_index.py </path/to/directory>
"""

DEFAULT_TEMPLATE = {
    "outputFileName": "index.md",
    "icons": {
        "DIR": "📁",#":file_folder:",
        "FILE": "🗒", #":spiral_notepad:",
        "UP": "⤴", #":arrow_heading_up:"
    },
    "excludedFiles": ["index.md"],
    "template": r"""
# Index of ${path}
Files in this directory:
%for displayName, fileName, type in files:
- ${icons[type]} [${displayName}](${fileName})
% endfor
"""
}

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template

def createDirectoryListing(baseDirectory, template, subDirectory = ""):
    if baseDirectory.endswith("/"):
        baseDirectory = baseDirectory[:-1]

    thisDirectory = baseDirectory + "/" + subDirectory

    files = []

    if subDirectory:
        files.append((
            "Parent Directory",
            "../",
            "UP"
        ))

    for fileName in sorted(os.listdir(thisDirectory)):
        if fileName in template["excludedFiles"]:
            continue

        fileIsDir = os.path.isdir(thisDirectory + "/" + fileName)
        fileType = "DIR" if fileIsDir else "FILE"
        fileDisplayName = fileName + "/" if fileIsDir else fileName

        files.append((fileDisplayName, fileName, fileType))

        if fileIsDir:
            createDirectoryListing(baseDirectory, template, subDirectory + "/" + fileName)

    displayPath = "/" if not subDirectory else subDirectory

    fileContents = Template(template["template"]).render(files=files, path=displayPath, icons=template["icons"])
    
    with open(thisDirectory + "/" + template["outputFileName"], "w+") as file:
        file.write(fileContents)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()

    createDirectoryListing(args.directory, DEFAULT_TEMPLATE)

if __name__ == '__main__':
    main()