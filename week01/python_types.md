# L02 Python 자료형과 자료구조 산출물

## 1. 기본 자료형과 형변환
| 자료형 | 값 예시 | type() 결과 | 설명 |
|---|---|---|---|
| int | `10` | `<class 'int'>` | 정수형 |
| float | `3.14` | `<class 'float'>` | 실수형 |
| bool | `True` | `<class 'bool'>` | 논리형 (True/False) |
| str | `'42'` | `<class 'str'>` | 문자열 |
| None | `None` | `<class 'NoneType'>` | 값의 부재 |

* **형변환 예시**: `int('42')` -> `42`, `str(3.14)` -> `'3.14'`
* **False 판별값**: `bool('')` -> `False`, `bool(0)` -> `False`
* **변환 불가 오류 재현**: `int('hello_wine')` 실행 시 `ValueError: invalid literal for int() with base 10: 'hello_wine'` 발생 확인

## 2. 자료구조 (list, tuple, dict, set) 비교표
| 구분 | list | tuple | dict | set |
|---|---|---|---|---|
| 순서 유지 | O | O | O (Python 3.7+) | X |
| 수정 가능(mutable) | O | X | O | O |
| 중복 허용 | O | O | 키(Key) 불가, 값(Value) 가능 | X |
| 원소 접근 | 정수 인덱싱/슬라이싱 | 정수 인덱싱/슬라이싱 | 키(Key) 조회 | 집합 순회 및 연산 |
| 선택 이유 | 순서대로 여러 값을 담고 수정할 때 | 데이터 변경을 방지하고 보호할 때 | 컬럼명이나 키로 빠르게 조회할 때 | 중복을 제거하거나 집합 비교를 할 때 |

* `sample_list[1:3]` -> `[20, 30]`
* `sample_dict['alcohol']` -> `13.5`
* `sample_set` -> `{1, 2, 3}`

## 3. 참조, 복사, Hashable 검증
1. **참조와 얕은 복사 (`a=[1,2]`, `b=a`, `c=a.copy()`, `b.append(3)`)**
   - `a`: `[1, 2, 3]` (b와 동일 메모리 참조로 변경됨)
   - `b`: `[1, 2, 3]`
   - `c`: `[1, 2]` (독립 복사본으로 유지됨)
2. **중첩 list 복사**
   - 얕은 복사(`copy`): 내부 객체의 참조가 공유되어 내부 변경 시 함께 바뀜 (`[[1, 2, 99], [3, 4]]`)
   - 깊은 복사(`deepcopy`): 내부 객체까지 완전히 새로 복사되어 영향 없음 (`[[1, 2], [3, 4]]`)
3. **tuple 내부 list의 가변성**
   - `(1, [10, 20])`에서 튜플 자체는 수정 불가능하지만, 내부 list 원소는 수정 가능하여 `(1, [10, 20, 30])`으로 변경됨
4. **Hashable 조건**
   - `tuple`은 immutable이므로 dict 키 및 set 원소 가능
   - `list`는 mutable하므로 `TypeError: unhashable type: 'list'` 발생
