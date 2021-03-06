from Tkinter import * 
import threading
import time
from firebase import firebase
import os
import RPi.GPIO as GPIO
#configuraciones
firebase = firebase.FirebaseApplication('https://domotica-2020.firebaseio.com/',None)
GPIO.setmode(GPIO.BCM) 
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) 


if __name__ == '__main__':

		def relay1():
			if t_btn['text'] == 'encendido':
				t_btn.config(text='apagado')
                                GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
				firebase.put('/','reley-1','apagado')
				
			else:
				t_btn.config(text='encendido')
				GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
                                firebase.put('/','reley-1','encendido')
				

		def relay2():
			if t_btn2['text'] == 'encendido':      
				t_btn2.config(text='apagado')
				firebase.put('/','reley-2','apagado')
				

			else:
				t_btn2.config(text='encendido')
				firebase.put('/','reley-2','encendido')
				

		def relay3():
			if t_btn3['text'] == 'encendido':
				t_btn3.config(text='apagado')
				firebase.put('/','reley-3','apagado')
				

			else:
				t_btn3.config(text='encendido')
				firebase.put('/','reley-3','encendido')
				


		def relay4():
			if t_btn4['text'] == 'encendido':
				t_btn4.config(text='apagado')
				firebase.put('/','reley-4','apagado')
				

			else:
				t_btn4.config(text='encendido')
				firebase.put('/','reley-4','encendido')
				

		def relay5():
			if t_btn5['text'] == 'encendido':
				t_btn5.config(text='apagado')
				firebase.put('/','reley-5','apagado')
				

			else:
				t_btn5.config(text='encendido')
				firebase.put('/','reley-5','encendido')
				


		def relay6():
			if t_btn6['text'] == 'encendido':
				t_btn6.config(text='apagado')
				firebase.put('/','reley-6','apagado')
           

			else:
				t_btn6.config(text='encendido')
				firebase.put('/','reley-6','encendido')
                 	




		root=Tk()

		root.title("control de reley")
		root.geometry("650x350")
		root.config(bg="#17202f")

		miFrame=Frame(root,width=550,height=250)
		miFrame.config(bg="#17202f")
		miFrame.pack()
		x="----"

		t_btn = Button(text= x, width=12, command=relay1)
		t_btn.place(x=100,y=100)

		t_btn2 = Button(text= x, width=12, command=relay2)
		t_btn2.place(x=100,y=150)

		t_btn3 = Button(text= x, width=12, command=relay3)
		t_btn3.place(x=100,y=200)

		t_btn4 = Button(text= x, width=12, command=relay4)
		t_btn4.place(x=100,y=250)

		t_btn5 = Button(text= x, width=12, command=relay5)
		t_btn5.place(x=100,y=300)

		t_btn6 = Button(text= x, width=12, command=relay6)
		t_btn6.place(x=100,y=350)
        
                
                
        
    
                    
		def info():
			threading.Timer(10.0, info).start()
			result = firebase.get('/reley-1','')
			t_btn.config(text=result)
                        checkout(RELAIS_1_GPIO,result) 
                 
                
		def info2():
			threading.Timer(1.0, info2).start()
			result = firebase.get('/reley-2','')
			t_btn2.config(text=result)

		def info3():
			threading.Timer(1.0, info3).start()
			result = firebase.get('/reley-3','')
			t_btn3.config(text=result)

		def info4():
			threading.Timer(1.0, info4).start()
			result = firebase.get('/reley-4','')
			t_btn4.config(text=result)

		def info5():
			threading.Timer(1.0, info5).start()
			result = firebase.get('/reley-5','')
			t_btn5.config(text=result)

		def info6():
			threading.Timer(1.0, info6).start()
			result = firebase.get('/reley-6','')
			t_btn6.config(text=result)

                def checkout(pin,resultado):
                    if(resultado == "apagado"):
                        print("esta apagado")
                        return GPIO.output(pin, GPIO.LOW)
                    else:
                        print("esta encendido")
                        return GPIO.output(pin, GPIO.HIGH)
                
                
		def popo():
			root.destroy()
			os._exit(1)
            
		info()
		info2()
		info3()
		info4()
		info5()
		info6()
		
		
		root.protocol('WM_DELETE_WINDOW', popo)
		root.mainloop()