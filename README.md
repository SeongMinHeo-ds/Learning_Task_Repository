# 6주 실습 안내

1 - 3주는 작은 데이터로 Python·ML·DL을 실제 실행합니다. 4~6주는 PC 웹에서 복잡한 LLM·RAG 동작을 관찰하고 JSON·청킹·검색·평가처럼 작은 계산을 직접 실행합니다. LLM 가중치·신경망 embedding·Chroma 설치와 구현은 필수가 아닙니다.

기준은 6주·주 5일·하루 6시간·총 180시간입니다.

| 주차 | 내용 | 수행 방식 | 상세 과제 |
| --- | --- | --- | --- |
| 1주 | Python·NumPy·pandas와 Wine 처리 | 실제 Python 프로그램 작성 | [순서대로 진행](week01/README.md) |
| 2주 | Titanic 전처리·학습·저장과 예측 | 실제 pandas·scikit-learn 실행 | [순서대로 진행](week02/README.md) |
| 3주 | FashionMNIST MLP 학습과 작은 Attention | 실제 PyTorch CPU 학습 | [순서대로 진행](week03/README.md) |
| 4주 | 웹으로 확인하는 LLM 입력·출력 흐름 | PC 웹 데모 + 작은 실제 계산 | [순서대로 진행](week04/README.md) |
| 5주 | 문서 청킹·TF-IDF·벡터 검색 실험 | PC 웹 데모 + 실제 검색·평가 계산 | [순서대로 진행](week05/README.md) |
| 6주 | 웹으로 따라가는 RAG와 인덱스·평가 | PC 웹 데모 + 실제 규칙 기반 검색·저장·집계 | [순서대로 진행](week06/README.md) |

## 진행

각 주차 README의 기준 설정을 먼저 맞추고 일별 수행·산출물·확인 방법을 순서대로 따라갑니다. CHECKLIST.md에서 L01~L30 증빙을 연결합니다. 같은 입력과 조건을 쓰되 환경·라이브러리에 따른 작은 수치 차이는 기록합니다.

4~6주 demo.html은 PC 브라우저에서 열면 작동하는 단일 파일입니다. 모델·API 키·서버·외부 CDN이 필요 없습니다. 실제 계산과 준비 응답 재생이 화면에 구분되어 있습니다.

## 공통 문서

- [30일 일정](CURRICULUM.md)
- [환경](ENVIRONMENT.md) · [라이브러리 이름](LIBRARIES.md)
- [제출 규칙](SUBMISSION.md) · [평가 기준](EVALUATION.md)
- [주간 보고서](templates/WEEKLY_REPORT.md)

외부 데이터·모델을 다운로드할 경우 DATA.md의 링크를 사용합니다. 설치 대상은 라이브러리 이름으로 안내합니다. 원본 데이터·가중치·인덱스 바이너리·환경은 Git에서 제외합니다. 이번 결과는 교육용 소규모 실습이며 모델 서비스 운영이나 실제 LLM 성능 검증까지 완료한 것으로 표시하지 않습니다.
