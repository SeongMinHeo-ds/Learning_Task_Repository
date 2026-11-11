# 2주차 Titanic 전처리·학습·저장과 예측

**목표:** 전처리를 train에만 fit하고 baseline·두 분류기를 비교한 뒤 확정한 모델을 저장·재로드해 예측한다.

수행 방식: **실제 pandas·scikit-learn 실행**. 주 5일·하루 6시간, 총 30시간이다. 아래 순서와 기준 설정으로 먼저 완료하고 확장은 그다음에 한다.

[입력 자료](DATA.md) · [참고 링크](RESOURCES.md) · [완료 체크](CHECKLIST.md)

## 1. 시작 전 준비와 기준 설정

1. 입력은 정답이 있는 Titanic 891행이다. Kaggle train.csv 또는 DATA.md에 기재한 공개 미러를 사용하고 실제 출처·파일 hash를 기록한다.
2. Survived는 정답, PassengerId는 ID. feature는 Age·Fare·SibSp·Parch·Pclass·Sex·Embarked만 사용한다. Name·Ticket·Cabin·ID·정답은 feature에서 제외한다.
3. train_test_split을 두 번 사용한다. 첫 번째 test_size=0.4, random_state=42, stratify=Survived. 남은 묶음에서 test_size=0.5, random_state=42, stratify=Survived로 나누면 train 534·validation 178·holdout 179행이다.
4. 숫자 5개는 train 중앙값 대체+표준화, 범주 2개는 train 최빈값 대체+OneHotEncoder(handle_unknown='ignore'). Dummy most_frequent, LogisticRegression(max_iter=1000, random_state=42), DecisionTreeClassifier(max_depth=3, random_state=42)를 비교한다.
5. 선택 기준은 validation accuracy. 동률이면 LogisticRegression을 먼저 선택한다. 확정 뒤 train만으로 fit한 선택 모델을 그대로 holdout에서 한 번 평가한다. holdout 결과로 설정을 바꾸지 않는다.

저장소 루트에 src/, data/, outputs/week02/를 준비한다. 아래 명령의 src 파일은 직접 작성할 프로그램이며 미리 완성된 코드가 아니다. DATA.md의 링크와 라이브러리 이름으로 환경을 준비한다. 데이터·가중치·가상환경을 Git에 추가하지 않는다.

## 2. 기준 실행 흐름

```text
python src/titanic_cli.py train --input data/titanic.csv --output-dir outputs/week02 --seed 42
```

입력 준비 → 일별 작업 → 결과 파일 생성 → 정상·실패 비교 → 보고서 순서로 진행한다.

## 3. 1일차 · L06 입력 확인·분할 후 pandas 점검

### 1-1. 수행

train.csv·test.csv·예시 제출 파일의 역할을 구분한다. 정답이 있는 891행에서 정해 둔 규칙으로 세 분할을 먼저 만든다.

- **나와야 할 것:** 입력 역할 표, split_info.json 초안
- **확인 방법:** Kaggle test.csv와 예시 제출 파일을 정답으로 사용하지 않는다.

### 1-2. 수행

train에서 결측·dtype·중복·분포를 정리하고 Pclass별 Fare 평균과 그룹 행 수를 집계한다.

- **나와야 할 것:** data_report.md, train_group_summary.csv
- **확인 방법:** 전체 891행 통계와 train 전용 통계를 혼동하지 않는다.

### 1-3. 수행

Pclass로 집계표를 원본 train에 left merge하고 many_to_one 관계를 확인한다. 오른쪽 key가 중복된 예도 작은 복사본에서 재현한다.

- **나와야 할 것:** merge_validation.json
- **확인 방법:** 정상 결합 전후 534행과 PassengerId 대응이 유지된다. 연습용 집계 열은 모델 feature에 추가하지 않는다.

## 4. 2일차 · L07 분할 고정·baseline 평가

### 2-1. 수행

각 분할 PassengerId와 크기·seed를 저장하고 ID 교집합을 확인한다.

- **나와야 할 것:** split_info.json
- **확인 방법:** 세 집합은 겹치지 않고 합집합은 891개다.

### 2-2. 수행

DummyClassifier(strategy='most_frequent')를 train에 fit하고 validation에서 accuracy와 binary F1을 구한다.

- **나와야 할 것:** model_comparison.csv의 baseline 행
- **확인 방법:** 어떤 복잡한 모델도 쓰지 않은 기준 성능임을 설명한다.

### 2-3. 수행

accuracy와 F1의 분모, 양성 클래스 Survived=1, holdout을 남기는 이유를 기록한다.

- **나와야 할 것:** 평가 기준 설명
- **확인 방법:** validation 결과로 모델을 고르는 동안 holdout 지표를 보지 않는다.

## 5. 3일차 · L08 전처리 Pipeline과 두 모델 비교

### 3-1. 수행

숫자·범주 열 처리기를 ColumnTransformer로 합치고 모델과 Pipeline으로 연결한다.

- **나와야 할 것:** 전처리 구조와 feature 목록
- **확인 방법:** imputer·scaler·encoder와 모델 모두 train에만 fit한다.

### 3-2. 수행

LogisticRegression과 깊이 3 tree를 각각 학습하고 같은 validation 178행에서 예측한다.

- **나와야 할 것:** 세 모델의 model_comparison.csv
- **확인 방법:** model, settings, fit_partition, validation_rows, accuracy, f1을 남긴다.

### 3-3. 수행

accuracy가 높은 후보를 선택하고 동률 규칙까지 기록한다. 선택 시점의 설정을 고정한다.

- **나와야 할 것:** 선택 이유와 확정 설정
- **확인 방법:** holdout을 확인한 후 모델을 바꾸지 않는다.

## 6. 4일차 · L09 오류 분석·holdout·저장 검증

### 4-1. 수행

선택 모델의 validation confusion matrix를 실제 행·예측 열로 만들고 오분류 5개를 찾는다.

- **나와야 할 것:** validation_confusion_matrix.csv, validation_errors.csv
- **확인 방법:** 행·열의 0/1 의미와 각 오류 사례의 ID·정답·예측을 설명한다.

### 4-2. 수행

확정 모델을 holdout 179행에서 한 번 평가하고 ID·예측·실제 정답을 저장한다.

- **나와야 할 것:** holdout_result.json, holdout_predictions.csv
- **확인 방법:** CSV에서 직접 다시 구한 accuracy가 JSON 결과와 일치한다.

### 4-3. 수행

전처리를 포함한 Pipeline을 저장하고 다시 로드한다. 같은 입력의 예측을 저장 전후 대조한다.

- **나와야 할 것:** reload_check.json
- **확인 방법:** 불일치 개수 0인지 확인한다. 새 프로세스 검증 여부는 실제 수행한 범위대로 쓴다.

## 7. 5일차 · L10 학습·예측 인터페이스와 재현

### 5-1. 수행

train 실행과 predict 실행을 구분한다. predict는 저장된 Pipeline을 읽어 새 CSV를 처리하고 재학습하지 않는다.

- **나와야 할 것:** src/titanic_cli.py와 실행 README
- **확인 방법:** 입력·모델·출력 경로를 인자로 바꿀 수 있다.

### 5-2. 수행

파일 없음·필수 열 없음·입력 행 순서 변경을 확인한다.

- **나와야 할 것:** error_cases.csv와 ID 대응 결과
- **확인 방법:** 순서를 바꾼 입력에서도 PassengerId별 예측이 대응해야 한다.

### 5-3. 수행

새 터미널에서 기준 실행을 재현하고 주요 함수·fit 대상·선택 이유를 설명한다.

- **나와야 할 것:** 주간 보고서와 증빙
- **확인 방법:** 작은 지표 차이는 버전·환경과 함께 기록하며 특정 정확도를 합격선으로 삼지 않는다.

## 8. 제출 파일과 확인 기준

| 파일 | 내용·필드 | 확인 기준 |
| --- | --- | --- |
| split_info.json | seed, rule, train/validation/holdout_rows, 각 PassengerId | 534/178/179, ID 교집합 0 |
| data_report.md / train_group_summary.csv / merge_validation.json | train 결측·집계·key·전후 행 수 | merge 전후 534행 |
| model_comparison.csv | baseline·LogisticRegression·tree의 설정과 validation 지표 | 세 행, 같은 validation |
| validation_confusion_matrix.csv / validation_errors.csv | 정답·예측 행렬과 실제 오분류 5건 | 행렬 합 178 |
| holdout_result.json / holdout_predictions.csv | 선택 모델·features·지표, PassengerId·Survived·actual_Survived | 179행에서 지표 재계산 가능 |
| reload_check.json / error_cases.csv | 저장·재로드 일치, 오류·순서 변경 | 검증한 프로세스 범위 명시 |

## 9. 주간 완료와 막혔을 때

저장한 Pipeline으로 재학습 없이 예측하고, 세 분할과 전처리 fit 대상 및 오류 사례를 설명한다.

각 L 번호마다 코드 또는 웹 관찰, 실제 결과 파일, 짧은 설명을 연결한다. 결과 숫자가 다르면 입력 파일·분할 index·버전·설정부터 대조한다. 오류가 나면 입력, 기대 결과, 실제 메시지, 시도한 내용을 기록한다. 미실행·미측정·미채점은 그대로 표시한다.

[주간 보고서 양식](../templates/WEEKLY_REPORT.md)에 실제 시간·증빙·참고 자료와 AI 사용 범위를 적는다. 웹 실험은 브라우저에서 계산한 값과 시뮬레이션 응답을 구분한다.
