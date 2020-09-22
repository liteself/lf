ECHO off

for %%f in (*.dat) do (
    SETLOCAL
    set result=%%f".result"

    echo s         segments  mm        kN > %%f.result
    findstr "^[0-9]" %%f >> %%f.result
)

python main.py .

del *.dat.result
:: for f in data/* ; do bash PreProcess.sh $f ; done