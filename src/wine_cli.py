"""
L03: Wine 데이터 처리 CLI 골격
- 실행 인자: --input, --column, --threshold, --output-dir
- 주요 함수 분리: read_data, filter_rows, summarize, save_outputs
- 에러 처리: 파일 없음, 존재하지 않는 열, 숫자가 아닌 임계값
"""
import argparse
import json
import os
import sys
from typing import Any, Dict, List, Tuple


def read_data(filepath: str) -> Tuple[List[str], List[Dict[str, Any]]]:
    """입력 CSV를 읽어 헤더와 행 딕셔너리 목록을 반환합니다.
    입력: filepath (str) / 반환값: (headers, rows) / 부작용: 파일 읽기(I/O)
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"입력 파일을 찾을 수 없습니다: {filepath}")

    with open(filepath, mode="r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        return [], []

    headers = [h.strip() for h in lines[0].split(",")]
    rows: List[Dict[str, Any]] = []

    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        row_dict = {}
        for h, val in zip(headers, values):
            try:
                row_dict[h] = float(val)
            except ValueError:
                row_dict[h] = val
        rows.append(row_dict)

    return headers, rows


def filter_rows(
    rows: List[Dict[str, Any]], column: str, threshold: float
) -> List[Dict[str, Any]]:
    """지정한 열의 값이 threshold 이상인 행만 추출합니다.
    입력: rows, column, threshold / 반환값: filtered_rows / 부작용: 없음 (순수 연산)
    """
    if not rows:
        return []

    if column not in rows[0]:
        raise KeyError(f"지정한 열 '{column}'이(가) 데이터에 존재하지 않습니다.")

    filtered = []
    for r in rows:
        val = r.get(column)
        if isinstance(val, (int, float)) and val >= threshold:
            filtered.append(r)
    return filtered


def summarize(
    total_rows: int,
    filtered_rows: List[Dict[str, Any]],
    column: str,
    threshold: float,
) -> Dict[str, Any]:
    """필터링 전후 행 수 및 조건 메타데이터를 요약 dict로 생성합니다.
    입력: total_rows, filtered_rows, column, threshold / 반환값: summary (dict) / 부작용: 없음
    """
    selected_count = len(filtered_rows)
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
    }


def save_outputs(
    summary_data: Dict[str, Any],
    filtered_rows: List[Dict[str, Any]],
    headers: List[str],
    output_dir: str,
) -> None:
    """요약 JSON 및 필터 결과 CSV를 디렉터리에 저장합니다.
    입력: summary_data, filtered_rows, headers, output_dir / 반환값: None / 부작용: 파일 생성(I/O)
    """
    os.makedirs(output_dir, exist_ok=True)

    json_path = os.path.join(output_dir, "wine_summary.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary_data, f, indent=2, ensure_ascii=False)

    csv_path = os.path.join(output_dir, "wine_filtered.csv")
    with open(csv_path, "w", encoding="utf-8") as f:
        if headers:
            f.write(",".join(headers) + "\n")
            for row in filtered_rows:
                line = ",".join(str(row.get(h, "")) for h in headers)
                f.write(line + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="L03 Wine Data Processing CLI")
    parser.add_argument("--input", required=True, help="입력 CSV 파일 경로")
    parser.add_argument("--column", required=True, help="필터링 기준 열 이름")
    parser.add_argument("--threshold", required=True, help="필터링 기준 임계값(실수형)")
    parser.add_argument("--output-dir", required=True, help="출력 디렉터리 경로")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # 임계값 수치 변환 검증
    try:
        threshold = float(args.threshold)
    except ValueError:
        print(f"[Error] --threshold 인자는 숫자여야 합니다. 입력값: '{args.threshold}'", file=sys.stderr)
        sys.exit(1)

    try:
        headers, rows = read_data(args.input)
        filtered = filter_rows(rows, args.column, threshold)
        summary = summarize(len(rows), filtered, args.column, threshold)
        save_outputs(summary, filtered, headers, args.output_dir)
        print(f">> [성공] 총 {len(rows)}행 중 {len(filtered)}행 선택 완료 -> {args.output_dir}")
    except (FileNotFoundError, KeyError) as e:
        print(f"[Error] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()