from os import listdir
from os.path import isfile
import sys

import xml.etree.cElementTree as ET
import uuid

root = ET.Element("archimate:model")
root.attrib["xmlns:archimate"] = "http://www.archimatetool.com/archimate"
root.attrib["name"] = "Create Oracle"
root.attrib["id"] = str(uuid.uuid4())
root.attrib["version"] = "4.6.0"

folder = ET.SubElement(root, "folder")
folder.attrib["name"] = "Application"
folder.attrib["type"] = "application"
folder.attrib["id"] = str(uuid.uuid4())

app = ET.SubElement(folder, "element")
app.attrib["name"] = "test"
app.attrib["id"] = str(uuid.uuid4())
app.attrib["xsi:type"] = "archimate:ApplicationFunction"

tree = ET.ElementTree(root)

tree.write("create.archimate")

