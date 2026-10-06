# 3주차 목표 체크리스트

직접 실행·설명·검증하고 증빙을 남긴 조건만 체크합니다. 각 ID는 엑셀의 같은 작업 ID와 대응합니다.

## L11 tensor autograd와 DataLoader

완료 조건: NumPy와 tensor의 dtype·shape, batch와 gradient 계산을 작은 입력으로 설명한다.

- [ ] NumPy와 tensor 변환·dtype·장치를 비교한다.
- [ ] DataLoader의 이미지·label shape를 확인한다.
- [ ] 작은 연산의 gradient와 requires_grad를 확인한다.

증빙 경로 또는 링크:

## L12 MLP forward와 loss

완료 조건: flatten·Linear·activation·logits와 loss 입력의 shape·dtype을 설명한다.

- [ ] 작은 MLP를 직접 구성한다.
- [ ] 층별 입력·출력 shape와 logits를 확인한다.
- [ ] loss의 출력과 정답 입력 조건을 설명한다.

증빙 경로 또는 링크:

## L13 학습 루프와 지표 기록

완료 조건: zero_grad·backward·step의 순서와 역할을 설명하고 학습 지표를 기록한다.

- [ ] 학습 루프에서 gradient 초기화·계산·업데이트를 확인한다.
- [ ] 장치·batch·epoch·seed와 optimizer 설정을 남긴다.
- [ ] epoch별 학습·검증 지표를 저장한다.

증빙 경로 또는 링크:

## L14 검증 저장과 별도 추론

완료 조건: 검증 모드와 gradient 비활성화를 구분하고 확정 모델 저장·추론을 재현한다.

- [ ] 곡선과 오분류 사례 5개를 분석한다.
- [ ] state_dict 저장·재로드를 별도 실행에서 비교한다.
- [ ] 확정 모델의 공식 test 평가와 한계를 기록한다.

증빙 경로 또는 링크:

## L15 Attention shape와 causal mask

완료 조건: 작은 Q K V의 행렬곱·scaling·softmax·causal mask를 설명하고 출력 차이를 확인한다.

- [ ] Q K V와 점수·가중치·출력 shape를 기록한다.
- [ ] softmax 축과 causal mask를 작은 입력에서 확인한다.
- [ ] 미래 토큰 정보 차단과 다음 토큰 예측을 연결해 설명한다.

증빙 경로 또는 링크:

## 주간 회고

- 완료한 ID:
- 미완료 조건과 원인:
- 다음 확인 또는 보충:

[주간 보고서](../templates/WEEKLY_REPORT.md)에 실제 시간을 남기고 교육자와 상태를 확인합니다.
