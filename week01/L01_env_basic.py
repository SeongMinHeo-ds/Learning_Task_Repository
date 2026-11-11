import sys
import os

# 1. 실행 Python과 현재 경로 확인 (L01 요구사항 1)
print("=== L01 환경 확인 ===")
print("Python Executable Path:", sys.executable)
print("Python Version:", sys.version)
print("Current Working Directory:", os.getcwd())
print()

# 2. 기본 값, 조건문, 반복문 실행 (L01 요구사항 2)
print("=== L01 기본 값·조건·반복 ===")
numbers = [1, 2, 3, 4, 5]
threshold = 3

for num in numbers:
    if num > threshold:
        print(f"숫자 {num}: 임계값({threshold}) 초과")
    else:
        print(f"숫자 {num}: 임계값({threshold}) 이하")