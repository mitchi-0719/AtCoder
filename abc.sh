#!/bin/bash


if [ -z "$1" ]; then
    echo "Contest number is empty"
else
    if [ -d "./ABC/$1" ]; then
        echo "./ABC/$1 already exists"
    else
        mkdir ./ABC/$1
    fi

    for p in A B C D E; do
        if [ ! -f "./ABC/$1/$p.py" ]; then
            cp ./template/ABC/main.py "./ABC/$1/$p.py"
        fi
        code "./ABC/$1/$p.py"
    done
fi
