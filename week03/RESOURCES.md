# 3주차 참고 자료

공식 예제를 읽고 입력과 출력부터 확인하세요. 예제를 실행했더라도 본인이 사용한 배치, 설정, 저장 방식과 변경 내용을 설명해야 합니다.

## 먼저 볼 자료

| 자료 | 찾아볼 내용 | 연결 목표 |
|---|---|---|
| [Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | 전체 학습 흐름과 tensor 기초 | L11~L15 |
| [Datasets and DataLoaders](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html) | FashionMNIST, 데이터와 배치 | L11 |
| [Build the Neural Network](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html) | 작은 MLP, forward와 shape | L12 |
| [Optimizing Model Parameters](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) | loss, gradient, optimizer와 검증 | L13·L14 |
| [Save and Load the Model](https://docs.pytorch.org/tutorials/beginner/basics/saveloadrun_tutorial.html) | state_dict와 재로드 후 추론 | L15 |

## 읽은 뒤 확인할 질문

- 한 이미지와 한 배치의 shape는 어떻게 다른가요?
- 입력 이미지가 모델의 첫 Linear 층에 들어갈 때 어떤 모양이어야 하나요?
- 모델 출력 logits와 예측 클래스는 어떻게 다른가요?
- gradient를 초기화하지 않으면 어떤 일이 일어나나요?
- eval 모드와 gradient 계산 비활성화는 같은 기능인가요?
- state_dict를 불러올 때 모델 구조와 전처리도 알아야 하는 이유는 무엇인가요?

출처 확인일: 2026-10-06.
