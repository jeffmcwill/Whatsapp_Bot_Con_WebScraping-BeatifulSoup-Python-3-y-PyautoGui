import pyautogui
import time
import webbrowser

#en esta version del programa solo envia el mensaje cada vez que lo ejecutamos
#en nuestra pc, vere si consigo que pueda enviarte actualizaciones del precio 
#cada cierto tiempo.
#-----------------------------------------------------------------------------
#sirve para conectar el programa de python con tu cuenta de whatsapp.

numerodetelefono='...'
#se agrega aqui el numero de telefono.

msm=open('mensajes.txt')
mensajes=[]

for i in msm:
	mensajes.append(i)

url='https://web.whatsapp.com/send?phone='
#se usa esto para añadir la url del whatsapp web.

webbrowser.open(url+numerodetelefono)
time.sleep(8)

#----------------------------------------------------------------------
#este algoritmo abre el archivo en modo lectura y envia
#el contenido de este al usuario que nosotros hayamos elegido.
#en este caso con el uso del web scrapping envia los datos actualizados
#del dolar blue tanto compra como venta.
#-----------------------------------------------------------------------

with open('mensajes.txt','r') as file:
	for line in file:
		pyautogui.typewrite(line)
		pyautogui.press("enter")