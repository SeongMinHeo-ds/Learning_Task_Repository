# 1주차 완료 체크리스트

[상세 가이드](README.md)의 각 일차를 완료한 뒤 실제 증빙을 연결한다.

## L01 작업 위치·환경·실행 확인

- [x] environment.md: 편집기와 터미널이 같은 Python을 사용하는지 경로를 대조한다.
- [x] basics.py와 실행 기록: 합계 6, 선택 결과 [2,3]인지 예상과 비교한다.
- [x] run_week01.sh와 셸 실행 기록: cd로 위치를 바꾼 뒤 상대 경로가 왜 달라지는지 설명한다.

증빙 경로·링크:
- 실행 스크립트: week01/L01_env_basic.py, week01/run_L01.sh
- 환경 기록: week01/environment.md
- 검증 결과: Python 3.12.10 경로 확인, 합계 6 및 [2, 3] 필터 검증 완료

## L02 자료형·자료구조·참조와 복사

- [x] python_types.md: None과 0, 문자열 '3'과 숫자 3을 구분한다.
- [x] 자료구조 비교표와 작은 실행 코드: 순서대로 여러 값을 다루는 경우, 이름으로 조회하는 경우, 중복을 없애는 경우의 선택 이유를 각각 쓴다.
- [x] 참조·복사 전후 값과 설명: a와 b는 바뀌고 c는 바깥 list 기준으로 분리된다. tuple 안의 list도 변경될 수 있음을 확인한다.

증빙 경로·링크:
- 실행 스크립트: week01/L02_data_structures.py
- 산출물: week01/python_types.md (기본형/컨테이너 비교표, 참조·복사 및 hashable 검증)

## L03 함수·파일·JSON·실행 인자

- [x] functions_io.md: print와 return을 구분하고 함수 이름만으로 역할을 설명할 수 있게 한다.
- [x] src/wine_cli.py의 실행 골격: 다른 입력 경로와 출력 폴더를 전달할 수 있어야 한다.
- [x] error_cases.csv: 기대 결과·실제 메시지·실행 성공 여부를 구분한다. 이 단계는 최종 필터 구현 후 다시 확인한다.

증빙 경로·링크:
- 실행 코드: src/wine_cli.py
- 산출물: week01/functions_io.md, week01/error_cases.csv
- 검증 내용: read_data/filter_rows/summarize/save_outputs 분리 및 3종 오류 케이스 처리 확인

## L04 NumPy 결과를 손계산과 대조

- [ ] numpy_results.json: 원소 수는 6으로 유지된다. mask 결과의 순서도 기록한다.
- [ ] 연산별 입력·shape·결과 표: 축별 합 [5,7,9]와 [6,15], 전체 합 21을 대조하고 원소별 곱과 행렬곱의 출력 shape를 구분한다.
- [ ] numpy_notes.md: view가 원본을 공유하는 경우와 독립 copy를 실제 값으로 설명한다.

증빙 경로·링크:

## L05 Wine 필터·집계·결과 검증

- [ ] 데이터 출처와 기본 점검 기록: 178행·13 feature인지 확인한다. 결측이 없어도 열별 0개를 기록한다.
- [ ] wine_summary.json, wine_filtered.csv, wine_group_summary.csv: 13.0 조건은 92행이다. 모든 결과 행의 alcohol이 조건을 만족하고 row_id가 원본과 대응해야 한다.
- [ ] validation_results.csv와 실행 README: 100.0은 정상적인 0행 결과다. 입력 행 수=선택 행 수+제외 행 수가 맞아야 한다.

증빙 경로·링크:
