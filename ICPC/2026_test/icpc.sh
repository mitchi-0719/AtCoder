#!/bin/bash

# 引数を変数に格納
x1="$1"
x2="$2"

# out.txtの末尾が改行で終わっていない場合は改行を追加
if [ -f "$x1/$x1.ans" ]; then
  if [ -n "$(tail -c 1 "$x1/$x1.ans")" ]; then
    echo >> "$x1/$x1.ans"
  fi
fi

# コマンドを実行して結果を一時ファイルに保存
temp_output=$(mktemp)
python3 "$x1/$x1.py" < "$x1/$x1.in" > "$temp_output"

# 結果を比較
if diff -q "$temp_output" "$x1/$x1.ans" > /dev/null; then
  echo "correct!"
else
  echo "Output differs:"
  echo "============"
  diff "$temp_output" "$x1/$x1.ans"
  echo "============"
  echo "Expected Output:"
  cat "$x1/$x1.ans"
fi
echo "============"

# 実行結果を表示
echo "Program Output:"
cat "$temp_output"
echo "============"

# 一時ファイルを削除
rm "$temp_output"