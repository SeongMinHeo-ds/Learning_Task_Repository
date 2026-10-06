# 2주차 참고 자료

과제를 읽고 데이터 흐름과 평가 조건을 먼저 정리하세요. 필요한 API는 공식 문서에서 직접 찾아 적용합니다.

## 먼저 볼 자료

| 자료 | 찾아볼 내용 | 연결 목표 |
|---|---|---|
| [Titanic 대회 소개](https://www.kaggle.com/competitions/titanic) | 예측 문제, 데이터와 결과의 의미 | L06 |
| [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) | 분할, seed, 계층화 | L07 |
| [Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | 데이터 누수와 전처리 일관성 | L07·L08 |
| [Pipeline과 ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html) | 전처리와 모델 연결, 열별 처리 | L08 |

## 구현 중 찾아볼 자료

| 자료 | 찾아볼 내용 | 연결 목표 |
|---|---|---|
| [scikit-learn API 목록](https://scikit-learn.org/stable/api/index.html) | DummyClassifier, LogisticRegression, DecisionTreeClassifier, 결측 처리와 인코딩 | L07~L09 |
| [분류 평가 지표](https://scikit-learn.org/stable/modules/model_evaluation.html) | accuracy, confusion matrix와 지표의 한계 | L09 |
| [Model persistence](https://scikit-learn.org/stable/model_persistence.html) | Pipeline 저장, 재로드와 환경 기록 | L10 |

## 읽은 뒤 확인할 질문

- baseline은 무엇과 비교하기 위한 것인가요?
- train, validation, holdout과 Kaggle test 파일은 어떤 차이가 있나요?
- 결측값 처리 기준을 전체 데이터에서 계산하면 평가에 어떤 영향을 줄 수 있나요?
- 처음 보는 범주가 들어오면 선택한 전처리는 어떻게 동작하나요?
- 정확도가 같은 모델이라도 다른 오류를 낼 수 있나요?
- 전처리를 포함해 저장하는 이유는 무엇인가요?

출처 확인일: 2026-10-06.
