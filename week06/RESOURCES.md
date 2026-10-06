# 6주차 참고 자료

과제를 읽고 현재 작업에 필요한 자료부터 찾아보세요. 공식 예제는 참고할 수 있지만 과제의 입력·출력·설정에 맞추어 직접 구현하고 변경 내용을 설명합니다.

| 자료 | 찾아볼 내용 | 읽을 시점 |
| --- | --- | --- |
| [Chroma 로컬 영속 클라이언트](https://docs.trychroma.com/reference/python/client) | 로컬 저장과 별도 프로세스 재사용 | 먼저 |
| [Chroma 데이터 추가](https://docs.trychroma.com/docs/collections/add-data) | 직접 embedding·ID·문서·metadata 저장 | 먼저 |
| [Chroma 검색](https://docs.trychroma.com/docs/querying-collections/query-and-get) | query embedding·결과·거리 해석 | 먼저 |
| [Chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating) | 질문·context·role과 입력 예산 | 필요할 때 |
| [RAG 원논문](https://arxiv.org/abs/2005.11401) | retrieval과 generation의 관계 | 선택 |

## 확인 질문

- L26: 라이브러리 기본 embedding과 직접 만든 embedding이 섞이지 않았나요?
- L27: 답변의 출처가 모델이 만든 이름이 아니라 실제 문서라는 근거는 무엇인가요?
- L28: 검색 결과가 있다는 이유만으로 항상 답변해도 되나요?
- L29: 검색 실패와 생성 실패를 평가표에서 어떻게 구분했나요?
- L30: 새 환경에서 이 프로젝트를 실행하려면 무엇을 준비해야 하나요?

자료 확인일: 2026-10-06. 문서의 버전과 실제 사용한 버전이 다를 수 있으므로 실행 환경과 모델 revision을 남깁니다.
