""" Build index from directory listing
Original source: https://stackoverflow.com/questions/39048654/how-to-enable-directory-indexing-on-github-pages

make_index.py </path/to/directory> [--header <header text>]
"""

INDEX_TEMPLATE = r"""
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of ${header}</title>
 </head>
 <body>
<h1>Index of ${header}</h1>
  <table>
    <tr><th colspan="5"><hr></th></tr>
        % for name, type, icon in files:
            <tr><td valign="top"><img src="${icon}" alt="[${type}]"></td><td><a href="${name}">${name}</a></tr>
        % endfor
    <tr><th colspan="5"><hr></th></tr>
</table>
<address>Static directory listing :)</address>
</body></html>
"""

FOLDER_ICON = "R0lGODlhFAAWAMIAAP/////Mmcz//5lmMzMzMwAAAAAAAAAAACH+TlRoaXMgYXJ0IGlzIGluIHRoZSBwdWJsaWMgZG9tYWluLiBLZXZpbiBIdWdoZXMsIGtldmluaEBlaXQuY29tLCBTZXB0ZW1iZXIgMTk5NQAh+QQBAAACACwAAAAAFAAWAAADVCi63P4wyklZufjOErrvRcR9ZKYpxUB6aokGQyzHKxyO9RoTV54PPJyPBewNSUXhcWc8soJOIjTaSVJhVphWxd3CeILUbDwmgMPmtHrNIyxM8Iw7AQA7"
FILE_ICON = "R0lGODlhFAAWAMIAAP///8z//5mZmTMzMwAAAAAAAAAAAAAAACH+TlRoaXMgYXJ0IGlzIGluIHRoZSBwdWJsaWMgZG9tYWluLiBLZXZpbiBIdWdoZXMsIGtldmluaEBlaXQuY29tLCBTZXB0ZW1iZXIgMTk5NQAh+QQBAAABACwAAAAAFAAWAAADaDi6vPEwDECrnSO+aTvPEQcIAmGaIrhR5XmKgMq1LkoMN7ECrjDWp52r0iPpJJ0KjUAq7SxLE+sI+9V8vycFiM0iLb2O80s8JcfVJJTaGYrZYPNby5Ov6WolPD+XDJqAgSQ4EUCGQQEJADs="
BACK_ICON = "R0lGODlhFAAWAMIAAP///8z//5mZmWZmZjMzMwAAAAAAAAAAACH+TlRoaXMgYXJ0IGlzIGluIHRoZSBwdWJsaWMgZG9tYWluLiBLZXZpbiBIdWdoZXMsIGtldmluaEBlaXQuY29tLCBTZXB0ZW1iZXIgMTk5NQAh+QQBAAABACwAAAAAFAAWAAADSxi63P4jEPJqEDNTu6LO3PVpnDdOFnaCkHQGBTcqRRxuWG0v+5LrNUZQ8QPqeMakkaZsFihOpyDajMCoOoJAGNVWkt7QVfzokc+LBAA7"

EXCLUDED = ['index.html']

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template

def createDirectoryListing(directory, hasBackOption=False):
    files = []

    if hasBackOption:
        files.append((
            "../",
            "UP",
            "data:image/gif;base64, " + BACK_ICON
        ))

    for fileName in sorted(os.listdir(directory)):
        if fileName in EXCLUDED:
            continue

        fileIsDir = os.path.isdir(directory + "/" + fileName)
        fileType = "DIR" if fileIsDir else "FILE"
        fileIcon = "data:image/gif;base64, " + (FOLDER_ICON if fileIsDir else FILE_ICON)
        fileDisplayName =   fileName + "/" if fileIsDir else fileName

        files.append((fileDisplayName, fileType, fileIcon))

        if fileIsDir:
            createDirectoryListing(directory + "/" + fileName, True)

    fileContents = Template(INDEX_TEMPLATE).render(files=files, header=directory)
    with open(directory + "/index.html", "w+") as file:
        file.write(fileContents)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()

    createDirectoryListing(args.directory)

if __name__ == '__main__':
    main()