:: Programmer: Cruz Macias
:: run a python script
@ECHO OFF
color 0d
(
echo ****************************************
echo Execution Date: %DATE% 
echo py_script LOG ID: %DATE:~-4,4%%DATE:~-10,2%%DATE:~-7,2%_%TIME:~1,1%%TIME:~3,2%%TIME:~6,2% 

python btc_api_comp.py

) >> log\btc_program.log
