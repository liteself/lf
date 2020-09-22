ECHO off

for %%f in (*.dat) do (
    SETLOCAL

    head -n 8 %%f | tail -n 1 > %%f.result
    findstr  "^[^a-zA-Z]" %%f >> %%f.result
)

for %%f in (*.csv) do (
    SETLOCAL

    tail -n +2 %%f > %%f.result
)

python r.py .

:: del *.dat.temp

pause