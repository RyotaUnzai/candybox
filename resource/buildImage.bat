@echo off
chcp 65001

set py=.\resource\imageResource.py
python resource\createQRCImage.py .\
pyside2-rcc.exe -o %py% .\resource\imageResource.qrc

for %%A in (%py%) do set A=%%~nxA
copy %py% src\core\%A%
