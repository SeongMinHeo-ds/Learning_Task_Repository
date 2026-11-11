# 5주차 완료 체크리스트

[상세 가이드](README.md)의 각 일차를 완료한 뒤 실제 증빙을 연결한다.

## L21 입력 문서와 개발 질문 확인

- [ ] 문서 목록과 corpus 범위 설명: 작성한 문단과 공식 문서 snapshot을 구분한다.
- [ ] 개발 질문 분류 표: 답 가능 15개와 근거 없음 5개인지 센다.
- [ ] 기준 입력 관찰 기록: 문서·질문 순서와 ID를 바꾸지 않는다.

증빙 경로·링크:

## L22 고정 규칙으로 청킹

- [ ] chunks.jsonl 또는 웹 export의 chunks: 본문이 원문[start:end]와 정확히 같아야 한다.
- [ ] chunk_comparison.csv: 겹치는 문자가 무엇인지 직접 표시하고 0≤overlap<chunk_size를 확인한다.
- [ ] chunk_checks.json: 문자 수를 embedding token 수로 표현하지 않는다. 실제 모델의 token 절단 검사는 이번 범위가 아니다.

증빙 경로·링크:

## L23 교육용 cosine 계산과 top-3

- [ ] cosine_math.json: 점수 [1,0.8,0], 순서 [0,1,2]를 대조한다.
- [ ] vector_search.json: 이 벡터가 어떤 keyword 범주를 세었는지 설명한다.
- [ ] 검색 결과와 근거 확인 기록: 정답 문서를 찾았다는 것과 필요한 근거가 chunk에 있다는 것을 구분한다.

증빙 경로·링크:

## L24 실제 TF-IDF와 벡터 방식 비교

- [ ] retrieval_comparison.csv: 서로 다른 점수 체계의 숫자를 같은 확률로 해석하지 않는다.
- [ ] 표현 변경 사례: 바뀐 질문은 개발셋 기준 지표와 별도의 추가 실험으로 기록한다.
- [ ] 근거 없음 검색 사례: top-3가 존재한다고 문서에 정답이 있다는 뜻은 아니다.

증빙 경로·링크:

## L25 20개 질문 Recall과 설정 저장

- [ ] retrieval_results.json, retrieval_metrics.json: 상위 3개 chunk의 doc_id 중복을 제거하고 정답 문서 집합과 비교한다.
- [ ] 질문별 계산과 집계: 정답 문서 2개 중 1개면 Recall 0.5다. 질문 평균의 분모 15를 기록한다.
- [ ] manifest.json, 추가 실험 보고: corpus ID·청킹·검색 방법·정규화·동점 규칙을 저장한다.

증빙 경로·링크:
