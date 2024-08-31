import os
import random

TEXT_EXT = [".txt"]
IMAGE_EXT = [".jpg", ".png"]

def get_image_list(path):
    image_names = []
    for maindir, subdir, file_name_list in os.walk(path):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            ext = os.path.splitext(apath)[1]
            if ext in IMAGE_EXT:
                image_names.append(apath)
    return image_names

if __name__ == '__main__':
    image_path = './train/images'
    images = get_image_list(image_path)

    random.shuffle(images)

    # 이미지 리스트를 분할(10%는 labeled, 나머지 90%는 unlabeled)
    split_point = int(len(images) * 0.2)
    labeled_images = images[:split_point]
    unlabeled_images = images[split_point:]

    with open("p20_labeled_train.txt", "w") as f:
        for img in labeled_images:
            img = img.replace("\\", "/")
            f.writelines(img + '\n')

    with open("p20_unlabeled_train.txt", "w") as f:
        for img in unlabeled_images:
            img = img.replace("\\", "/")
            f.writelines(img + '\n')
