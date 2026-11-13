import hashlib
import json
import os
import pandas as pd
from sklearn.model_selection import train_test_split

INPUT_PATH = "../data/titanic.csv"
OUT_DIR = "../outputs/week02"
os.makedirs(OUT_DIR, exist_ok=True)

with open(INPUT_PATH, "rb") as f:
    file_hash = hashlib.sha256(f.read()).hexdigest()

df = pd.read_csv(INPUT_PATH)
assert len(df) == 891, f"기대 행 수 891행과 다릅니다: {len(df)}"

roles_md = f"""# L06 입력 파일 역할 구분 및 데이터 출처 기록

## 1. 실제 사용한 데이터 출처 및 해시 (DATA.md 기준)
- **데이터 출처**: 공개 Titanic CSV 미러 (`https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`)
  - *참고*: Kaggle에서 직접 다운로드하지 않고 동일 스키마의 공개 미러를 사용함
- **저장 경로**: `data/titanic.csv`
- **SHA-256 해시**: `{file_hash}`
- **행·열 규격**: {df.shape[0]}행 × {df.shape[1]}열
- **열 목록**: `{list(df.columns)}`

## 2. Kaggle Titanic 파일별 역할 구분표
| 파일 구분 | 포함 내용 | 본 과제에서의 역할 | 정답(Survived) 사용 여부 |
|---|---|---|---|
| `train.csv` (`data/titanic.csv`) | `Survived`(정답)가 포함된 891행 데이터 | **학습(534)·검증(178)·홀드아웃(179) 분할 및 모델 학습/평가용** | **O (정답 라벨로 사용)** |
| `test.csv` | `Survived` 열이 없는 418행 추론 대상 데이터 | Kaggle 대회 제출용 비라벨 테스트 데이터 | **X (정답으로 절대 사용 안 함)** |
| `gender_submission.csv` (예시 제출) | `PassengerId`와 임의 예측 `Survived` 예시 형식 | 제출 CSV 포맷 확인용 예시 파일 | **X (정답으로 절대 사용 안 함)** |
"""
with open("L06_input_roles.md", "w", encoding="utf-8") as f:
    f.write(roles_md)

train_df, temp_df = train_test_split(
    df, test_size=0.4, random_state=42, stratify=df["Survived"]
)
val_df, holdout_df = train_test_split(
    temp_df, test_size=0.5, random_state=42, stratify=temp_df["Survived"]
)

assert len(train_df) == 534 and len(val_df) == 178 and len(holdout_df) == 179

split_info = {
    "seed": 42,
    "rule": "1st: train_test_split(test_size=0.4, stratify=Survived, random_state=42) -> 2nd: train_test_split(test_size=0.5, stratify=Survived, random_state=42)",
    "total_rows": int(len(df)),
    "train_rows": int(len(train_df)),
    "validation_rows": int(len(val_df)),
    "holdout_rows": int(len(holdout_df)),
    "train_ids": train_df["PassengerId"].tolist(),
    "validation_ids": val_df["PassengerId"].tolist(),
    "holdout_ids": holdout_df["PassengerId"].tolist(),
}
with open(os.path.join(OUT_DIR, "split_info.json"), "w", encoding="utf-8") as f:
    json.dump(split_info, f, indent=2)

dup_count = int(train_df.duplicated().sum())
dup_id_count = int(train_df["PassengerId"].duplicated().sum())

group_summary = (
    train_df.groupby("Pclass", as_index=False)
    .agg(train_rows=("PassengerId", "count"), mean_fare=("Fare", "mean"))
)
group_summary["mean_fare"] = group_summary["mean_fare"].round(4)
group_summary.to_csv(os.path.join(OUT_DIR, "train_group_summary.csv"), index=False)

report_lines = [
    "# L06 Train 데이터 전용 점검 보고서 (data_report.md)",
    "",
    "> **주의**: 데이터 누수 방지를 위해 전체 891행이 아닌 **오직 train 분할 534행만**을 대상으로 산출한 통계입니다.",
    "",
    "## 1. 기본 규격 및 중복 점검 (train 534행 기준)",
    f"- **분석 대상 행 수**: {len(train_df)}행 (전체 891행 중 60%)",
    f"- **전체 행 중복 건수**: {dup_count}건",
    f"- **`PassengerId` 중복 건수**: {dup_id_count}건",
    f"- **타깃(`Survived`) 분포**: 0(사망) = {int((train_df['Survived']==0).sum())}명, 1(생존) = {int((train_df['Survived']==1).sum())}명",
    "",
    "## 2. 열별 자료형(dtype) 및 결측치 현황 (train 534행 기준)",
    "| 열 이름 | 자료형 (dtype) | 결측치 수 (Missing) | 결측 비율 (%) |",
    "|---|---|---|---|",
]
for col in train_df.columns:
    m_cnt = int(train_df[col].isnull().sum())
    m_pct = round(m_cnt / len(train_df) * 100, 2)
    report_lines.append(f"| `{col}` | `{train_df[col].dtype}` | {m_cnt} | {m_pct}% |")

report_lines.extend([
    "",
    "## 3. 모델 사용 Feature 7개 요약 통계 (train 534행 기준)",
    "- **수치형 5개**: `Age`, `Fare`, `SibSp`, `Parch`, `Pclass`",
    "- **범주형 2개**: `Sex`, `Embarked`",
    "- **제외 열**: `PassengerId`(ID), `Survived`(정답), `Name`, `Ticket`, `Cabin`",
    "",
    "## 4. Pclass별 행 수 및 Fare 평균 (`train_group_summary.csv` 요약)",
    "| Pclass | train_rows | mean_fare |",
    "|---|---|---|",
])
for _, r in group_summary.iterrows():
    report_lines.append(f"| {int(r['Pclass'])} | {int(r['train_rows'])} | {r['mean_fare']} |")

with open(os.path.join(OUT_DIR, "data_report.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(report_lines) + "\n")

merged_normal = pd.merge(
    train_df, group_summary, on="Pclass", how="left", validate="many_to_one"
)
assert len(merged_normal) == 534
assert (merged_normal["PassengerId"].values == train_df["PassengerId"].values).all()

small_left = train_df[["PassengerId", "Pclass", "Fare"]].head(5).copy()
dup_right = pd.DataFrame({
    "Pclass": [1, 1, 2, 3],
    "note": ["dup_A", "dup_B", "single_2", "single_3"]
})
merged_exploded = pd.merge(small_left, dup_right, on="Pclass", how="left")

merge_val = {
    "normal_many_to_one_merge": {
        "join_key": "Pclass",
        "how": "left",
        "validate_rule": "many_to_one",
        "rows_before": int(len(train_df)),
        "rows_after": int(len(merged_normal)),
        "passenger_id_preserved": bool((merged_normal["PassengerId"].values == train_df["PassengerId"].values).all()),
        "added_to_model_features": False,
        "note": "연습용 집계 열(train_rows, mean_fare)은 모델 학습 feature에 추가하지 않음"
    },
    "duplicate_right_key_experiment": {
        "description": "오른쪽 테이블에 Pclass=1 키가 2번 중복될 때 1:N 카테시안 곱으로 행 수가 팽창하는 현상 재현",
        "left_rows_before": int(len(small_left)),
        "left_pclass_1_count": int((small_left["Pclass"] == 1).sum()),
        "right_rows_with_dup_key": int(len(dup_right)),
        "rows_after_merge": int(len(merged_exploded)),
        "row_increase": int(len(merged_exploded) - len(small_left)),
    }
}
with open(os.path.join(OUT_DIR, "merge_validation.json"), "w", encoding="utf-8") as f:
    json.dump(merge_val, f, indent=2, ensure_ascii=False)

print(">> [완료] L06 모든 검증 및 산출물 생성 완료")
