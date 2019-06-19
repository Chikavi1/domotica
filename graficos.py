from Tkinter import * 
import threading
import time
from firebase import firebase
firebase = firebase.FirebaseApplication('https://domotica-2020.firebaseio.com/',None)
if __name__ == '__main__':
#import Adafruit_DHT
#humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
		def put_temperatura():
		  threading.Timer(1.0, put_temperatura).start()
		  medida = 23.434
		  firebase.put('/','temperatura',medida)

		put_temperatura()

		
		def relay1():
			threading.Timer(1.0, relay1).start()
			result = firebase.get('/reley-1','')
			print(result)
			if result == 'encendido':
		        #t_btn.config(text='apagado')
				firebase.put('/','reley-1','apagado')
				print("apague reley")
			else:
		    #t_btn.config(text='encendido')
				firebase.put('/','reley-1','encendido')
				print("encendi reley")
		
		def relay2():
		    if t_btn2.config('text')[-1] == 'encendido':
		        #t_btn.config(text='apagado')
		        firebase.put('/','reley-2','apagado')
		        print("apague reley")
		    else:
		        #t_btn.config(text='encendido')
		        firebase.put('/','reley-2','encendido')
		        print("encendi reley")
		root=Tk()
		root.title("control de reley")
		root.geometry("650x350")
		root.config(bg="#17202f")

		miFrame=Frame(root,width=550,height=250)
		miFrame.config(bg="#17202f")
		miFrame.pack()


		def temperatura():
		  threading.Timer(1.0, temperatura).start()
		  nombre.set("Temperatura: {0:0.1f} \n ".format(firebase.get('/temperatura','')))
		  miLabel = Label(miFrame,textvariable = nombre, bg="#17202f",fg="white")
		  miLabel.place(x=350,y=100)


		nombre = StringVar()
		temperatura()

		#nombre.set("Temperatura: {0:0.1f} \n ".format(temp))

		#print('Temp={0:0.1f}  Humidity={1:0.1f}%'.format(temperature, humidity))
		#miLabel = Label(miFrame,textvariable = nombre, bg="#17202f",fg="white")
		#miLabel.place(x=350,y=100)
		x = "------"

		t_btn = Button(text= x, width=12, command=relay1)
		t_btn.place(x=400,y=200)

		t_btn2 = Button(text= x, width=12, command=relay2)
		t_btn2.place(x=400,y=300)

		def reley1():
		 threading.Timer(1.0, reley1).start()
		 global x
		 x = firebase.get('/reley-1','')
		 t_btn.config(text= x)
		 if x == "encendido" :
		  print("prendi esta wea")
		 else :
		 	print("apague esta wea")
		reley1()

		def reley2():
		 threading.Timer(1.0, reley2).start()
		 global x2
		 x2= firebase.get('/reley-2','')
		 t_btn2.config(text= x2)
		reley2()


		root.mainloop()