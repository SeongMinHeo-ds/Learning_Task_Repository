# 1주차 Python 자료형과 NumPy pandas 기초

이번 주 실습은 **Wine 데이터 처리 CLI와 기초 연산 노트**입니다. 대응 ID는 L01~L05, 계획시간은 30시간입니다.

[참고 자료](RESOURCES.md) · [데이터와 모델 링크](DATA.md) · [체크리스트](CHECKLIST.md)

## 과제

Wine 데이터를 직접 확보해 원본의 열 의미와 형식을 확인합니다. 자료형과 연산을 작은 입력으로 먼저 확인하고, 데이터를 읽어 요약 JSON과 조건별 CSV를 저장하는 프로그램을 작성합니다.

int, float, bool, str, None과 list, tuple, dict, set을 예제로 비교합니다. 값 변환, 인덱싱, 슬라이싱, membership, 변경 가능성, 같은 객체를 참조하는 변수와 복사, dict 키와 set 원소의 조건을 확인합니다. tuple과 set도 전체 자료구조 중 하나로 다룹니다.

함수의 인자와 반환값, 조건·반복, import와 실행 시작점, 파일·JSON, 예외 처리를 사용합니다. 자신의 함수와 라이브러리 객체의 역할을 설명하고 경로를 인자로 받는 실행 기능을 만듭니다. Bash에서 실행하는 작은 스크립트도 직접 작성합니다.

NumPy로 배열을 만들고 shape, dtype, axis, 인덱싱, boolean mask, reshape, broadcasting, 벡터화와 행렬곱을 확인합니다. 작은 배열의 합과 평균을 Python 반복문 결과와 비교하고 copy와 view의 차이를 확인합니다.

pandas의 Series와 DataFrame, CSV 입출력, loc와 iloc, 조건 선택, 정렬, 결측과 자료형, groupby를 사용합니다. 숫자 열과 임계값을 실행 인자로 받아 임계값 이상인 행을 저장하고, 필터 전후 행 수와 자료형·결측 요약을 JSON으로 남깁니다.

## 일별 작업과 결과

| 일차 | ID | 작업 | 산출물 |
| --- | --- | --- | --- |
| 1 | L01 | 환경과 Python 기본 실행 | 환경 기록과 작은 실행 예제 |
| 2 | L02 | Python 자료형과 자료구조 | 자료형 비교와 참조·복사 노트 |
| 3 | L03 | 함수와 모듈 파일 예외 | 함수·파일 처리와 CLI 골격 |
| 4 | L04 | NumPy 배열과 벡터 연산 | shape·axis·broadcasting 검증 노트 |
| 5 | L05 | pandas 기초와 Wine CLI | Wine 요약 JSON과 필터 CSV |

## 제출할 산출물

- 자료형·NumPy 비교 노트
- Wine 처리 코드와 Bash 실행 스크립트
- 요약 JSON과 필터 결과 CSV
- 함수 입출력·환경·오류 기록과 실행 README

## 주간 완료 기준

입력과 필터 조건을 바꿔 실행하고, 함수의 반환값·배열 axis·DataFrame 선택을 설명한다.

**선택 확장:** 성능 벤치마크, 복잡한 클래스 설계와 시각화 확장은 필수 완료 후 수행합니다.

코드 구조와 명령 이름은 직접 정하고 실제 사용 방법을 README에 기록합니다. [주간 보고서](../templates/WEEKLY_REPORT.md)에 실행·설명·검증 증빙을 남기세요. LLM과 RAG 평가는 [공통 평가 기준](../EVALUATION.md)을 사용합니다.
