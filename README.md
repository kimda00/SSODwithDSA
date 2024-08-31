# SSOD with DSA

ssod 학습

configs/ssod/custom 안에있는 yaml파일 써야하고
데이터셋의 경우 dataset이라는 폴더안에 txt파일과 함께 저장했었음

dsa 적용 학습은
python dsa_train.py --cfg configs/ssod/custom/coco.yaml

yaml 파일은 project name 수정하고, 에폭맞게 변경하고 웨이트파일은 있는거 사용


DSA 

python divide_bs.py
로 bs별로 폴더 분리

python get_diversity_images.py
로 각 구역별 이미지 계산하고 뽑아냄.

txt파일 만들기
pythom ./utils/get_txt_file_for_ssod.py 
레이블할 이미지와 언레이블드 이미지 나눠서 txt파일 만들수 있음