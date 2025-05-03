# SSOD with DSA

이 프로젝트는 "데이터 선별 및 준지도 객체 검출 기반 유니버설 신호등 인식" 졸업 논문을 위한 코드 실행 및 실험 환경입니다.

본 연구는 YOLOv7 기반 준지도 학습(SSOD)과 데이터 선별 알고리즘을 결합하여
다양한 국가의 신호등 인식을 최소한의 라벨링 데이터로도 가능하게 하는 모델을 구축하는 것을 목표로 합니다.

## 연구 목적
- 국가마다 다른 교통 신호등 형태 및 의미를 인식할 수 있는 범용 신호등 인식 기술 개발
- 라벨링 데이터 구축 비용과 시간을 절감
- 준지도 학습과 데이터 선별 기법 결합을 통한 성능 향상

## 주요 기능
- YOLOv7 기반 준지도 객체 검출(SSOD) 모델 학습
- 밝기/선명도 기반 데이터 선별 알고리즘 적용
- labeled/unlabeled 데이터 분리 및 txt 파일 자동 생성
- 실험 환경과 단계별 실행 스크립트 제공

## 개발 환경
- Python 3.x
- PyTorch
- YOLOv7
- CUDA 환경 (GPU)

## 프로젝트 실행 순서

1. SSOD 학습 환경 설정
- configs/ssod/custom/ 폴더 안의 yaml 파일에 데이터셋 경로 지정
- dataset 폴더 안에 데이터(txt 파일 포함)를 저장
- yaml 파일 설정:
    - project name 수정
    - 필요한 경우 epochs, weights 경로 수정
      
![image](https://github.com/user-attachments/assets/e771469e-e50e-469d-ae64-02164e3c509d)

2. 데이터 선별 알고리즘 적용
- **밝기와 선명도 기반**으로 데이터를 선별하는 알고리즘 제안.
- 선별된 데이터를 이용해 더 높은 성능을 낼 수 있는 라벨링 데이터셋 구축.
![image](https://github.com/user-attachments/assets/7856af6c-80cc-4c25-9de5-9c02d1922cf7)

#### BS 별 폴더 분리
```bash
python divide_bs.py
```

#### 각 구역 별 이미지 계산 후 추출
```bash
python get_diversity_images.py
```

#### labeled, unlabeled txt 파일 제작
```bash
python ./utils/get_txt_file_for_ssod.py
```

3. Data Selection 적용한 SSOD 학습
```bash
python dsa_train.py --cfg configs/ssod/custom/coco.yaml
```

---

## 📊 실험 결과 요약
- 5% 라벨링 데이터로도 지도학습 10%보다 높은 성능 달성
- 데이터 선별 알고리즘 적용 시 비적용 대비 성능 향상
- 일부 데이터셋에서 100% 지도학습 대비 준지도학습이 더 높은 성능
- 훈련 시간 단축 (예: 10.1일 → 1.5일)
![image](https://github.com/user-attachments/assets/d8386daf-ae88-4b4e-a20e-9a5eb7f9b2fd)

mAP50 및 F1-score 주요 결과:
- LOKI: mAP50=0.935 / F1=0.919 (40% 라벨링)
- DSTLD: mAP50=0.569 / F1=0.618 (50% 라벨링)

---

## ✅ 결론 및 기대 효과
- 글로벌 자율주행 기술에 적용 가능한 범용 신호등 인식 기술 확보
- 라벨링 비용/시간 절감 가능
- 효율적인 학습 및 인식 방법론 제안

---
추가적인 실험 및 논문 정보
- 김다영, "데이터 선별 및 준지도 객체 검출 기반 유니버설 신호등 인식", 제어로봇시스템학회, 2024년 5월
[논문 링크](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003105682)

