import os


def deletenull(label_path):
    files = os.listdir(label_path)
    for file in files:
        if os.path.getsize(label_path + "/" + file) == 0:
            os.remove(label_path + "/" + file)


if __name__ == '__main__':
    deletenull("Westlife/labels_with_ids")
