import requests
from bs4 import BeautifulSoup
import datetime as strftime,datetime

#este archivo sirve para sacar los datos de la pagina web
#al cual le vamos a aplicar el metodo de web scraping

url='https://www.cronista.com/MercadosOnline/moneda.html?id=ARSB'
#se toman los datos en tiempo real de la web el cronista.com

pagina=requests.get(url)
bs = BeautifulSoup(pagina.content,'html.parser')


mensaje = bs.find_all('div',class_='buy-value')
mensaje2 = bs.find_all('div',class_='sell-value')
texto = open('mensajes.txt','w')

for i in mensaje:
	texto.write("--------------------\n")
	texto.write("Dolar Blue Compra: ")
	texto.write(i.text)

for e in mensaje2:
	texto.write("\nDolar Blue Venta: ")
	texto.write(e.text)
	texto.write("\nFuente: Cronista.com")
	texto.write("\n--------------------")

print("Funcionando.")

