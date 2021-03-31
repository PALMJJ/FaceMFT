import os


with open("cuhksysu/cuhksysu.train", 'a') as f:
    images = os.listdir("/home/hengyuli/FaceMFT/dataset/cuhksysu/images")
    images.sort()
    for image in images:
        f.write("/home/hengyuli/FaceMFT/dataset/cuhksysu/images/" + image + "\n")
