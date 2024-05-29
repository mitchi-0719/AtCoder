@echo off
set /p filename="Enter the filename (without extension): "
python "%filename%.py" < "%filename%.in" > "%filename%.out"
