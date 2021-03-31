import os


with open("widerface/widerface.train", 'a') as f:
    images = os.listdir("/home/hengyuli/FaceMFT/dataset/widerface/images")
    images.sort()
    for image in images:
        f.write("/home/hengyuli/FaceMFT/dataset/widerface/images/" + image + "\n")
