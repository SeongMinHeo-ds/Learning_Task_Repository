# 3주차 FashionMNIST MLP 학습과 작은 Attention

**목표:** 작은 MLP의 forward·loss·gradient·학습·검증·저장·재로드를 실행하고 Attention의 축과 causal mask를 설명한다.

수행 방식: **실제 PyTorch CPU 학습**. 주 5일·하루 6시간, 총 30시간이다. 아래 순서와 기준 설정으로 먼저 완료하고 확장은 그다음에 한다.

[입력 자료](DATA.md) · [참고 링크](RESOURCES.md) · [완료 체크](CHECKLIST.md)

## 1. 시작 전 준비와 기준 설정

1. FashionMNIST 공식 train 60000행에서 train_test_split(np.arange(60000), train_size=2000, test_size=500, stratify=train_labels, random_state=42)로 train 2000·validation 500개를 선택한다.
2. 공식 test 10000개에서는 np.random.default_rng(42).choice(10000, size=1000, replace=False)로 고정 1000개만 평가한다. 선택 index를 모두 기록하며 전체 test 성능으로 표현하지 않는다.
3. 이미지는 float32/255, label은 int64. 모델 Flatten→Linear(784,64)→ReLU→Linear(64,10), CrossEntropyLoss, Adam(lr=0.003), batch=128, epoch=5, CPU threads=2, torch seed=42, shuffle generator seed=42.
4. validation loss가 가장 작은 epoch의 state_dict를 보관하고 설정 확정 후 공식 test 일부를 한 번 평가한다. test로 epoch를 고르지 않는다.
5. Attention은 Q=K=[[1,0],[0,1],[1,1]], V=[[1,2],[3,4],[10,20]], scale=sqrt(2), softmax는 마지막 축으로 비교한다.

저장소 루트에 src/, data/, outputs/week03/를 준비한다. 아래 명령의 src 파일은 직접 작성할 프로그램이며 미리 완성된 코드가 아니다. DATA.md의 링크와 라이브러리 이름으로 환경을 준비한다. 데이터·가중치·가상환경을 Git에 추가하지 않는다.

## 2. 기준 실행 흐름

```text
python src/fashion_mlp.py --train-size 2000 --validation-size 500 --test-size 1000 --epochs 5 --batch-size 128 --seed 42 --output-dir outputs/week03
```

입력 준비 → 일별 작업 → 결과 파일 생성 → 정상·실패 비교 → 보고서 순서로 진행한다.

## 3. 1일차 · L11 데이터·tensor·gradient 확인

### 1-1. 수행

공식 데이터를 확보하고 정해 둔 index를 선택한다. 출처·선택 규칙·seed·index를 저장한다.

- **나와야 할 것:** training_config.json 초안
- **확인 방법:** train·validation index가 겹치지 않고 test는 공식 별도 묶음이다.

### 1-2. 수행

DataLoader에서 배치 하나를 꺼내 이미지·label의 shape·dtype·device를 출력한다. NumPy 변환 전후도 확인한다.

- **나와야 할 것:** tensor_shapes_and_gradient.json
- **확인 방법:** 이미지는 [128,1,28,28] float32, label은 [128] int64다.

### 1-3. 수행

x=[2,3]에 requires_grad를 주고 sum(x*x)를 미분한다.

- **나와야 할 것:** 작은 gradient 결과
- **확인 방법:** gradient [4,6]과 requires_grad의 역할을 설명한다.

## 4. 2일차 · L12 MLP forward와 loss

### 2-1. 수행

고정한 모델을 구성하고 배치 하나가 각 층을 통과할 때 shape를 기록한다.

- **나와야 할 것:** 층별 입력·출력 표
- **확인 방법:** [128,784]→[128,64]→[128,10] 흐름을 확인한다.

### 2-2. 수행

마지막 출력 logits와 argmax 예측을 구분하고 CrossEntropyLoss에 logits와 label을 넣는다.

- **나와야 할 것:** loss·logits·정답 조건 기록
- **확인 방법:** loss 전에 softmax를 중복 적용하지 않는다. label dtype과 범위를 확인한다.

### 2-3. 수행

잘못된 label shape·dtype을 작은 예에서 확인하고 올바른 입력과 비교한다.

- **나와야 할 것:** 오류 관찰 기록
- **확인 방법:** 어느 조건이 loss 입력과 맞지 않는지 설명한다.

## 5. 3일차 · L13 학습 루프와 5 epoch 기록

### 3-1. 수행

각 batch에서 zero_grad→forward→loss→backward→step을 실행한다.

- **나와야 할 것:** 학습 루프와 역할 설명
- **확인 방법:** 업데이트 전후 파라미터가 실제로 달라지는지 작은 배치로 확인한다.

### 3-2. 수행

각 epoch에서 train loss·accuracy와 validation loss·accuracy를 구한다. validation은 eval 모드와 gradient 비활성화를 사용한다.

- **나와야 할 것:** training_history.csv
- **확인 방법:** 정확히 5행이며 loss는 샘플 수로 가중 평균한다.

### 3-3. 수행

validation loss가 가장 낮은 모델 파라미터를 복사해 보관한다. 선택 epoch·설정을 기록한다.

- **나와야 할 것:** 선택 기준과 checkpoint 기록
- **확인 방법:** 마지막 epoch와 best epoch를 무조건 같다고 가정하지 않는다.

## 6. 4일차 · L14 최종 평가·그림·별도 재로드

### 4-1. 수행

학습·검증 곡선을 그리고 실제 오분류 5개에 원본 test index·정답·예측을 표시한다.

- **나와야 할 것:** learning_curves.png, misclassified_examples.png/.json
- **확인 방법:** 그림의 값은 CSV와 같아야 하며 원인을 이미지 하나만으로 단정하지 않는다.

### 4-2. 수행

선택 모델을 고정 test 1000개에서 평가한다.

- **나와야 할 것:** test_result.json
- **확인 방법:** 평가 개수와 선택 규칙을 명시하고 전체 10000개 성능으로 표시하지 않는다.

### 4-3. 수행

state_dict를 저장하고 새 Python 프로세스에서 같은 모델 구조로 로드한다. 고정 입력 5개의 logits와 예측을 비교한다.

- **나와야 할 것:** reload_check.json
- **확인 방법:** logits는 atol=1e-5로 대조하고 최대 오차·예측 일치·별도 프로세스 여부를 기록한다.

## 7. 5일차 · L15 Attention 축과 causal mask

### 5-1. 수행

Q@K.T/sqrt(2)를 계산한 뒤 마지막 축 softmax와 V 곱을 구한다.

- **나와야 할 것:** attention_results.json의 mask 없는 값
- **확인 방법:** 점수 [3,3], 가중치 [3,3], 출력 [3,2]를 확인한다.

### 5-2. 수행

미래 위치 점수를 차단하는 upper triangular causal mask를 적용한다.

- **나와야 할 것:** mask 전후 가중치와 출력
- **확인 방법:** 미래 위치 가중치 합은 0, 각 행의 합은 약 1이다.

### 5-3. 수행

softmax 축을 0으로 바꾸고 결과를 비교한다. 미래 V를 바꿨을 때 앞쪽 출력에 영향이 있는지도 작은 입력으로 확인한다.

- **나와야 할 것:** attention_notes.md
- **확인 방법:** 다음 토큰 예측에서 미래 정보를 막는 이유와 전체 Transformer 구현과의 차이를 설명한다.

## 8. 제출 파일과 확인 기준

| 파일 | 내용·필드 | 확인 기준 |
| --- | --- | --- |
| training_config.json | source·hash·train/validation/test index·seed·모델·optimizer | 2000/500/1000과 5 epoch |
| tensor_shapes_and_gradient.json | 배치·층별 shape·dtype·작은 gradient | gradient [4,6] |
| training_history.csv / learning_curves.png | epoch별 loss·accuracy와 동일 값의 그림 | 5행, train·validation 모두 기록 |
| misclassified_examples.png/.json | 실제 오분류 5개와 원본 index·정답·예측 | 예측과 정답이 실제로 다른 사례 |
| test_result.json / reload_check.json | 부분 test 지표·별도 로드 비교 | 1000개 평가, logits 오차≤허용 범위 |
| attention_results.json / attention_notes.md | Q/K/V·scores·weights·output·mask·설명 | 미래 가중치 0, 행 합 약 1 |

## 9. 주간 완료와 막혔을 때

학습·저장·별도 추론을 재현하고, logits·loss·gradient와 Attention mask의 값을 설명한다.

각 L 번호마다 코드 또는 웹 관찰, 실제 결과 파일, 짧은 설명을 연결한다. 결과 숫자가 다르면 입력 파일·분할 index·버전·설정부터 대조한다. 오류가 나면 입력, 기대 결과, 실제 메시지, 시도한 내용을 기록한다. 미실행·미측정·미채점은 그대로 표시한다.

[주간 보고서 양식](../templates/WEEKLY_REPORT.md)에 실제 시간·증빙·참고 자료와 AI 사용 범위를 적는다. 웹 실험은 브라우저에서 계산한 값과 시뮬레이션 응답을 구분한다.
