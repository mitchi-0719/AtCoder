if [ -z "$1" ]; then
    echo "Contest number is empty"
else
    if [ -d "./ABC/$1" ]; then
        echo "./ABC/$1 already exists"
    else
        mkdir ./ABC/$1
    fi
    touch ./ABC/$1/A.py
    touch ./ABC/$1/B.py
    touch ./ABC/$1/C.py
    touch ./ABC/$1/D.py
    code ./ABC/$1/D.py
    code ./ABC/$1/C.py
    code ./ABC/$1/B.py
    code ./ABC/$1/A.py
fi
