import sys
if sys.version_info.major != 3:
    print("wrong python version:", sys.version_info.major)
    quit()

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from shutil import copyfile
import os
import random

labels = [ "partial_faces", "is_female", "baby_age", "child_age", "teenager_age", "youth_age", "middle_age", "senior_age", "white_race", "black_race", "asian_race", "oval_face", "round_face", "heart_face", "smiling", "mouth_open", "frowning", "wearing_glasses", "wearing_sunglasses", "wearing_lipstick", "tongue_out", "duck_face", "black_hair", "blond_hair", "brown_hair", "red_hair", "curly_hair", "straight_hair", "braid_hair", "showing_cellphone", "using_earphone", "using_mirror", "braces", "wearing_hat", "harsh_lighting", "dim_lighting" ]

dataset = './Selfie-dataset/selfie_dataset.txt'
image_dir = './Selfie-dataset/images'

def copy_images(label, set_name):
    print("copy_images:", label, "for", set_name)
    female_index = labels.index("is_female")

    if not label in labels:
        print("bad label:", label)
        quit()
    label_index = labels.index(label)
    src_dir = image_dir

    train_dir = "dataset/training/" + set_name + "/" + label
    test_dir = "dataset/testing/" + set_name + "/" + label
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)

    fp = open(dataset)
    lines = fp.readlines()
    files = []
    for line in lines:
        line = line.strip().split(" ")
        file = line[0] + ".jpg"
        score = line[1]
        cats = line[2:]
        if not cats[female_index] == "1":
            continue
        if cats[label_index] == "1":
            files.append(file)

    for i, file in enumerate(files):
            src = src_dir + "/" + file
            dst = train_dir + "/" + file
            if random.random() < 0.1666:
                dst = test_dir + "/" + file
            copyfile(src, dst)

copy_images("black_hair", "color")
copy_images("red_hair", "color")
copy_images("brown_hair", "color")
copy_images("blond_hair", "color")
copy_images("straight_hair", "curl")
copy_images("curly_hair", "curl")
copy_images("braid_hair", "curl")
copy_images("black_race", "race")
copy_images("white_race", "race")
copy_images("asian_race", "race")

