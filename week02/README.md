# 2주차 pandas 데이터 처리와 머신러닝

이번 주 실습은 **Titanic 분류와 재사용 가능한 예측 CLI**입니다. 대응 ID는 L06~L10, 계획시간은 30시간입니다.

[참고 자료](RESOURCES.md) · [데이터와 모델 링크](DATA.md) · [체크리스트](CHECKLIST.md)

## 과제

Titanic 데이터를 확보하고 pandas로 결측·중복·자료형·분포를 확인합니다. 상세 탐색과 전처리 결정 전에 train, validation, holdout을 나누고 분할 규칙과 seed를 기록합니다.

groupby 집계표와 원본을 key로 결합해 merge 전후 행 수와 key 중복을 확인합니다. train에서 얻은 통계를 다른 데이터에 적용하는 과정과 전체 데이터에서 통계를 만드는 과정의 차이를 설명합니다.

DummyClassifier, LogisticRegression, 작은 DecisionTreeClassifier를 동일 validation에서 비교합니다. 필요한 결측 처리, scaling과 범주 인코딩을 ColumnTransformer와 Pipeline으로 묶고 train에만 fit합니다.

모델과 설정을 확정한 뒤 holdout을 한 번 평가합니다. Pipeline을 저장·재로드하고 예측 CSV를 만듭니다. 학습과 예측 실행 기능, 로그와 실패 입력을 정리합니다. Kaggle 제출은 선택입니다.

## 일별 작업과 결과

| 일차 | ID | 작업 | 산출물 |
| --- | --- | --- | --- |
| 6 | L06 | pandas 정리 집계 결합 | 결측·dtype·groupby·merge 기록 |
| 7 | L07 | 분할과 baseline 평가 | 고정 분할과 Dummy 평가 |
| 8 | L08 | 전처리 Pipeline과 모델 비교 | 동일 조건 모델 2개 비교표 |
| 9 | L09 | 오류 분석과 모델 저장 | holdout·오류 사례·재로드 비교 |
| 10 | L10 | ML CLI와 재현 리뷰 | 학습·예측 명령과 실패 입력 기록 |

## 제출할 산출물

- pandas 처리와 merge 검증 기록
- 분할·baseline·모델 비교표
- confusion matrix와 확정 모델 holdout 평가
- 저장·재로드·예측 CLI와 README

## 주간 완료 기준

전처리 fit 대상과 데이터 분할을 코드에서 보여주고 저장한 Pipeline으로 새 입력을 예측한다.

**선택 확장:** 큰 모델, 광범위한 튜닝과 Kaggle 순위 경쟁은 확장 과제입니다.

코드 구조와 명령 이름은 직접 정하고 실제 사용 방법을 README에 기록합니다. [주간 보고서](../templates/WEEKLY_REPORT.md)에 실행·설명·검증 증빙을 남기세요. LLM과 RAG 평가는 [공통 평가 기준](../EVALUATION.md)을 사용합니다.
