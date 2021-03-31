import os


with open("eccv2016/eccv2016.train", 'a') as f:
    files = os.listdir("eccv2016")
    for file in files:
        dir = "/home/hengyuli/FaceMFT/dataset/eccv2016/" + file
        if os.path.isdir(dir):
            lables_with_ids = os.listdir(dir + "/" + "labels_with_ids")
            lables_with_ids.sort()
            for label in lables_with_ids:
                f.write(dir + "/" + "images/" + label[:-4] + ".jpg" + "\n")
