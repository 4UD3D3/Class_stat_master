@echo off

::------------------------------------------------
:: Running Python API
::------------------------------------------------

echo Lancement API python (mail + stats)...
start cmd /k "cd scripts_stats & python -m flask run"

::------------------------------------------------
:: Running react server
::------------------------------------------------

echo Lancement react server...
start cmd /k "cd platform & npm start"