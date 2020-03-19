from os import listdir
from os.path import isfile

import xml.etree.cElementTree as ET
import uuid

archifiles = [f for f in listdir(".") if isfile(
    f) and f.endswith(".archimate") and "-Repo" not in f and "project" not in f]

root = ET.Element("archimate:model")
root.attrib["xmlns:archimate"] = "http://www.archimatetool.com/archimate"
root.attrib["name"] = "Kadaster"
root.attrib["id"] = str(uuid.uuid4())
root.attrib["version"] = "4.6.0"

folder = ET.SubElement(root, "folder")
folder.attrib["name"] = "Kadaster Repository"
folder.attrib["id"] = str(uuid.uuid4())

for af in archifiles:
    print("Parsing: ", af)
    subfolder = ET.SubElement(folder, "folder")
    subfolder.attrib["name"] = af
    subfolder.attrib["id"] = str(uuid.uuid4())
    #subfolder.attrib["type"] = "other"
    data = ET.parse(af)

    afroot = data.getroot()
    old_repo = afroot.find("./folder[@name='Kadaster Repository']")
    if old_repo:
        afroot.remove(old_repo)
        print("old repo removed")
    for c in afroot.find("."):
        subfolder.append(c)

no_save = False
count = 0
for e in root.findall(".//child[@archimateElement]"):
    aelem = e.get("archimateElement")
    count += 1
    if not root.findall(".//element[@id='" + aelem + "']"):
        print("Removed: ", aelem)
        no_save = True
print("Nr of elements: ", count)

tree = ET.ElementTree(root)
if not no_save:
    tree.write("Kadaster-Repository.archimate")
