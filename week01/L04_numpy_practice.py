"""
L04: NumPy 배열, 벡터 연산, 손계산 대조
- A = [[1, 2, 3], [4, 5, 6]], b = [10, 20, 30]
- 4-1: shape, dtype, 인덱싱, mask (A > 3), reshape(3, 2)
- 4-2: axis=0/1 합·평균, Python 반복문 대조, A+b, A*A, A@A.T
- 4-3: slice (view) vs copy 수정 시 원본 변화 검증
- 산출물: week01/numpy_results.json, week01/numpy_notes.md
"""
import json
import numpy as np

# ==========================================
# 4-1. 배열 생성, 인덱싱, Mask, Reshape
# ==========================================
A = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

shape_A = list(A.shape)          # [2, 3]
dtype_A = str(A.dtype)           # 'int32'
elem_0_1 = int(A[0, 1])          # 2 (0행 1열)
row_1 = A[1, :].tolist()         # [4, 5, 6] (1행 전체)
col_2 = A[:, 2].tolist()         # [3, 6] (2열 전체)

# boolean mask (A > 3)
mask = A > 3
mask_selected = A[mask].tolist() # [4, 5, 6]

# reshape(3, 2)
A_reshaped = A.reshape(3, 2).tolist()

# ==========================================
# 4-2. 집계, 손계산 대조, 벡터/행렬 연산
# ==========================================
sum_axis0 = A.sum(axis=0).tolist()     # [5, 7, 9] (열 방향 합)
sum_axis1 = A.sum(axis=1).tolist()     # [6, 15]   (행 방향 합)
mean_axis0 = A.mean(axis=0).tolist()   # [2.5, 3.5, 4.5]
mean_axis1 = A.mean(axis=1).tolist()   # [2.0, 5.0]
total_sum_np = int(A.sum())            # 21

# Python 반복문 기반 손계산 대조
py_sum_axis0 = [0, 0, 0]
py_sum_axis1 = [0, 0]
py_total_sum = 0

for i in range(len(A)):
    row_sum = 0
    for j in range(len(A[i])):
        val = int(A[i, j])
        py_sum_axis0[j] += val
        row_sum += val
        py_total_sum += val
    py_sum_axis1[i] = row_sum

# Broadcasting & Matrix Multiplication
b = np.array([10, 20, 30], dtype=np.int32)
A_add_b = (A + b).tolist()             # [[11, 22, 33], [14, 25, 36]], shape (2, 3)
elem_mult = (A * A).tolist()           # 원소별 곱 [[1, 4, 9], [16, 25, 36]], shape (2, 3)
matmul_res = (A @ A.T).tolist()        # 행렬곱 [[14, 32], [32, 77]], shape (2, 2)

# ==========================================
# 4-3. View(Slice) vs Copy 원본 변화 검증
# ==========================================
orig_for_slice = np.array([[1, 2, 3], [4, 5, 6]])
slice_view = orig_for_slice[0, :]
slice_view[0] = 99
orig_after_slice_modified = orig_for_slice.tolist()  # [[99, 2, 3], [4, 5, 6]]

orig_for_copy = np.array([[1, 2, 3], [4, 5, 6]])
copy_arr = orig_for_copy.copy()
copy_arr[0, 0] = 99
orig_after_copy_modified = orig_for_copy.tolist()    # [[1, 2, 3], [4, 5, 6]]

# ==========================================
# 산출물 1: week01/numpy_results.json 저장
# ==========================================
results_data = {
    "array_A": {
        "shape": shape_A,
        "dtype": dtype_A,
        "total_elements": int(A.size),
        "indexing": {
            "A[0, 1]": elem_0_1,
            "row_1": row_1,
            "col_2": col_2,
        },
        "mask_gt_3": {
            "mask_order": [bool(x) for x in mask.flatten()],
            "selected_values": mask_selected,
        },
        "reshape_3x2": A_reshaped,
    },
    "operations": {
        "sum_axis0": sum_axis0,
        "sum_axis1": sum_axis1,
        "mean_axis0": mean_axis0,
        "mean_axis1": mean_axis1,
        "total_sum": total_sum_np,
        "broadcasting_A_plus_b": {
            "input_b": b.tolist(),
            "output_shape": list((A + b).shape),
            "result": A_add_b,
        },
        "elementwise_multiplication_A_x_A": {
            "output_shape": [2, 3],
            "result": elem_mult,
        },
        "matrix_multiplication_A_matmul_A_T": {
            "output_shape": [2, 2],
            "result": matmul_res,
        },
    },
    "view_vs_copy": {
        "original_after_slice_view_mutation": orig_after_slice_modified,
        "original_after_copy_mutation": orig_after_copy_modified,
    },
}

with open("numpy_results.json", "w", encoding="utf-8") as f:
    json.dump(results_data, f, indent=2)

# ==========================================
# 산출물 2: week01/numpy_notes.md 저장
# ==========================================
markdown_notes = f"""# L04 NumPy 연산 손계산 대조 및 메모리 검증 노트 (numpy_notes.md)

## 1. 기본 규격 및 Shape
- **배열 A**: shape `(2, 3)`, dtype `int32`
- **원소 개수 보존**: `2 * 3 = 6`개 원소가 `reshape(3, 2)` 후에도 총 6개 유지
- **A > 3 불리언 마스크**: `{mask_selected}` (순서: 1행부터 스캔되어 4, 5, 6 추출)

## 2. 연산별 입력·Shape·손계산 대조표
| 연산 | 수식 / 표현식 | 입력 Shape | 출력 Shape | 결과 | 손계산 및 Python 반복문 대조 |
|---|---|---|---|---|---|
| 축 0 합 | `A.sum(axis=0)` | `(2, 3)` | `(3,)` | `{sum_axis0}` | `[1+4, 2+5, 3+6] = [5, 7, 9]` (일치) |
| 축 1 합 | `A.sum(axis=1)` | `(2, 3)` | `(2,)` | `{sum_axis1}` | `[1+2+3, 4+5+6] = [6, 15]` (일치) |
| 전체 합 | `A.sum()` | `(2, 3)` | scalar | `{total_sum_np}` | 반복문 합 `{py_total_sum}`과 일치 |
| 축 0 평균 | `A.mean(axis=0)` | `(2, 3)` | `(3,)` | `{mean_axis0}` | `[5/2, 7/2, 9/2] = [2.5, 3.5, 4.5]` |
| 축 1 평균 | `A.mean(axis=1)` | `(2, 3)` | `(2,)` | `{mean_axis1}` | `[6/3, 15/3] = [2.0, 5.0]` |
| 브로드캐스팅 | `A + b` | `(2, 3) + (3,)` | `(2, 3)` | `{A_add_b}` | `b`가 각 행에 확장 더해짐 |
| 원소별 곱 | `A * A` | `(2, 3) * (2, 3)` | `(2, 3)` | `{elem_mult}` | 위치별 단순 제곱 |
| 행렬곱 | `A @ A.T` | `(2, 3) @ (3, 2)` | `(2, 2)` | `{matmul_res}` | 행벡터와 열벡터의 내적 계산 |

## 3. View(Slice) vs Copy 동작 차이
1. **Slice (View)**
   - `slice_view = A[0, :]` 후 `slice_view[0] = 99` 변경 시
   - 원본 배열 `orig_for_slice[0, 0]`도 `99`로 **함께 변경됨** (`{orig_after_slice_modified}`)
   - 이유: 슬라이싱은 새로운 메모리를 할당하지 않고 원본의 메모리 주소를 참조하는 view를 반환하기 때문
2. **Copy (독립 복사)**
   - `copy_arr = A.copy()` 후 `copy_arr[0, 0] = 99` 변경 시
   - 원본 배열은 `{orig_after_copy_modified}`로 **변경되지 않고 보존됨**
   - 이유: `copy()`는 독립적인 연속 메모리 블록을 새로 할당하여 데이터를 복제하기 때문
"""

with open("numpy_notes.md", "w", encoding="utf-8") as f:
    f.write(markdown_notes)

print(">> [완료] L04 연산 검증 및 산출물 2종 생성 완료:")
print("   - week01/numpy_results.json")
print("   - week01/numpy_notes.md")