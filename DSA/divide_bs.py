import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from tqdm import tqdm
import shutil

def log_transform(values, epsilon=1e-5):
    return np.log(values + epsilon)

def calculate_features(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return brightness, laplacian_var

def normalize_values(values):
    max_value = max(values) if values else 1  # 최대값이 0이 되는 것을 방지
    return [value / max_value for value in values]

def read_label_files_from_folders(base_folders):
    label_counts = {}  # 전체 라벨별 이미지 개수를 저장할 딕셔너리

    for base_folder in base_folders:
        labels_folder_path = os.path.join(base_folder, 'labels')  # 'labels' 폴더 경로
        
        if os.path.exists(labels_folder_path) and os.path.isdir(labels_folder_path):
            label_files = [f for f in os.listdir(labels_folder_path) if f.endswith('.txt')]
            
            for label_file in label_files:
                label_file_path = os.path.join(labels_folder_path, label_file)
                
                with open(label_file_path, 'r') as file:
                    for line in file:
                        parts = line.strip().split(' ')
                        if len(parts) > 0:  # 라인에 데이터가 있는지 확인
                            label = parts[0]  # 클래스 ID
                            label_counts[label] = label_counts.get(label, 0) + 1

    return label_counts

def process_and_classify_images(base_folders, base_path, brightness_bins):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    saved_images = set()
    class_image_count = {}  # 클래스별 이미지 개수를 저장할 딕셔너리

    all_brightness_values = []
    all_sharpness_values = []

    # 이미지 경로 수집
    image_paths = []
    for base_folder in tqdm(base_folders, desc="Processing base folders"):
        image_folder = os.path.join(base_folder, 'images')
        image_paths.extend([os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')])

    # 이미지 처리 및 밝기와 선명도 값 수집
    for image_path in tqdm(image_paths, desc="Processing images"):
        if image_path in saved_images:
            continue
        image = cv2.imread(image_path)
        if image is None:
            continue

        brightness, sharpness = calculate_features(image)

        all_brightness_values.append(brightness)
        all_sharpness_values.append(sharpness)

    # 밝기와 선명도 값 정규화
    normalized_brightness_values = normalize_values(all_brightness_values)
    log_sharpness_values = [log_transform(value) for value in all_sharpness_values]
    normalized_sharpness_values = normalize_values(log_sharpness_values)
    #     # 샤프니스의 분위수 계산
    # sharpness_quantiles = np.percentile(normalized_sharpness_values, [20, 40, 60, 80])

    # # 정규화된 샤프니스 값에 기반한 동적 구간 생성
    # sharpness_bins = list(sharpness_quantiles) + [1.0]
    # 최소값과 최대값을 기준으로 5개의 구역으로 나누기 위한 경계값 계산
    min_sharpness = min(normalized_sharpness_values)
    max_sharpness = max(normalized_sharpness_values)
    interval = (max_sharpness - min_sharpness) / 5
    sharpness_bins = [min_sharpness + interval * i for i in range(1, 5)] + [max_sharpness]


    # 정규화된 값을 사용하여 이미지 분류 및 클래스 폴더 생성
    for idx, image_path in enumerate(image_paths):
        brightness_index = sum(b <= normalized_brightness_values[idx] for b in brightness_bins)
        sharpness_index = sum(s <= normalized_sharpness_values[idx] for s in sharpness_bins)
        class_folder = f'b{brightness_index}_s{sharpness_index}'
        class_path = os.path.join(base_path, class_folder)
        if not os.path.exists(class_path):
            os.makedirs(class_path)

        file_name = os.path.basename(image_path)
        save_path = os.path.join(class_path, file_name)
        shutil.copy(image_path, save_path)

        # 라벨 파일 복사
        label_file_path = image_path.replace('images', 'labels').rsplit('.', 1)[0] + '.txt'
        if os.path.exists(label_file_path):
            shutil.copy(label_file_path, class_path)

        class_image_count[class_folder] = class_image_count.get(class_folder, 0) + 1

    # 각 클래스별 이미지 개수 출력
    for class_name, count in class_image_count.items():
        print(f"{class_name}: {count} images")

    return normalized_brightness_values, normalized_sharpness_values, class_image_count, sharpness_bins


# def plot_histogram(brightness_values, sharpness_values, brightness_bins, sharpness_bins):
def plot_histogram(brightness_values, sharpness_values):

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(brightness_values, bins=50, color='blue', alpha=0.7)
    plt.title('Histogram of Brightness')
    plt.xlabel('Brightness')
    plt.ylabel('Number of Instances')
    plt.ylim(0, 1000) 
    # for edge in brightness_bins:
    #     plt.axvline(edge, color='red', linestyle='--', linewidth=1)

    plt.subplot(1, 2, 2)
    plt.hist(sharpness_values, bins=50, color='green', alpha=0.7)
    plt.title('Histogram of Sharpness') 
    plt.xlabel('Sharpness')
    plt.ylabel('Number of Instances')
    plt.ylim(0, 1000) 
    # for edge in sharpness_bins:
    #     plt.axvline(edge, color='red', linestyle='--', linewidth=1)
      
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    base_folders = ['no_remove']
    base_path = "./after"
    brightness_bins = [0.2, 0.4, 0.6, 0.8]
    # sharpness_bins = [0.4, 0.4, 0.6, 0.8]

    all_brightness_values, all_sharpness_values, class_image_count,sharpness_bins = process_and_classify_images(base_folders, base_path, brightness_bins)
    
    # 폴더 내 모든 라벨 파일에서 클래스별 개수 읽기
    label_counts = read_label_files_from_folders(base_folders)
    
    # 전체 클래스별 이미지 개수 출력 (이미지 분류 결과 + 라벨 파일 결과)
    for class_name, count in label_counts.items():
        print(f"Class {class_name} from labels: {count} images")


    # 히스토그램 그리기
    plot_histogram(all_brightness_values, all_sharpness_values)
