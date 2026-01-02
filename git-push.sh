#!/bin/bash


if [ -z "$1" ]; then
  echo "Contest number is empty"
else
  git add .
  git commit -m "$1"
  git push
fi
