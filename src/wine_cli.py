"""
L05: Wine 데이터 처리 CLI 최종본
- 실행 인자: --input, --column, --threshold, --output-dir
- 산출물: wine_summary.json, wine_filtered.csv, wine_group_summary.csv
"""
import argparse
import json
import os
import sys
from typing import Any, Dict
import pandas as pd


def read_data(filepath: str) -> pd.DataFrame:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"입력 파일을 찾을 수 없습니다: {filepath}")
    return pd.read_csv(filepath)


def filter_rows(df: pd.DataFrame, column: str, threshold: float) -> pd.DataFrame:
    if column not in df.columns:
        raise KeyError(f"지정한 열 '{column}'이(가) 데이터에 존재하지 않습니다.")
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise TypeError(f"지정한 열 '{column}'은(는) 숫자형 열이 아닙니다.")
    return df[df[column] >= threshold].copy()


def summarize(
    df: pd.DataFrame, filtered_df: pd.DataFrame, column: str, threshold: float
) -> Dict[str, Any]:
    total_rows = int(len(df))
    selected_count = int(len(filtered_df))
    excluded_count = total_rows - selected_count

    return {
        "input_rows": total_rows,
        "output_rows": selected_count,
        "excluded_rows": excluded_count,
        "filter": {
            "column": column,
            "threshold": threshold,
            "condition": f"{column} >= {threshold}",
        },
        "dtypes": {col: str(dtype) for col, dtype in df.dtypes.items()},
        "missing": {col: int(cnt) for col, cnt in df.isnull().sum().items()},
    }


def make_group_summary(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby("class_id", as_index=False)
        .agg(rows=("row_id", "count"), mean_alcohol=("alcohol", "mean"))
    )
    grouped["mean_alcohol"] = grouped["mean_alcohol"].round(4)
    return grouped


def save_outputs(
    summary_data: Dict[str, Any],
    filtered_df: pd.DataFrame,
    group_df: pd.DataFrame,
    output_dir: str,
) -> None:
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "wine_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)

    filtered_df.to_csv(os.path.join(output_dir, "wine_filtered.csv"), index=False)
    group_df.to_csv(os.path.join(output_dir, "wine_group_summary.csv"), index=False)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="L05 Wine Data Processing CLI")
    parser.add_argument("--input", required=True, help="입력 CSV 파일 경로")
    parser.add_argument("--column", required=True, help="필터링 기준 숫자 열 이름")
    parser.add_argument("--threshold", required=True, help="필터링 기준 임계값(실수형)")
    parser.add_argument("--output-dir", required=True, help="출력 파일 저장 디렉터리")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    try:
        threshold = float(args.threshold)
    except ValueError:
        print(f"[Error] --threshold 인자는 숫자여야 합니다. 입력값: '{args.threshold}'", file=sys.stderr)
        sys.exit(1)

    try:
        df = read_data(args.input)
        filtered_df = filter_rows(df, args.column, threshold)
        summary = summarize(df, filtered_df, args.column, threshold)
        group_df = make_group_summary(df)
        save_outputs(summary, filtered_df, group_df, args.output_dir)
        print(f">> [성공] 총 {len(df)}행 중 {len(filtered_df)}행 선택 완료 -> {args.output_dir}")
    except (FileNotFoundError, KeyError, TypeError) as e:
        print(f"[Error] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()