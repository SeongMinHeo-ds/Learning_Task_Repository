# 5주차 참고 자료

과제를 읽고 현재 작업에 필요한 자료부터 찾아보세요. 공식 예제는 참고할 수 있지만 과제의 입력·출력·설정에 맞추어 직접 구현하고 변경 내용을 설명합니다.

| 자료 | 찾아볼 내용 | 읽을 시점 |
| --- | --- | --- |
| [Sentence Transformers 유사도](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html) | encode·정규화·cosine 유사도 | 먼저 |
| [임베딩 모델 카드](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) | 입력 제한·차원과 모델 사용 조건 | 먼저 |
| [scikit-learn 텍스트 특성](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) | TF-IDF baseline | 필요할 때 |
| [NumPy 입문](https://numpy.org/doc/stable/user/absolute_beginners.html) | 벡터·행렬·axis 연산 복습 | 필요할 때 |
| [RAG 원논문](https://arxiv.org/abs/2005.11401) | retriever와 generator 역할의 개요 | 선택 |

## 확인 질문

- L21: 정답 근거가 없는 질문을 데이터셋에서 어떻게 표시했나요?
- L22: 검색한 chunk가 원문의 어느 부분인지 어떻게 찾나요?
- L23: 질문과 문서에 다른 임베딩 모델을 쓰면 무엇이 달라지나요?
- L24: 표현을 바꿨을 때 검색 결과가 달라진 이유를 어떻게 확인하나요?
- L25: chunk 설정을 바꾸었는데도 같은 정답 문서 기준으로 평가할 수 있나요?

자료 확인일: 2026-10-06. 문서의 버전과 실제 사용한 버전이 다를 수 있으므로 실행 환경과 모델 revision을 남깁니다.
