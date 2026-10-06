# 3주차 데이터 링크

## FashionMNIST

- [torchvision FashionMNIST 데이터 안내](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.FashionMNIST.html)
- [PyTorch 데이터와 DataLoader 설명](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html)

링크의 데이터 확보 기능과 사용법을 확인해 직접 다운로드하세요. 이 패키지에는 이미지나 label 파일이 들어 있지 않습니다.

## 확보한 뒤 확인할 내용

- 공식 훈련 데이터와 공식 test의 역할
- 이미지와 label의 의미 및 shape
- train과 validation의 분할 기준
- 작은 부분집합의 선택 규칙과 크기
- 데이터 보관 위치와 다운로드 여부
- 학습과 추론에 사용할 전처리

작은 부분집합을 사용할 경우 클래스 분포를 확인하세요. 줄인 데이터의 결과를 전체 데이터에서 얻은 성능으로 표현하지 않습니다. 공식 test는 최종 평가를 위해 남깁니다.

이미지와 다운로드 캐시는 로컬에 보관합니다. Git에는 출처와 확보 방법, 사용한 범위와 결과 기록을 남기세요.
