from os import listdir
from os.path import isfile
import sys

import xml.etree.cElementTree as ET
import uuid

source = "src/u_oracle_schema.csv"

root = ET.Element("archimate:model")
root.attrib["xmlns:archimate"] = "http://www.archimatetool.com/archimate"
root.attrib["name"] = "Convert " + source
root.attrib["id"] = str(uuid.uuid4())
root.attrib["version"] = "4.6.0"

folder = ET.SubElement(root, "folder")
folder.attrib["name"] = "Application"
folder.attrib["type"] = "application"
folder.attrib["id"] = str(uuid.uuid4())

with open(source) as f:
    for l in f.readlines():
        p = l.split(',')
        #print(p[1])
        if p[1] != '"Prod"':
            continue
        name = p[0][1:-1]
        print(name)

        app = ET.SubElement(folder, "element")
        app.attrib["name"] = name
        app.attrib["id"] = str(uuid.uuid4())
        app.attrib["xsi:type"] = "archimate:ApplicationFunction"

tree = ET.ElementTree(root)

tree.write(source.split('/')[-1] + ".archimate")

