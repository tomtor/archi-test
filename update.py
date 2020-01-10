import xml.etree.cElementTree as ET
import urllib.request

import uuid

namespaces = {'archimate': "http://www.archimatetool.com/archimate",
              'ns0': "http://www.archimatetool.com/archimate",
              }

response = urllib.request.urlopen(
    'https://raw.githubusercontent.com/tomtor/archi-test/master/Kadaster-Repository.archimate')
new_repo = response.read()

#ET.register_namespace("archimate", )

new_repo = ET.fromstring(new_repo)

data = ET.parse("project.archimate")

# ============== update code start ====================

root = data.getroot()
root.attrib["xmlns:archimate"] = "http://www.archimatetool.com/archimate"

old_repo = root.find(".//folder[@name='Kadaster Repository']")
if old_repo:
    root.remove(old_repo)
else:
    print("no old repo")
root.insert(0, new_repo.find(".//folder[@name='Kadaster Repository']"))

for e in root.findall(".//child[@archimateElement]"):
    aelem = e.get("archimateElement")
    if not root.findall(".//element[@id='" + aelem + "']"):
        print("Removed: ", aelem)
        old = root.find(".//folder[@name='OLD-Repo']")
        if not old:
            print("Create OLD-Repo folder")
            old = ET.SubElement(root, "folder")
            old.attrib["name"] = "OLD-Repo"
            old.attrib["id"] = str(uuid.uuid4())
            old.attrib["type"] = "other"
        aelem = old_repo.find(".//element[@id='" + aelem + "']")
        old.append(aelem)

tree = ET.ElementTree(root)

# ========== end update code ===========

tree.write("project-new.archimate")
