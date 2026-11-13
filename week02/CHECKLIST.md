# 2주차 완료 체크리스트

[상세 가이드](README.md)의 각 일차를 완료한 뒤 실제 증빙을 연결한다.

## L06 입력 확인·분할 후 pandas 점검

- [x] 입력 역할 표, split_info.json 초안: Kaggle test.csv와 예시 제출 파일을 정답으로 사용하지 않는다.
- [x] data_report.md, train_group_summary.csv: 전체 891행 통계와 train 전용 통계를 혼동하지 않는다.
- [x] merge_validation.json: 정상 결합 전후 534행과 PassengerId 대응이 유지된다. 연습용 집계 열은 모델 feature에 추가하지 않는다.

증빙 경로·링크:
- 실행 코드: week02/L06_prepare_and_check.py
- 역할·출처 기록: week02/L06_input_roles.md
- 산출물: outputs/week02/split_info.json, outputs/week02/data_report.md, outputs/week02/train_group_summary.csv, outputs/week02/merge_validation.json

## L07 분할 고정·baseline 평가

- [ ] split_info.json: 세 집합은 겹치지 않고 합집합은 891개다.
- [ ] model_comparison.csv의 baseline 행: 어떤 복잡한 모델도 쓰지 않은 기준 성능임을 설명한다.
- [ ] 평가 기준 설명: validation 결과로 모델을 고르는 동안 holdout 지표를 보지 않는다.

증빙 경로·링크:

## L08 전처리 Pipeline과 두 모델 비교

- [ ] 전처리 구조와 feature 목록: imputer·scaler·encoder와 모델 모두 train에만 fit한다.
- [ ] 세 모델의 model_comparison.csv: model, settings, fit_partition, validation_rows, accuracy, f1을 남긴다.
- [ ] 선택 이유와 확정 설정: holdout을 확인한 후 모델을 바꾸지 않는다.

증빙 경로·링크:

## L09 오류 분석·holdout·저장 검증

- [ ] validation_confusion_matrix.csv, validation_errors.csv: 행·열의 0/1 의미와 각 오류 사례의 ID·정답·예측을 설명한다.
- [ ] holdout_result.json, holdout_predictions.csv: CSV에서 직접 다시 구한 accuracy가 JSON 결과와 일치한다.
- [ ] reload_check.json: 불일치 개수 0인지 확인한다. 새 프로세스 검증 여부는 실제 수행한 범위대로 쓴다.

증빙 경로·링크:

## L10 학습·예측 인터페이스와 재현

- [ ] src/titanic_cli.py와 실행 README: 입력·모델·출력 경로를 인자로 바꿀 수 있다.
- [ ] error_cases.csv와 ID 대응 결과: 순서를 바꾼 입력에서도 PassengerId별 예측이 대응해야 한다.
- [ ] 주간 보고서와 증빙: 작은 지표 차이는 버전·환경과 함께 기록하며 특정 정확도를 합격선으로 삼지 않는다.

증빙 경로·링크:
