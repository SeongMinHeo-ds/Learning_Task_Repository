import csv
import json
import subprocess
import sys

INPUT_CSV = "../data/wine.csv"
CLI_SCRIPT = "../src/wine_cli.py"
OUT_DIR = "../outputs/week01"

# 1. 원본 CSV를 순수 Python 반복문으로 직접 세는 함수
def count_with_loop(threshold: float) -> int:
    count = 0
    with open(INPUT_CSV, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if float(row["alcohol"]) >= threshold:
                count += 1
    return count

# 2. 14.0 -> 100.0 -> 13.0 순서로 실행 (마지막 13.0 결과가 outputs/week01에 최종 보존됨)
thresholds = [14.0, 100.0, 13.0]
validation_rows = []

for th in thresholds:
    loop_count = count_with_loop(th)
    cmd = [
        sys.executable, CLI_SCRIPT,
        "--input", INPUT_CSV,
        "--column", "alcohol",
        "--threshold", str(th),
        "--output-dir", OUT_DIR
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)

    with open(f"{OUT_DIR}/wine_summary.json", "r", encoding="utf-8") as jf:
        summary = json.load(jf)

    in_r = summary["input_rows"]
    out_r = summary["output_rows"]
    exc_r = summary["excluded_rows"]

    assert in_r == out_r + exc_r, f"행 수 합계 불일치: {in_r} != {out_r} + {exc_r}"
    assert out_r == loop_count, f"반복문 대조 불일치: CLI={out_r}, Loop={loop_count}"

    validation_rows.append({
        "case": f"alcohol >= {th}",
        "expected": f"loop_count={loop_count}, sum_check={in_r}",
        "actual": f"input={in_r}, output={out_r}, excluded={exc_r}",
        "evidence": res.stdout.strip()
    })

order = {"alcohol >= 13.0": 0, "alcohol >= 14.0": 1, "alcohol >= 100.0": 2}
validation_rows.sort(key=lambda x: order[x["case"]])

with open("validation_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["case", "expected", "actual", "evidence"])
    writer.writeheader()
    writer.writerows(validation_rows)

# 3. 최종 필터 구현 후 오류 케이스 3종 재확인 -> error_cases.csv 갱신
error_tests = [
    ("file_not_found", ["--input", "../data/no_file.csv", "--column", "alcohol", "--threshold", "13.0", "--output-dir", OUT_DIR], "FileNotFoundError 안내"),
    ("invalid_column", ["--input", INPUT_CSV, "--column", "unknown_col", "--threshold", "13.0", "--output-dir", OUT_DIR], "KeyError 안내"),
    ("invalid_threshold", ["--input", INPUT_CSV, "--column", "alcohol", "--threshold", "abc", "--output-dir", OUT_DIR], "ValueError 안내"),
]

error_rows = []
for case_name, args, exp in error_tests:
    res = subprocess.run([sys.executable, CLI_SCRIPT] + args, capture_output=True, text=True)
    err_msg = res.stderr.strip()
    error_rows.append({
        "case": case_name,
        "expected": exp,
        "actual": err_msg,
        "evidence": f"returncode={res.returncode} (정상 실패 처리)"
    })

with open("error_cases.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["case", "expected", "actual", "evidence"])
    writer.writeheader()
    writer.writerows(error_rows)

print(">> [완료] validation_results.csv 및 error_cases.csv 검증 저장 완료")