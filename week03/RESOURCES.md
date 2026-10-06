# 3주차 참고 자료

과제를 읽고 현재 작업에 필요한 자료부터 찾아보세요. 공식 예제는 참고할 수 있지만 과제의 입력·출력·설정에 맞추어 직접 구현하고 변경 내용을 설명합니다.

| 자료 | 찾아볼 내용 | 읽을 시점 |
| --- | --- | --- |
| [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | tensor·DataLoader·autograd 흐름 | 먼저 |
| [모델 구성](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html) | MLP·forward·shape | 먼저 |
| [학습 루프](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) | loss·gradient·optimizer와 검증 | 먼저 |
| [모델 저장과 추론](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html) | state_dict·재로드·eval | 필요할 때 |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | scaled dot-product·multi-head·mask의 개요 | 필요할 때 |

## 확인 질문

- L11: 어떤 값에 gradient가 생기고 배치의 각 차원은 무엇을 뜻하나요?
- L12: logits와 예측 클래스는 어떻게 다른가요?
- L13: gradient를 초기화하지 않으면 어떤 결과가 생기나요?
- L14: eval 모드와 gradient 계산 비활성화는 같은 기능인가요?
- L15: mask를 적용하면 어느 연결과 정보가 사라지나요?

자료 확인일: 2026-10-06. 문서의 버전과 실제 사용한 버전이 다를 수 있으므로 실행 환경과 모델 revision을 남깁니다.
