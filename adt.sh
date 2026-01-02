#!/bin/bash


if [ -z "$1" ]; then
    echo "Contest number is empty"
else
    if [ -d "./ADT/$1" ]; then
        echo "./ADT/$1 already exists"
    else
        mkdir ./ADT/$1
    fi

    for p in A B C D E F G H; do
        if [ ! -f "./ADT/$1/$p.py" ]; then
            cp ./template/ABC.py "./ADT/$1/$p.py"
        fi
        code "./ADT/$1/$p.py"
    done
fi
