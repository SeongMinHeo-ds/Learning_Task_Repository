# 2주차 데이터 링크

## Titanic

- [Kaggle Titanic 데이터 페이지](https://www.kaggle.com/competitions/titanic/data)
- [대회 소개](https://www.kaggle.com/competitions/titanic)

데이터는 링크에서 직접 확보합니다. 계정이나 대회 규칙 확인이 필요할 수 있습니다. 원본 파일은 이 패키지에 포함하지 않습니다.

## 파일별 확인 사항

| 파일 | 직접 확인할 내용 |
|---|---|
| train.csv | 입력과 생존 정답이 있는 데이터의 역할 |
| test.csv | 정답이 없는 예측 대상 데이터의 역할 |
| gender_submission.csv | 제출 형식과 예시 예측의 역할 |

예시 제출 파일의 예측값을 평가용 정답으로 사용하지 않습니다. 로컬 최종 평가에는 `train.csv` 안에서 따로 남긴 holdout을 사용합니다.

출처, 확보 날짜, 파일의 행·열 수, 정답·ID 열과 로컬 위치를 기록하세요. 원본은 변경하지 않고 처리 결과를 별도로 저장합니다.

## 접근이 막힐 때 사용할 데이터

- [UCI Wine 데이터](https://archive.ics.uci.edu/dataset/109/wine)

교육자에게 접근 문제를 알리고 대체 여부를 확인합니다. Wine을 사용할 때도 분할, DummyClassifier baseline, 두 모델 비교, Pipeline, 저장·재로드 목표는 유지합니다. 데이터에 결측이 없더라도 선택한 전처리의 동작과 필요성을 설명하세요.

대체 과제의 예측 CSV는 본인이 부여한 `row_id`와 `predicted_class`를 담고, 사용한 정답 값의 의미를 기록합니다. Kaggle 제출은 수행하지 않습니다. UCI 원본과 라이브러리 버전 데이터의 label 값이 다를 수 있으므로 실제 사용한 값을 확인하세요.
