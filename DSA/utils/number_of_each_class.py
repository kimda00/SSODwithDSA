import os
import matplotlib.pyplot as plt
from collections import defaultdict

def count_classes(directory):
    class_counts = defaultdict(int)
    for filename in os.listdir(directory):
        if filename.endswith('.txt') and not filename.startswith('classes'):  # 'classes.txt' 제외
            with open(os.path.join(directory, filename), 'r') as file:
                for line in file:
                    class_id = int(line.split()[0])
                    class_counts[class_id] += 1
    return class_counts

folder1 = 'inhacv_msssid_test/labels'
folder2 = 'lisa_msssid_test/labels'

total_counts = defaultdict(int)
for folder in [folder1, folder2]:
    counts = count_classes(folder)
    for key, value in counts.items():
        total_counts[key] += value

# 클래스 ID와 빈도수로 히스토그램 생성
classes = list(total_counts.keys())
frequencies = [total_counts[class_id] for class_id in classes]

plt.bar(classes, frequencies)
plt.xlabel('Class ID')
plt.ylabel('Frequency')
plt.title('Combined Class Distribution Histogram')
plt.show()

# 총 라벨 수와 각 클래스별 라벨 수 출력
total_labels = sum(total_counts.values())
print(f'Total number of labels: {total_labels}')
for class_id in sorted(total_counts):
    print(f'Class ID {class_id}: {total_counts[class_id]} labels')