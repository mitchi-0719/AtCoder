#!/bin/bash

# 引数が指定されていない場合はエラーメッセージを表示して終了
if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: $0 <directory> <subdirectory>"
  exit 1
fi

# 引数を変数に格納
x1="$1"
x2="$2"

# out.txtの末尾が改行で終わっていない場合は改行を追加
if [ -f "$x1/$x2/out.txt" ]; then
  if [ -n "$(tail -c 1 "$x1/$x2/out.txt")" ]; then
    echo >> "$x1/$x2/out.txt"
  fi
fi

# コマンドを実行して結果を一時ファイルに保存
temp_output=$(mktemp)
python3 "$x1/$x2/$x2.py" < "$x1/$x2/in.txt" > "$temp_output"

# 結果を比較
if diff -q "$temp_output" "$x1/$x2/out.txt" > /dev/null; then
  echo "correct!"
else
  echo "Output differs:"
  echo "============"
  diff "$temp_output" "$x1/$x2/out.txt"
fi
echo "============"

# 実行結果を表示
echo "Program Output:"
cat "$temp_output"
echo "============"

# 一時ファイルを削除
rm "$temp_output"