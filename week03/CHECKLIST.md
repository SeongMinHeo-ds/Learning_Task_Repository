# 3주차 완료 체크리스트

[상세 가이드](README.md)의 각 일차를 완료한 뒤 실제 증빙을 연결한다.

## L11 데이터·tensor·gradient 확인

- [ ] training_config.json 초안: train·validation index가 겹치지 않고 test는 공식 별도 묶음이다.
- [ ] tensor_shapes_and_gradient.json: 이미지는 [128,1,28,28] float32, label은 [128] int64다.
- [ ] 작은 gradient 결과: gradient [4,6]과 requires_grad의 역할을 설명한다.

증빙 경로·링크:

## L12 MLP forward와 loss

- [ ] 층별 입력·출력 표: [128,784]→[128,64]→[128,10] 흐름을 확인한다.
- [ ] loss·logits·정답 조건 기록: loss 전에 softmax를 중복 적용하지 않는다. label dtype과 범위를 확인한다.
- [ ] 오류 관찰 기록: 어느 조건이 loss 입력과 맞지 않는지 설명한다.

증빙 경로·링크:

## L13 학습 루프와 5 epoch 기록

- [ ] 학습 루프와 역할 설명: 업데이트 전후 파라미터가 실제로 달라지는지 작은 배치로 확인한다.
- [ ] training_history.csv: 정확히 5행이며 loss는 샘플 수로 가중 평균한다.
- [ ] 선택 기준과 checkpoint 기록: 마지막 epoch와 best epoch를 무조건 같다고 가정하지 않는다.

증빙 경로·링크:

## L14 최종 평가·그림·별도 재로드

- [ ] learning_curves.png, misclassified_examples.png/.json: 그림의 값은 CSV와 같아야 하며 원인을 이미지 하나만으로 단정하지 않는다.
- [ ] test_result.json: 평가 개수와 선택 규칙을 명시하고 전체 10000개 성능으로 표시하지 않는다.
- [ ] reload_check.json: logits는 atol=1e-5로 대조하고 최대 오차·예측 일치·별도 프로세스 여부를 기록한다.

증빙 경로·링크:

## L15 Attention 축과 causal mask

- [ ] attention_results.json의 mask 없는 값: 점수 [3,3], 가중치 [3,3], 출력 [3,2]를 확인한다.
- [ ] mask 전후 가중치와 출력: 미래 위치 가중치 합은 0, 각 행의 합은 약 1이다.
- [ ] attention_notes.md: 다음 토큰 예측에서 미래 정보를 막는 이유와 전체 Transformer 구현과의 차이를 설명한다.

증빙 경로·링크:
