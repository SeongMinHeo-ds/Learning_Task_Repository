#!/usr/bin/env bash

echo "=== [1] 현재 작업 위치 확인 ==="
pwd

echo ""
echo "=== [2] basics.py 실행 (합계 6, 선택 [2,3] 검증) ==="
"/c/Program Files/Python312/python.exe" basics.py

echo ""
echo "=== [3] 상대 경로 설명 ==="
echo "스크립트 실행 전 위치가 바뀌면(cd) 기준점이 달라져 파일 상대경로도 달라짐"

echo ""
echo "=== [4] Git 상태 ==="
git status