# 1주차 Python·NumPy·pandas와 Wine 처리

**목표:** Wine 178행을 읽어 조건에 맞는 CSV와 요약 JSON을 저장하고 자료형·함수·배열·표 선택을 설명한다.

수행 방식: **실제 Python 프로그램 작성**. 주 5일·하루 6시간, 총 30시간이다. 아래 순서와 기준 설정으로 먼저 완료하고 확장은 그다음에 한다.

[입력 자료](DATA.md) · [참고 링크](RESOURCES.md) · [완료 체크](CHECKLIST.md)

## 1. 시작 전 준비와 기준 설정

1. Python 3.12 계열, CPU, numpy·pandas·scikit-learn. 설치 대상은 이름만 제시하며 설치 방법은 환경에 맞게 확인한다.
2. 입력은 sklearn.datasets.load_wine(as_frame=True)의 전체 데이터다. target을 class_id로 바꾸고 row_id=1~178을 앞에 추가한다. class_id는 0·1·2이며 UCI 원래 라벨 1·2·3과 구분한다.
3. 입력 data/wine.csv, 결과 outputs/week01/. 기준 조건 alcohol >= 13.0. 변경 조건 14.0, 0행 조건 100.0. 원본 파일은 수정하지 않는다.
4. 공통 배열 A=[[1,2,3],[4,5,6]], broadcasting 벡터 b=[10,20,30]. 행 순서는 원본을 유지하고 CSV에는 pandas index를 별도 저장하지 않는다.

저장소 루트에 src/, data/, outputs/week01/를 준비한다. 아래 명령의 src 파일은 직접 작성할 프로그램이며 미리 완성된 코드가 아니다. DATA.md의 링크와 라이브러리 이름으로 환경을 준비한다. 데이터·가중치·가상환경을 Git에 추가하지 않는다.

## 2. 기준 실행 흐름

```text
python src/wine_cli.py --input data/wine.csv --column alcohol --threshold 13.0 --output-dir outputs/week01
```

입력 준비 → 일별 작업 → 결과 파일 생성 → 정상·실패 비교 → 보고서 순서로 진행한다.

## 3. 1일차 · L01 작업 위치·환경·실행 확인

### 1-1. 수행

저장소를 클론하고 루트에서 작업한다. 터미널의 현재 경로와 사용 중인 셸, Python 실행 경로·버전을 확인한다.

- **나와야 할 것:** environment.md
- **확인 방법:** 편집기와 터미널이 같은 Python을 사용하는지 경로를 대조한다.

### 1-2. 수행

작은 파일에서 숫자·문자열을 출력하고, [1,2,3]을 반복해 합계를 구한다. 조건문으로 값이 2 이상인 항목만 고른다.

- **나와야 할 것:** basics.py와 실행 기록
- **확인 방법:** 합계 6, 선택 결과 [2,3]인지 예상과 비교한다.

### 1-3. 수행

현재 위치를 출력하고 작은 Python 파일을 실행하는 run_week01.sh를 만든다. Git Bash에서 bash run_week01.sh로 실행한다.

- **나와야 할 것:** run_week01.sh와 셸 실행 기록
- **확인 방법:** cd로 위치를 바꾼 뒤 상대 경로가 왜 달라지는지 설명한다.

## 4. 2일차 · L02 자료형·자료구조·참조와 복사

### 2-1. 수행

int·float·bool·str·None 각각의 값과 type 결과, 문자열에서 숫자로 바꾸는 예를 기록한다. 변환 불가능한 문자열의 오류도 확인한다.

- **나와야 할 것:** python_types.md
- **확인 방법:** None과 0, 문자열 '3'과 숫자 3을 구분한다.

### 2-2. 수행

list·tuple·dict·set에 같은 주제의 값을 넣어 순서·중복·조회·추가·변경을 비교한다. 인덱싱·슬라이싱·in을 직접 실행한다.

- **나와야 할 것:** 자료구조 비교표와 작은 실행 코드
- **확인 방법:** 순서대로 여러 값을 다루는 경우, 이름으로 조회하는 경우, 중복을 없애는 경우의 선택 이유를 각각 쓴다.

### 2-3. 수행

a=[1,2], b=a, c=a.copy()를 만든 뒤 b에 3을 추가한다. 중첩 list의 얕은 복사도 따로 확인한다. dict 키와 set 원소의 hashable 조건을 확인한다.

- **나와야 할 것:** 참조·복사 전후 값과 설명
- **확인 방법:** a와 b는 바뀌고 c는 바깥 list 기준으로 분리된다. tuple 안의 list도 변경될 수 있음을 확인한다.

## 5. 3일차 · L03 함수·파일·JSON·실행 인자

### 3-1. 수행

read_data, filter_rows, summarize, save_outputs 역할로 함수를 나눈다. 각 함수의 입력·반환값·파일 부작용을 한 줄씩 적는다.

- **나와야 할 것:** functions_io.md
- **확인 방법:** print와 return을 구분하고 함수 이름만으로 역할을 설명할 수 있게 한다.

### 3-2. 수행

CLI는 --input, --column, --threshold, --output-dir 인자를 받게 만든다. 입력 경로를 코드에 고정하지 않는다. 요약 자료를 dict로 만들고 JSON 파일에 저장한다.

- **나와야 할 것:** src/wine_cli.py의 실행 골격
- **확인 방법:** 다른 입력 경로와 출력 폴더를 전달할 수 있어야 한다.

### 3-3. 수행

파일 없음, 존재하지 않는 열, 숫자가 아닌 임계값을 각각 시도한다. 사용자가 원인을 알 수 있는 오류를 기록한다.

- **나와야 할 것:** error_cases.csv
- **확인 방법:** 기대 결과·실제 메시지·실행 성공 여부를 구분한다. 이 단계는 최종 필터 구현 후 다시 확인한다.

## 6. 4일차 · L04 NumPy 결과를 손계산과 대조

### 4-1. 수행

A를 ndarray로 만들고 shape·dtype, 행·열 인덱싱, A>3 mask, reshape(3,2)를 출력한다.

- **나와야 할 것:** numpy_results.json
- **확인 방법:** 원소 수는 6으로 유지된다. mask 결과의 순서도 기록한다.

### 4-2. 수행

axis=0·1의 합과 평균, A+b, A*A, A@A.T를 계산한다. 합계를 Python 반복문으로도 구한다.

- **나와야 할 것:** 연산별 입력·shape·결과 표
- **확인 방법:** 축별 합 [5,7,9]와 [6,15], 전체 합 21을 대조하고 원소별 곱과 행렬곱의 출력 shape를 구분한다.

### 4-3. 수행

작은 배열의 slice와 copy를 각각 바꾸고 원본 변화 여부를 기록한다.

- **나와야 할 것:** numpy_notes.md
- **확인 방법:** view가 원본을 공유하는 경우와 독립 copy를 실제 값으로 설명한다.

## 7. 5일차 · L05 Wine 필터·집계·결과 검증

### 5-1. 수행

Wine을 확보하고 class_id·row_id 규칙대로 data/wine.csv를 만든다. 열 이름·자료형·결측을 확인하고 loc·iloc로 첫 행을 각각 선택한다.

- **나와야 할 것:** 데이터 출처와 기본 점검 기록
- **확인 방법:** 178행·13 feature인지 확인한다. 결측이 없어도 열별 0개를 기록한다.

### 5-2. 수행

src/wine_cli.py에서 alcohol >= threshold인 행을 고르고 summary와 filtered CSV를 저장한다. class_id별 행 수와 alcohol 평균을 groupby로 구한다.

- **나와야 할 것:** wine_summary.json, wine_filtered.csv, wine_group_summary.csv
- **확인 방법:** 13.0 조건은 92행이다. 모든 결과 행의 alcohol이 조건을 만족하고 row_id가 원본과 대응해야 한다.

### 5-3. 수행

13.0·14.0·100.0으로 각각 실행해 전후 행 수를 비교하고 원본 반복문으로 센 개수와 대조한다. 새 터미널에서 기준 실행을 반복한다.

- **나와야 할 것:** validation_results.csv와 실행 README
- **확인 방법:** 100.0은 정상적인 0행 결과다. 입력 행 수=선택 행 수+제외 행 수가 맞아야 한다.

## 8. 제출 파일과 확인 기준

| 파일 | 내용·필드 | 확인 기준 |
| --- | --- | --- |
| environment.md / functions_io.md | Python·셸·함수 인자·반환값 | 경로와 실제 실행 방법을 확인할 수 있음 |
| python_types.md / numpy_results.json / numpy_notes.md | 입력·shape·연산·결과·설명 | 같은 작은 입력을 다시 계산해 대조 가능 |
| wine_summary.json | input_rows, output_rows, excluded_rows, filter, dtypes, missing | 기준 입력 178행, 선택 92행 |
| wine_filtered.csv | row_id, 13 feature, class_id | index 열 없이 92행, row_id 순서 유지 |
| wine_group_summary.csv | class_id, rows, mean_alcohol | 그룹 rows의 합이 178 |
| validation_results.csv / error_cases.csv | case, expected, actual, evidence | 조건 변경·0행·잘못된 입력을 각각 기록 |

## 9. 주간 완료와 막혔을 때

조건을 바꾸어 CSV·JSON을 다시 만들고, 선택된 한 행과 축별 합·평균을 본인이 설명한다.

각 L 번호마다 코드 또는 웹 관찰, 실제 결과 파일, 짧은 설명을 연결한다. 결과 숫자가 다르면 입력 파일·분할 index·버전·설정부터 대조한다. 오류가 나면 입력, 기대 결과, 실제 메시지, 시도한 내용을 기록한다. 미실행·미측정·미채점은 그대로 표시한다.

[주간 보고서 양식](../templates/WEEKLY_REPORT.md)에 실제 시간·증빙·참고 자료와 AI 사용 범위를 적는다. 웹 실험은 브라우저에서 계산한 값과 시뮬레이션 응답을 구분한다.
