# 2주차 참고 자료

과제를 읽고 현재 작업에 필요한 자료부터 찾아보세요. 공식 예제는 참고할 수 있지만 과제의 입력·출력·설정에 맞추어 직접 구현하고 변경 내용을 설명합니다.

| 자료 | 찾아볼 내용 | 읽을 시점 |
| --- | --- | --- |
| [pandas 입문](https://pandas.pydata.org/docs/user_guide/10min.html) | 결측·자료형·집계와 선택 복습 | 먼저 |
| [pandas merge와 join](https://pandas.pydata.org/docs/user_guide/merging.html) | key, 결합 유형과 중복으로 인한 행 수 변화 | 먼저 |
| [데이터 누수와 흔한 실수](https://scikit-learn.org/stable/common_pitfalls.html) | fit 대상과 전처리 일관성 | 먼저 |
| [Pipeline과 ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html) | 전처리와 모델 연결 | 먼저 |
| [분할 API](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) | 분할·seed·계층화 | 필요할 때 |
| [scikit-learn API](https://scikit-learn.org/stable/api/index.html) | baseline·분류기·인코딩·결측 처리 | 필요할 때 |
| [분류 지표](https://scikit-learn.org/stable/modules/model_evaluation.html) | accuracy와 confusion matrix | 필요할 때 |
| [모델 저장](https://scikit-learn.org/stable/model_persistence.html) | Pipeline 저장·재로드와 환경 기록 | 필요할 때 |

## 확인 질문

- L06: merge 후 행 수가 늘었다면 어떤 key를 먼저 확인하나요?
- L07: validation을 보고 고른 모델의 최종 평가에는 어떤 데이터를 써야 하나요?
- L08: scaling과 결측 통계가 어디서 계산되는지 코드에서 보여주세요.
- L09: 저장 전후 예측이 같다는 것을 무엇으로 확인했나요?
- L10: 학습을 다시 실행하지 않고 예측만 수행할 수 있나요?

자료 확인일: 2026-10-06. 문서의 버전과 실제 사용한 버전이 다를 수 있으므로 실행 환경과 모델 revision을 남깁니다.
