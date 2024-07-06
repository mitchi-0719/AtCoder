#!/bin/bash

# ファイル名の設定
OUT_FILE="$1.out"
ANS_FILE="$1.ans"

# ファイルの存在確認
if [ ! -f "$OUT_FILE" ]; then
    echo "Error: $OUT_FILE not found"
    exit 1
fi

if [ ! -f "$ANS_FILE" ]; then
    echo "Error: $ANS_FILE not found"
    exit 1
fi

# ファイルの比較
if diff -q $1.out $1.ans > /dev/null; then
    echo "Accept!"
else
    echo "Wrong Answer!"
fi
