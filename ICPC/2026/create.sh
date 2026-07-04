mkdir $1
cp temp.py $1/$1.py
touch $1/$1.in
touch $1/$1.ans
code $1/$1.py
code $1/$1.in
code $1/$1.ans