from os import listdir
from os.path import isfile, join

import xml.etree.cElementTree as ET
import uuid

archifiles = [f for f in listdir(".") if isfile(f) and f.endswith(".archimate") and not "-Repo" in f]

root = ET.Element("archimate:model")
#root.attrib["xmlns:xsi"] = "http://www.w3.org/2001/XMLSchema-instance"
root.attrib["xmlns:archimate"] = "http://www.archimatetool.com/archimate"
root.attrib["name"] = "Kadaster"
root.attrib["id"] = str(uuid.uuid4())
root.attrib["version"] = "4.6.0"

folder = ET.SubElement(root, "folder")
folder.attrib["name"] = "Kadaster Repository"
folder.attrib["id"] = str(uuid.uuid4())
folder.attrib["type"] = "other"

for af in archifiles:
    print("Parsing: ", af)
    with open(af, 'r') as file:
        subfolder = ET.SubElement(folder, "folder")
        subfolder.attrib["name"] = af
        subfolder.attrib["id"] = str(uuid.uuid4())
        subfolder.attrib["type"] = "other"
        data = ET.parse(af)
        for c in data.getroot():
            subfolder.append(c)

tree = ET.ElementTree(root)
tree.write("Kadaster-Repository.archimate")