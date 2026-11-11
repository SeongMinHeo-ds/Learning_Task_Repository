"""
L02: Python 자료형·자료구조·참조와 복사
- 기본 자료형(int, float, bool, str, None), type, 형변환, 변환 오류
- list, tuple, dict, set 비교, 인덱싱, 슬라이싱, membership
- 참조(b=a) vs 복사(c=a.copy()), 중첩 list 얕은 복사, tuple 내 list 가변성
- hashable 키/원소 조건 검증
- 산출물: week01/python_types.md 자동 기록
"""
import copy

# ==========================================
# 2-1. 기본 자료형과 형변환, 오류 확인
# ==========================================
print("=== 2-1. 기본 자료형 및 형변환 ===")
v_int = 10
v_float = 3.14
v_bool = True
v_str = "42"
v_none = None

conv_int = int(v_str)
conv_str = str(v_float)
conv_bool_empty = bool("")
conv_bool_zero = bool(0)

# 변환 불가능한 문자열 오류 재현
error_msg = ""
try:
    int("hello_wine")
except ValueError as e:
    error_msg = str(e)

print(f"int: {v_int} ({type(v_int)}), float: {v_float} ({type(v_float)})")
print(f"bool: {v_bool} ({type(v_bool)}), str: {v_str} ({type(v_str)}), None: {v_none} ({type(v_none)})")
print(f"형변환: int('42') -> {conv_int}, str(3.14) -> '{conv_str}', bool('') -> {conv_bool_empty}, bool(0) -> {conv_bool_zero}")
print(f"변환 불가 오류 재현: int('hello_wine') -> ValueError: {error_msg}")
print()

# ==========================================
# 2-2. 4대 컨테이너 (list, tuple, dict, set) 비교
# ==========================================
print("=== 2-2. 자료구조 비교, 인덱싱, 슬라이싱, in 연산 ===")
sample_list = [10, 20, 30, 40]
sample_tuple = (10, 20, 30, 40)
sample_dict = {"alcohol": 13.5, "malic_acid": 2.3, "ash": 2.4}
sample_set = {1, 2, 2, 3, 3, 3}

print(f"list 인덱싱: {sample_list[0]}, 슬라이싱: {sample_list[1:3]}")
print(f"tuple 인덱싱: {sample_tuple[-1]}, 슬라이싱: {sample_tuple[:2]}")
print(f"dict 키 조회: sample_dict['alcohol'] -> {sample_dict['alcohol']}")
print(f"set 중복 제거 결과: {sample_set}")
print(f"membership('in'): 20 in list -> {20 in sample_list}, 'ash' in dict -> {'ash' in sample_dict}, 5 in set -> {5 in sample_set}")
print()

# ==========================================
# 2-3. 참조 vs 복사, tuple 내 list, Hashable 조건
# ==========================================
print("=== 2-3. 참조, 복사, tuple 내 list, Hashable ===")

# 1) a=[1,2], b=a, c=a.copy() 후 b에 3 추가
a = [1, 2]
b = a
c = a.copy()
b.append(3)

print(f"a: {a}")
print(f"b (참조): {b} (a와 동일 객체)")
print(f"c (a.copy): {c} (독립된 복사본)")

# 2) 중첩 list의 얕은 복사
nested_orig = [[1, 2], [3, 4]]
nested_shallow = nested_orig.copy()
nested_deep = copy.deepcopy(nested_orig)

nested_orig[0].append(99)
print(f"중첩 원소 수정 후 원본: {nested_orig}")
print(f"얕은 복사본(영향 받음): {nested_shallow}")
print(f"깊은 복사본(독립): {nested_deep}")

# 3) tuple 안의 list 변경 가능성
tuple_with_list = (1, [10, 20])
tuple_with_list[1].append(30)
print(f"tuple 내부 list 변경 결과: {tuple_with_list}")

# 4) hashable 조건
hash_dict = {}
valid_key = (1, 2)
hash_dict[valid_key] = "성공: 튜플은 immutable이므로 키 가능"

hash_error = ""
try:
    hash_dict[[1, 2]] = "실패해야 정상"
except TypeError as e:
    hash_error = str(e)
print(f"dict 키 TypeError 재현: {hash_error}")
print()

# ==========================================
# 제출 산출물 python_types.md 자동 생성
# ==========================================
markdown_content = f"""# L02 Python 자료형과 자료구조 산출물

## 1. 기본 자료형과 형변환
| 자료형 | 값 예시 | type() 결과 | 설명 |
|---|---|---|---|
| int | `{v_int}` | `{type(v_int)}` | 정수형 |
| float | `{v_float}` | `{type(v_float)}` | 실수형 |
| bool | `{v_bool}` | `{type(v_bool)}` | 논리형 (True/False) |
| str | `'{v_str}'` | `{type(v_str)}` | 문자열 |
| None | `{v_none}` | `{type(v_none)}` | 값의 부재 |

* **형변환 예시**: `int('{v_str}')` -> `{conv_int}`, `str({v_float})` -> `'{conv_str}'`
* **False 판별값**: `bool('')` -> `{conv_bool_empty}`, `bool(0)` -> `{conv_bool_zero}`
* **변환 불가 오류 재현**: `int('hello_wine')` 실행 시 `ValueError: {error_msg}` 발생 확인

## 2. 자료구조 (list, tuple, dict, set) 비교표
| 구분 | list | tuple | dict | set |
|---|---|---|---|---|
| 순서 유지 | O | O | O (Python 3.7+) | X |
| 수정 가능(mutable) | O | X | O | O |
| 중복 허용 | O | O | 키(Key) 불가, 값(Value) 가능 | X |
| 원소 접근 | 정수 인덱싱/슬라이싱 | 정수 인덱싱/슬라이싱 | 키(Key) 조회 | 집합 순회 및 연산 |
| 선택 이유 | 순서대로 여러 값을 담고 수정할 때 | 데이터 변경을 방지하고 보호할 때 | 컬럼명이나 키로 빠르게 조회할 때 | 중복을 제거하거나 집합 비교를 할 때 |

* `sample_list[1:3]` -> `{sample_list[1:3]}`
* `sample_dict['alcohol']` -> `{sample_dict['alcohol']}`
* `sample_set` -> `{sample_set}`

## 3. 참조, 복사, Hashable 검증
1. **참조와 얕은 복사 (`a=[1,2]`, `b=a`, `c=a.copy()`, `b.append(3)`)**
   - `a`: `{a}` (b와 동일 메모리 참조로 변경됨)
   - `b`: `{b}`
   - `c`: `{c}` (독립 복사본으로 유지됨)
2. **중첩 list 복사**
   - 얕은 복사(`copy`): 내부 객체의 참조가 공유되어 내부 변경 시 함께 바뀜 (`{nested_shallow}`)
   - 깊은 복사(`deepcopy`): 내부 객체까지 완전히 새로 복사되어 영향 없음 (`{nested_deep}`)
3. **tuple 내부 list의 가변성**
   - `(1, [10, 20])`에서 튜플 자체는 수정 불가능하지만, 내부 list 원소는 수정 가능하여 `(1, [10, 20, 30])`으로 변경됨
4. **Hashable 조건**
   - `tuple`은 immutable이므로 dict 키 및 set 원소 가능
   - `list`는 mutable하므로 `TypeError: {hash_error}` 발생
"""

with open("python_types.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(">> [완료] week01/python_types.md 산출물 생성 성공")