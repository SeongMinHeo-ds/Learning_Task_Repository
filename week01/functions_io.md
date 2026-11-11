# L03 함수 입출력 및 부작용 명세 (functions_io.md)

## 1. 함수 분리 목적과 원칙
- `print`는 콘솔 확인용 단순 출력이며, 실제 파이프라인의 데이터 전달은 명시적인 `return` 값을 사용합니다.
- 파일 I/O와 순수 데이터 가공 로직을 분리하여 모듈 재사용성과 테스트 용이성을 확보했습니다.

## 2. 함수별 세부 명세
- `read_data`: 입력 `filepath (str)`를 받아 `Tuple[List[str], List[Dict[str, Any]]]`를 반환하며, 디스크에서 파일을 읽는 부작용이 있습니다.
- `filter_rows`: 입력 `rows (List[Dict])`, `column (str)`, `threshold (float)`를 받아 `List[Dict[str, Any]]`를 반환하며, 파일 부작용이 없는 순수 함수입니다.
- `summarize`: 입력 `total_rows (int)`, `filtered_rows (List[Dict])`, `column (str)`, `threshold (float)`를 받아 요약 메타데이터 `Dict[str, Any]`를 반환하며, 파일 부작용이 없습니다.
- `save_outputs`: 입력 `summary_data (Dict)`, `filtered_rows (List[Dict])`, `headers (List[str])`, `output_dir (str)`를 받아 반환값은 `None`이며, 지정된 디렉터리에 `wine_summary.json`과 `wine_filtered.csv` 파일을 생성하는 부작용이 있습니다.
- `parse_args`: CLI 명령행 인자(`--input`, `--column`, `--threshold`, `--output-dir`)를 파싱하여 `argparse.Namespace`로 반환합니다.
