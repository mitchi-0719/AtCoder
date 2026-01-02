#!/bin/bash


if [ -d "./paiza/$1/$2.py" ]; then
    echo "./paiza/$1/$2.py already exists"
else
    if [ ! -d "./paiza/$1" ]; then
        mkdir ./paiza/$1
    fi
    cp ./template/Paiza.py "./paiza/$1/$2.py"
    code "./paiza/$1/$2.py"
fi