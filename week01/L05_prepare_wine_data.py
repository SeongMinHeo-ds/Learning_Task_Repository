import os
import pandas as pd
from sklearn.datasets import load_wine

# 1. Wine 데이터 확보
wine = load_wine(as_frame=True)
df = wine.frame.copy()

# 2. target -> class_id 이름 변경 및 row_id (1~178) 맨 앞 추가
df = df.rename(columns={"target": "class_id"})
df.insert(0, "row_id", range(1, len(df) + 1))

# 3. data/wine.csv 저장 (index 열 제외)
os.makedirs("../data", exist_ok=True)
output_path = "../data/wine.csv"
df.to_csv(output_path, index=False)

# 4. 기본 점검 정보 추출
info_df = pd.DataFrame({
    "column": df.columns,
    "dtype": [str(t) for t in df.dtypes],
    "missing_count": [int(c) for c in df.isnull().sum()]
})

loc_first = df.loc[0, ["row_id", "alcohol", "class_id"]].to_dict()
iloc_first = df.iloc[0, [0, 1, -1]].to_dict()

# 5. 데이터 출처 및 기본 점검 기록 저장 (week01/L05_data_inspection.md)
md_lines = [
    "# L05 Wine 데이터 출처 및 기본 점검 기록",
    "",
    "## 1. 데이터 출처 및 규칙 적용",
    "- **출처**: `sklearn.datasets.load_wine(as_frame=True)` (UCI Wine Dataset 기반)",
    "- **저장 경로**: `data/wine.csv` (pandas index 열 제외)",
    f"- **전체 규격**: {df.shape[0]}행 × {df.shape[1]}열 (`row_id` 1열 + feature 13열 + `class_id` 1열)",
    "- **라벨 규칙**: 기존 `target`을 `class_id` (0, 1, 2)로 변경, 맨 앞에 `row_id` (1~178) 추가",
    "",
    "## 2. 열 이름·자료형·결측치 점검 (전 열 결측 0개)",
    "| 열 이름 (Column) | 자료형 (dtype) | 결측치 수 (Missing) |",
    "|---|---|---|",
]
for _, r in info_df.iterrows():
    md_lines.append(f"| `{r['column']}` | `{r['dtype']}` | {r['missing_count']} |")

md_lines.extend([
    "",
    "## 3. 첫 행 선택 검증 (`loc` vs `iloc`)",
    f"- **`df.loc[0]` (라벨 기반 첫 행 주요 열)**: `{loc_first}`",
    f"- **`df.iloc[0]` (정수 위치 기반 첫 행 주요 열)**: `{iloc_first}`",
])

with open("L05_data_inspection.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines) + "\n")

print(f">> [완료] {output_path} ({df.shape[0]}행) 및 week01/L05_data_inspection.md 생성 완료")