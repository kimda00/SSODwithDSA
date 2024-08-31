import os
import shutil
import random

# 원본 이미지와 라벨 폴더 경로
images_folder = './base_dataset/redefined_lisa/images'
labels_folder = './base_dataset/redefined_lisa/labels'

# 이미지와 라벨 파일 리스트 불러오기
image_files = [os.path.splitext(file)[0] for file in os.listdir(images_folder)]
label_files = [os.path.splitext(file)[0] for file in os.listdir(labels_folder)]

# 파일 이름(확장자 제외)을 기준으로 이미지와 라벨 매칭
matched_files = list(set(image_files) & set(label_files))

# 매칭된 파일 수 확인
total_matched_files = len(matched_files)

# 요청한 샘플 수
sample_size = 1620

# 실제 매칭된 파일 수와 요청한 샘플 수 비교
if sample_size > total_matched_files:
    print(f"경고: 요청한 샘플 수({sample_size})가 매칭된 파일 수({total_matched_files})보다 많습니다. 사용 가능한 모든 파일을 사용합니다.")
    selected_files = matched_files
else:
    selected_files = random.sample(matched_files, sample_size)

# 새 폴더 경로
new_images_folder = 'test_dataset/randoms5/images'
new_labels_folder = 'test_dataset/randoms5/labels'

# 새 폴더 생성 (이미 존재하면 넘어감)
os.makedirs(new_images_folder, exist_ok=True)
os.makedirs(new_labels_folder, exist_ok=True)

# 선택된 파일을 새 폴더에 복사
for file_name in selected_files:
    # 이미지 파일 복사 (확장자를 다시 추가해야 함)
    shutil.copy(os.path.join(images_folder, file_name + '.jpg'),
                os.path.join(new_images_folder, file_name + '.jpg'))
    
    # 라벨 파일 복사 (확장자를 다시 추가해야 함)
    shutil.copy(os.path.join(labels_folder, file_name + '.txt'),
                os.path.join(new_labels_folder, file_name + '.txt'))

print("선택된 파일이 새 폴더에 복사되었습니다.")
