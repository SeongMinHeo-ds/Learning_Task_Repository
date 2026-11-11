import sys
import os

print("=== L01 환경 확인 ===")
print("Python Executable Path:", sys.executable)
print("Python Version:", sys.version)
print("Current Working Directory:", os.getcwd())
print()

print("=== L01 기본 값·조건·반복 ===")
numbers = [1, 2, 3]

# [1, 2, 3] 반복 합계
total_sum = 0
for n in numbers:
    total_sum += n

# 2 이상인 항목 필터
selected = []
for n in numbers:
    if n >= 2:
        selected.append(n)

print(f"입력 리스트: {numbers}")
print(f"합계 결과: {total_sum}")
print(f"2 이상 선택 결과: {selected}")