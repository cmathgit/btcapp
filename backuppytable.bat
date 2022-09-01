:: Programmer: Cruz Macias
:: make a backup copy of a table
@ECHO OFF
color 0d
(
echo ****************************************
echo Execution Date: %DATE% 
echo BACKUP TABLE LOG ID: %DATE:~-4,4%%DATE:~-10,2%%DATE:~-7,2%_%TIME:~1,1%%TIME:~3,2%%TIME:~6,2% 

cp btc_rates.tsv legacy\btc_butable_%DATE:~-4,4%%DATE:~-10,2%%DATE:~-7,2%_%TIME:~1,1%%TIME:~3,2%%TIME:~6,2%.tsv

) >> log\backuppy.log

