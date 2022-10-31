import requests
from datetime import date
import pyodbc

requis= requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
requis_dic = requis.json()
cot_dolar = requis_dic["USDBRL"]["bid"]

server = 'Your server' 
database = 'Your database' 
username = 'Your username' 
password = 'Your password' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

_date = date.today()
_datef = format(_date, '%d/%m/%Y')

cursor.execute("INSERT INTO svdolar (data, valor) VALUES ('"+ _datef +"',"+ str(float(cot_dolar)) +")")
cnxn.commit()
print('Inclusão concluída')