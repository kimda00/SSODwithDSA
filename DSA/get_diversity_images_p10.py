import os
import shutil
import random

start_path = './test_for_bs'
save_path = './no_remove/images'

if not os.path.exists(save_path):
    os.makedirs(save_path)

for i in range(0,5):
    for j in range(0,5):
        folder_name = f'b{i}_s{j}'
        folder_path = os.path.join(start_path, folder_name)
        print(folder_path)

        if os.path.exists(folder_path):
            images = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]
            num_images_to_select = max(1, len(images)//8)
            

            selected_images = random.sample(images, num_images_to_select)

            # save_folder_path = os.path.join(save_path, folder_name)
            # if not os.path.exists(save_folder_path):
            #     os.makedirs(save_folder_path)

            for image in selected_images:
                src_path = os.path.join(folder_path, image)
                dst_path = os.path.join(save_path, image)
                shutil.copy(src_path, dst_path)

            print(f'Selected {num_images_to_select} images from {folder_name} folder.')