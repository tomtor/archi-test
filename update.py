import xml.etree.cElementTree as ET
import urllib.request
import uuid


def update_repo(filename):
    response = urllib.request.urlopen(
        'https://raw.githubusercontent.com/tomtor/archi-test/master/Kadaster-Repository.archimate')
    new_repo = response.read()
    new_repo = ET.fromstring(new_repo)

    data = ET.parse(filename)
    root = data.getroot()
    root.attrib["xmlns:archimate"] = "http://www.archimatetool.com/archimate"

    old_repo = root.find(".//folder[@name='Kadaster Repository']")
    if old_repo:
        print("update old repo:", filename)
        root.remove(old_repo)
    else:
        print("no old repo", filename)

    # Find duplicated items in repo
    for f in new_repo.findall(".//folder"):
      # print(f)
      for e in f.findall("./"):
        if "id" in e.attrib:
            # print(e)
            for o in root.findall(".//element[@id='" + e.attrib["id"] + "']"):
                print("DEL: ", e.attrib["id"], o.attrib["id"])
                f.remove(e)
        else:
            pass
            # print("No ID:", e)

    root.insert(0, new_repo.find(".//folder[@name='Kadaster Repository']"))

    for e in root.findall(".//child[@archimateElement]"):
        aelem = e.get("archimateElement")
        if not root.findall(".//element[@id='" + aelem + "']"):
            print("Removed: ", aelem)
            old = root.findall(".//folder[@name='OLD-Repo']")
            if not old:
                print("Create OLD-Repo folder")
                old = ET.SubElement(root, "folder")
                old.attrib["name"] = "OLD-Repo"
                old.attrib["id"] = str(uuid.uuid4())
                old.attrib["type"] = "other"
            else:
                old = old[0]
            aelem = old_repo.find(".//element[@id='" + aelem + "']")
            old.append(aelem)
    return ET.ElementTree(root)


def main():
    filename = "project.archimate"
    tree = update_repo(filename)
    tree.write("project-new.archimate")


if __name__ == '__main__':
    main()
