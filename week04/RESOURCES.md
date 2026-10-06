# 4주차 참고 자료

과제를 읽고 현재 작업에 필요한 자료부터 찾아보세요. 공식 예제는 참고할 수 있지만 과제의 입력·출력·설정에 맞추어 직접 구현하고 변경 내용을 설명합니다.

| 자료 | 찾아볼 내용 | 읽을 시점 |
| --- | --- | --- |
| [LLM 추론](https://huggingface.co/docs/transformers/main/en/llm_tutorial) | tokenizer·모델 로드·generate와 입력 길이 | 먼저 |
| [Chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating) | role·template·생성 시작점 | 먼저 |
| [텍스트 생성 설정](https://huggingface.co/docs/transformers/main/en/generation_strategies) | 생성 길이·sampling·일관된 비교 조건 | 필요할 때 |
| [Qwen3 모델 카드](https://huggingface.co/Qwen/Qwen3-0.6B) | 지원 환경·thinking 모드·실제 추론 조건 | 필요할 때 |

## 확인 질문

- L16: 문자 수와 token 수가 다르면 context 제한을 어떻게 확인하나요?
- L17: 모델 로드 시간과 질문 한 건의 생성 시간을 어떻게 구분했나요?
- L18: 답변 변화가 어떤 설정 때문인지 비교표에서 보여주세요.
- L19: 입력이 너무 길거나 모델 출력 형식이 틀리면 사용자에게 무엇이 보이나요?
- L20: 그럴듯한 답변과 문서로 확인한 답변은 어떻게 구분하나요?

자료 확인일: 2026-10-06. 문서의 버전과 실제 사용한 버전이 다를 수 있으므로 실행 환경과 모델 revision을 남깁니다.
