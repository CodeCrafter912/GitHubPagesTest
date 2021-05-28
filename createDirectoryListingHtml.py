""" Build index from directory listing
Original source: https://stackoverflow.com/questions/39048654/how-to-enable-directory-indexing-on-github-pages

make_index.py </path/to/directory>
"""

BASE64_ICONS = {
    "DIR": "R0lGODlhFAAWAMIAAP/////Mmcz//5lmMzMzMwAAAAAAAAAAACH+TlRoaXMgYXJ0IGlzIGluIHRoZSBwdWJsaWMgZG9tYWluLiBLZXZpbiBIdWdoZXMsIGtldmluaEBlaXQuY29tLCBTZXB0ZW1iZXIgMTk5NQAh+QQBAAACACwAAAAAFAAWAAADVCi63P4wyklZufjOErrvRcR9ZKYpxUB6aokGQyzHKxyO9RoTV54PPJyPBewNSUXhcWc8soJOIjTaSVJhVphWxd3CeILUbDwmgMPmtHrNIyxM8Iw7AQA7",
    "FILE": "R0lGODlhFAAWAMIAAP///8z//5mZmTMzMwAAAAAAAAAAAAAAACH+TlRoaXMgYXJ0IGlzIGluIHRoZSBwdWJsaWMgZG9tYWluLiBLZXZpbiBIdWdoZXMsIGtldmluaEBlaXQuY29tLCBTZXB0ZW1iZXIgMTk5NQAh+QQBAAABACwAAAAAFAAWAAADaDi6vPEwDECrnSO+aTvPEQcIAmGaIrhR5XmKgMq1LkoMN7ECrjDWp52r0iPpJJ0KjUAq7SxLE+sI+9V8vycFiM0iLb2O80s8JcfVJJTaGYrZYPNby5Ov6WolPD+XDJqAgSQ4EUCGQQEJADs=",
    "UP": "R0lGODlhFAAWAMIAAP///8z//5mZmWZmZjMzMwAAAAAAAAAAACH+TlRoaXMgYXJ0IGlzIGluIHRoZSBwdWJsaWMgZG9tYWluLiBLZXZpbiBIdWdoZXMsIGtldmluaEBlaXQuY29tLCBTZXB0ZW1iZXIgMTk5NQAh+QQBAAABACwAAAAAFAAWAAADSxi63P4jEPJqEDNTu6LO3PVpnDdOFnaCkHQGBTcqRRxuWG0v+5LrNUZQ8QPqeMakkaZsFihOpyDajMCoOoJAGNVWkt7QVfzokc+LBAA7"
}

EMOJI_ICONS = {
    "DIR": "📁",#":file_folder:",
    "FILE": "🗒", #":spiral_notepad:",
    "UP": "⤴", #":arrow_heading_up:"
}

HTML_TEMPLATE = {
    "outputFileName": "index.html",
    "icons": BASE64_ICONS,
    "template": r"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of ${header}</title>
 </head>
 <body>
<h1>Index of ${header}</h1>
  <table>
    <tr><th colspan="5"><hr></th></tr>
        % for name, type in files:
            <tr><td valign="top"><img src="data:image/gif;base64, ${icons[type]}" alt="[${type}]"></td><td><a href="${name}">${name}</a></tr>
        % endfor
    <tr><th colspan="5"><hr></th></tr>
</table>
<address>Static directory listing :)</address>
</body></html>
"""
}

MD_TEMPLATE = {
    "outputFileName": "index.md",
    "icons": EMOJI_ICONS,
    "template": r"""
# Index of ${header}
Files in this directory:
%for name, type in files:
- ${icons[type]} [${name}](${name})
% endfor
"""
}

EXCLUDED = ['index.html', 'index.md']

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template

def createDirectoryListing(directory, template, hasBackOption=False):
    files = []

    if hasBackOption:
        files.append((
            "../",
            "UP"
        ))

    for fileName in sorted(os.listdir(directory)):
        if fileName in EXCLUDED:
            continue

        fileIsDir = os.path.isdir(directory + "/" + fileName)
        fileType = "DIR" if fileIsDir else "FILE"
        fileDisplayName =   fileName + "/" if fileIsDir else fileName

        files.append((fileDisplayName, fileType))

        if fileIsDir:
            createDirectoryListing(directory + "/" + fileName, template, True)

    fileContents = Template(template["template"]).render(files=files, header=directory, icons=template["icons"])
    
    with open(directory + "/" + template["outputFileName"], "w+") as file:
        file.write(fileContents)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()

    createDirectoryListing(args.directory, MD_TEMPLATE)

if __name__ == '__main__':
    main()