import threading
import time
from firebase import firebase
firebase = firebase.FirebaseApplication('https://domotica-2020.firebaseio.com/',None)

def hola_mundo(nombre):
	print("hola_mundo " + nombre)
	time.sleep(5)

if __name__ == '__main__':
	firebase.get('/temperatura','')

	thread = threading.Thread(target=hola_mundo, args=("chikavi",))
	thread.start()
	thread.join()
	print("hola mundo desde el hilo principal")
	time.sleep(16)
