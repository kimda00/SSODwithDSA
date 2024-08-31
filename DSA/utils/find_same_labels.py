import os
import shutil

images_names=[]
image_dir = 'ssim/ssim_train/images'

label_dst_dir='ssim/ssim_train/labels'
if not os.path.exists(label_dst_dir):
    os.makedirs(label_dst_dir)

for image_file in os.listdir(image_dir):
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        images_name = os.path.splitext(image_file)[0]
        images_names.append(images_name)
print(len(images_names))
label_dirs = ['base_dataset/redefined_lisa/labels', 'base_dataset/redefined_mobinha/labels']

for label_dir in label_dirs:
    print(label_dir)
    for label_file in os.listdir(label_dir):
        # if label_name.endswith('.txt'):
        label_name = os.path.splitext(label_file)[0]
        if label_name in images_names:
            label_src_path = os.path.join(label_dir, label_file)
            label_dst_path = os.path.join(label_dst_dir, label_file)
            shutil.copy(label_src_path, label_dst_path)
