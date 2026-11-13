# L06 입력 파일 역할 구분 및 데이터 출처 기록

## 1. 실제 사용한 데이터 출처 및 해시 (DATA.md 기준)
- **데이터 출처**: 공개 Titanic CSV 미러 (`https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`)
  - *참고*: Kaggle에서 직접 다운로드하지 않고 동일 스키마의 공개 미러를 사용함
- **저장 경로**: `data/titanic.csv`
- **SHA-256 해시**: `4a437fde05fe5264e1701a7387ac6fb75393772ba38bb2c9c566405af5af4bd7`
- **행·열 규격**: 891행 × 12열
- **열 목록**: `['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']`

## 2. Kaggle Titanic 파일별 역할 구분표
| 파일 구분 | 포함 내용 | 본 과제에서의 역할 | 정답(Survived) 사용 여부 |
|---|---|---|---|
| `train.csv` (`data/titanic.csv`) | `Survived`(정답)가 포함된 891행 데이터 | **학습(534)·검증(178)·홀드아웃(179) 분할 및 모델 학습/평가용** | **O (정답 라벨로 사용)** |
| `test.csv` | `Survived` 열이 없는 418행 추론 대상 데이터 | Kaggle 대회 제출용 비라벨 테스트 데이터 | **X (정답으로 절대 사용 안 함)** |
| `gender_submission.csv` (예시 제출) | `PassengerId`와 임의 예측 `Survived` 예시 형식 | 제출 CSV 포맷 확인용 예시 파일 | **X (정답으로 절대 사용 안 함)** |
