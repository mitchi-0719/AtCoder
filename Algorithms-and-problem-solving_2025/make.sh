#!/bin/bash

# 引数が2つ渡されているか確認
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <directory> <subdirectory>"
  exit 1
fi

# 引数を2つ受け取る
x1=$1
x2=$2

# x1の中にx2というディレクトリを作成
mkdir -p "$x1/$x2"

# その中に in.txt, out.txt を作成
touch "$x1/$x2/in.txt"
touch "$x1/$x2/out.txt"

# x2.py を ../../template/ICPC.py からコピーして作成
cp "./../template/ICPC.py" "$x1/$x2/$x2.py"

# 作成したファイルを開く
code "$x1/$x2/in.txt"
code "$x1/$x2/out.txt"
code "$x1/$x2/$x2.py"

echo "Directory and files created successfully in $x1/$x2"