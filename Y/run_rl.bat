ECHO off

for %%f in (*.dat) do (
    SETLOCAL

    head -n 8 %%f | tail -n 1 > %%f.result
    findstr  "^[^a-zA-Z]" %%f >> %%f.result
)


python rl.py .

:: del *.dat.temp

pause