# L06 Train 데이터 전용 점검 보고서 (data_report.md)

> **주의**: 데이터 누수 방지를 위해 전체 891행이 아닌 **오직 train 분할 534행만**을 대상으로 산출한 통계입니다.

## 1. 기본 규격 및 중복 점검 (train 534행 기준)
- **분석 대상 행 수**: 534행 (전체 891행 중 60%)
- **전체 행 중복 건수**: 0건
- **`PassengerId` 중복 건수**: 0건
- **타깃(`Survived`) 분포**: 0(사망) = 329명, 1(생존) = 205명

## 2. 열별 자료형(dtype) 및 결측치 현황 (train 534행 기준)
| 열 이름 | 자료형 (dtype) | 결측치 수 (Missing) | 결측 비율 (%) |
|---|---|---|---|
| `PassengerId` | `int64` | 0 | 0.0% |
| `Survived` | `int64` | 0 | 0.0% |
| `Pclass` | `int64` | 0 | 0.0% |
| `Name` | `str` | 0 | 0.0% |
| `Sex` | `str` | 0 | 0.0% |
| `Age` | `float64` | 107 | 20.04% |
| `SibSp` | `int64` | 0 | 0.0% |
| `Parch` | `int64` | 0 | 0.0% |
| `Ticket` | `str` | 0 | 0.0% |
| `Fare` | `float64` | 0 | 0.0% |
| `Cabin` | `str` | 419 | 78.46% |
| `Embarked` | `str` | 2 | 0.37% |

## 3. 모델 사용 Feature 7개 요약 통계 (train 534행 기준)
- **수치형 5개**: `Age`, `Fare`, `SibSp`, `Parch`, `Pclass`
- **범주형 2개**: `Sex`, `Embarked`
- **제외 열**: `PassengerId`(ID), `Survived`(정답), `Name`, `Ticket`, `Cabin`

## 4. Pclass별 행 수 및 Fare 평균 (`train_group_summary.csv` 요약)
| Pclass | train_rows | mean_fare |
|---|---|---|
| 1 | 128 | 84.0624 |
| 2 | 109 | 21.149 |
| 3 | 297 | 13.0022 |
