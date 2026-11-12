# L05 Wine 데이터 출처 및 기본 점검 기록

## 1. 데이터 출처 및 규칙 적용
- **출처**: `sklearn.datasets.load_wine(as_frame=True)` (UCI Wine Dataset 기반)
- **저장 경로**: `data/wine.csv` (pandas index 열 제외)
- **전체 규격**: 178행 × 15열 (`row_id` 1열 + feature 13열 + `class_id` 1열)
- **라벨 규칙**: 기존 `target`을 `class_id` (0, 1, 2)로 변경, 맨 앞에 `row_id` (1~178) 추가

## 2. 열 이름·자료형·결측치 점검 (전 열 결측 0개)
| 열 이름 (Column) | 자료형 (dtype) | 결측치 수 (Missing) |
|---|---|---|
| `row_id` | `int64` | 0 |
| `alcohol` | `float64` | 0 |
| `malic_acid` | `float64` | 0 |
| `ash` | `float64` | 0 |
| `alcalinity_of_ash` | `float64` | 0 |
| `magnesium` | `float64` | 0 |
| `total_phenols` | `float64` | 0 |
| `flavanoids` | `float64` | 0 |
| `nonflavanoid_phenols` | `float64` | 0 |
| `proanthocyanins` | `float64` | 0 |
| `color_intensity` | `float64` | 0 |
| `hue` | `float64` | 0 |
| `od280/od315_of_diluted_wines` | `float64` | 0 |
| `proline` | `float64` | 0 |
| `class_id` | `int64` | 0 |

## 3. 첫 행 선택 검증 (`loc` vs `iloc`)
- **`df.loc[0]` (라벨 기반 첫 행 주요 열)**: `{'row_id': 1.0, 'alcohol': 14.23, 'class_id': 0.0}`
- **`df.iloc[0]` (정수 위치 기반 첫 행 주요 열)**: `{'row_id': 1.0, 'alcohol': 14.23, 'class_id': 0.0}`
