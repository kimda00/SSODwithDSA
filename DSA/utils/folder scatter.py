import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_brightness_and_sharpness(image_path):
    image = cv2.imread(image_path)
    if image is None:
        return None, None  # 이미지가 없을 경우
    
    # 밝기 계산
    brightness = np.mean(image)
    
    # 라플라시안을 사용한 선명도 계산
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    sharpness = np.var(laplacian)
    
    return brightness, sharpness

def calculate_average_brightness_sharpness(folder_path):
    brightness_list = []
    sharpness_list = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            brightness, sharpness = calculate_brightness_and_sharpness(file_path)
            if brightness is not None and sharpness is not None:
                brightness_list.append(brightness)
                sharpness_list.append(sharpness)
    
    avg_brightness = np.mean(brightness_list) if brightness_list else 0
    avg_sharpness = np.mean(sharpness_list) if sharpness_list else 0
    
    return avg_brightness, avg_sharpness

def process_folders_and_plot(base_path):
    brightness_values = []
    sharpness_values = []
    colors = []
    folder_indices = []
    
    for index, folder_name in enumerate(sorted(os.listdir(base_path))):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            avg_brightness, avg_sharpness = calculate_average_brightness_sharpness(folder_path)
            brightness_values.append(avg_brightness)
            sharpness_values.append(avg_sharpness)
            colors.append(np.random.rand(3,))  # 무작위 색상 생성
            folder_indices.append(folder_name)  # 폴더 인덱스 추가
    
    plt.figure(figsize=(10, 6))
    plt.scatter(brightness_values, sharpness_values, c=colors)
    for i, txt in enumerate(folder_indices):
        plt.annotate(txt, (brightness_values[i], sharpness_values[i]), fontsize=13)  # 점 옆에 폴더 인덱스 표시
    plt.title('Average Brightness and Sharpness')
    plt.xlabel('Average Brightness')
    plt.ylabel('Average Sharpness')
    plt.grid(True)
    plt.savefig('./average_brightness_sharpness_with_indices.png')
    plt.show()

# base_path는 폴더들이 위치한 실제 경로로 설정해야 합니다.
base_path = 'p1_msssim'
process_folders_and_plot(base_path)
