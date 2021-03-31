import os
import xml.etree.ElementTree as ET


global count
count = 0


def xml_reader(filename):
    tree = ET.parse(filename)
    size = tree.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)
    objects = []
    for obj in tree.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text),
                              int(bbox.find('ymin').text),
                              int(bbox.find('xmax').text),
                              int(bbox.find('ymax').text)]
        objects.append(obj_struct)
    return width, height, objects


def voc2yolo(filename):
    global count
    width, height, objects = xml_reader(filename)
    lines = []
    for obj in objects:
        count += 1
        x, y, x2, y2 = obj['bbox']
        cx = (x2 + x) * 0.5 / width
        cy = (y2 + y) * 0.5 / height
        w = (x2 - x) * 1. / width
        h = (y2 - y) * 1. / height
        line = "%s %d %.6f %.6f %.6f %.6f\n" % (0, count, cx, cy, w, h)
        lines.append(line)
    txt_name = filename.replace(".xml", ".txt").replace("labels", "labels_with_ids")
    with open(txt_name, "w") as f:
        f.writelines(lines)


def listdir(dir):
    filenames = os.listdir(dir)
    filenames.sort()
    for filename in filenames:
        voc2yolo("labels/" + filename)


if __name__ == '__main__':
    listdir("labels")
