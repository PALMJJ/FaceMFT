from PIL import Image
from xml.dom.minidom import parse


def read_xml(filename, image_path, out):
    img = Image.open(image_path)
    image_width = img.size[0]
    image_height = img.size[1]
    domTree = parse(filename)
    rootNode = domTree.documentElement
    start_frame = int(rootNode.getAttribute("start_frame"))
    end_frame = int(rootNode.getAttribute("end_frame"))
    # for i in range(start_frame, end_frame + 1):
    #     open(out + str("%05d" % i) + ".txt", 'w')
    trajectorys = rootNode.getElementsByTagName("Trajectory")
    for trajectory in trajectorys:
        tid = int(trajectory.getAttribute("obj_id")) + 45
        frames = trajectory.getElementsByTagName("Frame")
        for frame in frames:
            frame_no = int(frame.getAttribute("frame_no"))
            x = int(frame.getAttribute("x"))
            y = int(frame.getAttribute("y"))
            width = int(frame.getAttribute("width"))
            height = int(frame.getAttribute("height"))
            cx = (x + width / 2) / image_width
            cy = (y + height / 2) / image_height
            w = width / image_width
            h = height / image_height
            with open(out + "%05d" % frame_no + ".txt", 'a') as f:
                f.write("%d %d %.6f %.6f %.6f %.6f\n" % (0, tid, cx, cy, w, h))    


if __name__ == '__main__':
    read_xml("/home/hengyuli/FaceMFT/dataset/eccv2016/Westlife/Westlife_gt.xml", "/home/hengyuli/FaceMFT/dataset/eccv2016/Westlife/images/00001.jpg", "/home/hengyuli/FaceMFT/dataset/eccv2016/Westlife/labels_with_ids/")
