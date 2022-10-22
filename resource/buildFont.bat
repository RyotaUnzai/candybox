@echo off
chcp 65001

set py=.\resource\fontResource.py
python resource\createQRCFont.py .\
pyside2-rcc.exe -o %py% .\resource\fontResource.qrc

for %%A in (%py%) do set A=%%~nxA
copy %py% src\core\%A%
