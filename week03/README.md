# 3주차 딥러닝과 Attention 기본 연산

이번 주 실습은 **FashionMNIST MLP와 작은 Attention 연산**입니다. 대응 ID는 L11~L15, 계획시간은 30시간입니다.

[참고 자료](RESOURCES.md) · [데이터와 모델 링크](DATA.md) · [체크리스트](CHECKLIST.md)

## 과제

FashionMNIST의 작은 부분집합으로 MLP를 구성합니다. NumPy와 tensor의 shape·dtype을 비교하고 한 배치의 입력부터 loss까지 따라갑니다.

학습과 validation을 나누고 epoch별 loss·accuracy를 기록합니다. state_dict를 저장하고 별도 실행에서 재로드하며 설정 확정 후 공식 test를 평가합니다.

작은 tensor의 Q, K, V로 scaled dot-product attention을 확인합니다. softmax 축과 causal mask를 바꾸어 출력 차이를 확인하고 전체 Transformer 학습 대신 연산과 shape를 설명합니다.

## 일별 작업과 결과

| 일차 | ID | 작업 | 산출물 |
| --- | --- | --- | --- |
| 11 | L11 | tensor autograd와 DataLoader | 배치 shape와 gradient 확인 |
| 12 | L12 | MLP forward와 loss | 모델 구조와 loss 입력 표 |
| 13 | L13 | 학습 루프와 지표 기록 | epoch별 loss·accuracy 기록 |
| 14 | L14 | 검증 저장과 별도 추론 | 곡선·오분류·재로드·test 결과 |
| 15 | L15 | Attention shape와 causal mask | Q K V와 mask 전후 출력 노트 |

## 제출할 산출물

- 배치·gradient·forward shape 기록
- 학습·검증 곡선과 오분류 분석
- state_dict 저장·재로드와 확정 모델 test 결과
- 작은 Attention shape·mask 비교 노트

## 주간 완료 기준

학습 루프와 별도 추론을 재현하고 QK 전치 곱과 mask의 shape를 설명한다.

**선택 확장:** CNN, Transformer 전체 구현과 GPU 최적화는 확장 과제입니다.

코드 구조와 명령 이름은 직접 정하고 실제 사용 방법을 README에 기록합니다. [주간 보고서](../templates/WEEKLY_REPORT.md)에 실행·설명·검증 증빙을 남기세요. LLM과 RAG 평가는 [공통 평가 기준](../EVALUATION.md)을 사용합니다.
