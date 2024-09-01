# SSOD with DSA

# SSOD 학습

## 환경 설정 및 데이터셋 준비
1. configs/ssod/custom 안에있는 yaml파일에 사용할 데이터셋의 경로 저장
2. 데이터셋의 경우 dataset이라는 폴더안에 txt파일과 함께 저장

## Data Selection 적용한 학습

```bash
python dsa_train.py --cfg configs/ssod/custom/coco.yaml

yaml 파일 설정 :
 - project name 수정
 - 필요한 경우 에폭 값 변경
 - 필요한 경우 웨이트 파일 변경

# DSA 

1. BS 별 폴더 분리
```bash
python divide_bs.py

2. 각 구역 별 이미지 계산 후 추출

```bash
python get_diversity_images.py

3. txt파일 만들기
labeled, unlabeled 이미지를 분리하여 txt파일 제작


```bash
pythom ./utils/get_txt_file_for_ssod.py 
