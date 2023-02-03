import numpy as np
from PIL import ImageGrab
from PIL import Image
import cv2
import time
import matplotlib.pyplot as plt
import os
import MonteCarlo
import Prob_Iniciales
import win32api, win32con
import LeeApuestas
import  pytesseract

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def mover(x,y):
	win32api.SetCursorPos((x,y))

def cls():
	os.system('CLS')
	pass

def borrarPantalla(): 
	if os.name == "posix":
	   os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
	   os.system ("cls")

def Juega(Probabilidad_ganar):

	pass

#EMpieza el programa
lista_cartas=[]
tu_mano=[]
last_time = time.time()
template_cartas=[]
pintas = {'c','d','p','t'}
for num in range (1,14):
	for pinta in pintas:
		template_cartas.append(cv2.cvtColor(cv2.imread('cartas_png/{}{}.png'.format(str(num),pinta)), cv2.COLOR_BGR2GRAY))

threshold=0.98

while (True):
	#declaracion de variables locales.
	last_time=time.time()
	image_1=np.array(ImageGrab.grab(bbox=(0,0,980,700))) #tamano ventana
	image_2=image_1.copy()
	image_1 =cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
	existe_nombre=0
	existe_flot=0
	existe_igualar=0
	#ubico el nombre y la zona de mi mano
	zona_nombre_aux2=[] 
	zona_nombre_aux=[]
	zona_nombre_aux2=zona_nombre_aux[:]
	nombre=cv2.cvtColor(cv2.imread('referencias/nombre.png'), cv2.COLOR_BGR2GRAY)
	w_nom,h_nom =nombre.shape[::-1]
	result_nom = cv2.matchTemplate(image_1, nombre, cv2.TM_CCOEFF_NORMED)
	loc=np.where(result_nom>=threshold)
	for pt_nom in zip (*loc[::-1]):
		cv2.rectangle(image_2, (pt_nom[0]-55, pt_nom[1]-55), (pt_nom[0]+w_nom+50, pt_nom[1]+h_nom+50), (255,0,255),2)
		try:
			zona_nombre_aux=image_2[pt_nom[1]-55:pt_nom[1]+h_nom, pt_nom[0]-55:pt_nom[0]+w_nom+50][:]
			zona_nombre=cv2.cvtColor(zona_nombre_aux, cv2.COLOR_BGR2GRAY)
			existe_nombre=1
		except :
			existe_nombre=0
	#ubico el pozo y la zona del flot.
	zona_flot=cv2.cvtColor(cv2.imread('referencias/pozo.jpg'), cv2.COLOR_BGR2GRAY)
	w_flot,h_flot =zona_flot.shape[::-1]
	result_flot = cv2.matchTemplate(image_1, zona_flot, cv2.TM_CCOEFF_NORMED)
	loc=np.where(result_flot>=threshold)
	#esto para identificar las cartas del flop
	for pt_flot in zip (*loc[::-1]):
		#cv2.rectangle(image_2, (pt_flot[0]+250, pt_flot[1]+110), (pt_flot[0]+w_flot-200, pt_flot[1]+h_flot), (255,0,255),2)
		zona_flot_aux=image_2[pt_flot[1]+h_flot:pt_flot[1]+110, pt_flot[0]+w_flot-200:pt_flot[0]+250][:]
		zona_flot=cv2.cvtColor(zona_flot_aux, cv2.COLOR_BGR2GRAY)
		existe_flot=1
	#esto para identificar el monto del pozo
	texto_pozo='No hay pozo aun'
	for pt_flot in zip (*loc[::-1]):
		#cv2.rectangle(image_2, (pt_flot[0]+100, pt_flot[1]+20), (pt_flot[0], pt_flot[1]), (255,0,255),2)
		zona_flot_aux2=image_2[pt_flot[1]:pt_flot[1]+15, pt_flot[0]:pt_flot[0]+100][:]
		#zona_flot2=cv2.cvtColor(zona_flot_aux2, cv2.COLOR_BGR2GRAY)
		texto_pozo=LeeApuestas.TextoApuesta(zona_flot_aux2)
	#Si hay nombre entonces busco mis cartas
	if existe_nombre==1:
		lista_cartas=[]
		tu_mano=[]
		contador=0
		for num in range (1,14):
			for pinta in pintas:
				template= template_cartas[contador]
				contador+=1
				#mis cartas en zona de nombre
				w,h =template.shape[::-1]
				result = cv2.matchTemplate(zona_nombre, template, cv2.TM_CCOEFF_NORMED)
				loc=np.where(result>=threshold)
				for pt in zip (*loc[::-1]):
					tu_mano.append ('{}{}'.format(str(num),pinta))
				#busco las cartas del flot cenrca del pozo.
				w,h =template.shape[::-1]
				result = cv2.matchTemplate(zona_flot, template, cv2.TM_CCOEFF_NORMED)
				loc=np.where(result>=threshold)
				for pt in zip (*loc[::-1]):
					lista_cartas.append('{}{}'.format(str(num),pinta))
		#buscar boton pasar
		pasar=cv2.cvtColor(cv2.imread('botones/pasar.jpg'), cv2.COLOR_BGR2GRAY)
		existe_pasar=0
		w_pasar,h_pasar =pasar.shape[::-1]
		result_pasar = cv2.matchTemplate(image_1, pasar, cv2.TM_CCOEFF_NORMED)
		loc=np.where(result_pasar>=threshold)
		for pt_pasar in zip (*loc[::-1]):
			existe_pasar=1
		existe_no_ir=0
		existe_igualar=0
		if existe_pasar==0:
			#buscar boton igualar
			igualar=cv2.cvtColor(cv2.imread('botones/igualar.jpg'), cv2.COLOR_BGR2GRAY)
			
			w_igualar,h_igualar =igualar.shape[::-1]
			result_igualar = cv2.matchTemplate(image_1, igualar, cv2.TM_CCOEFF_NORMED)
			loc=np.where(result_igualar>=threshold)
			for pt_igualar in zip (*loc[::-1]):
				imagen_igualar=image_2[pt_igualar[1]+h_igualar:pt_igualar[1]+70, pt_igualar[0]+w_igualar-100:pt_igualar[0]+100][:]
				texto_igualar=LeeApuestas.TextoApuesta(imagen_igualar)
				existe_igualar=1
			#buscar boton no ir
			no_ir=cv2.cvtColor(cv2.imread('botones/no_ir.jpg'), cv2.COLOR_BGR2GRAY)
			w_no_ir,h_no_ir =no_ir.shape[::-1]
			result_no_ir = cv2.matchTemplate(image_1, no_ir, cv2.TM_CCOEFF_NORMED)
			loc=np.where(result_no_ir>=threshold)
			for pt_no_ir in zip (*loc[::-1]):
				existe_no_ir=1
			pass
		#Busca Subir
		subir=cv2.cvtColor(cv2.imread('botones/subir.png'), cv2.COLOR_BGR2GRAY)
		existe_subir=0
		w_subir,h_subir=subir.shape[::-1]
		result_subir = cv2.matchTemplate(image_1, subir, cv2.TM_CCOEFF_NORMED)
		loc=np.where(result_subir>=threshold)
		for pt_subir in zip (*loc[::-1]):
			existe_subir=1
		#buscar boton apostar
		apostar=cv2.cvtColor(cv2.imread('botones/apostar.jpg'), cv2.COLOR_BGR2GRAY)
		existe_apostar=0
		w_apostar,h_apostar =apostar.shape[::-1]
		result_apostar = cv2.matchTemplate(image_1, apostar, cv2.TM_CCOEFF_NORMED)
		loc=np.where(result_apostar>=threshold)
		for pt_apostar in zip (*loc[::-1]):
			imagen_apostar=image_2[pt_apostar[1]+h_apostar:pt_apostar[1]+70, pt_apostar[0]+w_apostar-100:pt_apostar[0]+100][:]
			texto_apostar=LeeApuestas.TextoApuesta(imagen_apostar)
			existe_apostar=1
		#Busca he vuelto
		vuelto=cv2.cvtColor(cv2.imread('botones/vuelto.png'), cv2.COLOR_BGR2GRAY)
		existe_vuelto=0
		w_vuelto,h_vuelto=vuelto.shape[::-1]
		result_vuelto = cv2.matchTemplate(image_1, vuelto, cv2.TM_CCOEFF_NORMED)
		loc=np.where(result_vuelto>=threshold)
		for pt_vuelto in zip (*loc[::-1]):
			click(pt_vuelto[0],pt_vuelto[1])
			pass
		#En juegos ZOOM busca retirar
		"""
		Retirarse=cv2.cvtColor(cv2.imread('botones/retirarse.png'), cv2.COLOR_BGR2GRAY)
		existe_retirarse=0
		w_retirarse,h_retirarse=Retirarse.shape[::-1]
		result_retirarse = cv2.matchTemplate(image_1, Retirarse, cv2.TM_CCOEFF_NORMED)
		loc=np.where(result_retirarse>=threshold)
		for pt_retirarse in zip (*loc[::-1]):
			existe_retirarse=1"""
		#Busca Oponente
		Oponente=cv2.cvtColor(cv2.imread('botones/carta.png'), cv2.COLOR_BGR2GRAY)
		existe_oponente=0
		w_oponente,h_oponente=Oponente.shape[::-1]
		result_oponente=cv2.matchTemplate(image_1, Oponente, cv2.TM_CCOEFF_NORMED)
		loc=np.where(result_oponente>=threshold)
		for pt_oponente in zip (*loc[::-1]):
			existe_oponente+=1
		#imprime
		cls()
		print ('---------------------------------')
		print ('En la mesa: ')
		print (lista_cartas)
		print (' y tu mano es:')
		print (tu_mano)
		print ('Oponentes: '+ str(existe_oponente/2))
		if existe_igualar==1:
			print ('Igualar: ' + str(texto_igualar))
		if existe_apostar==1:
			print ('Apostar: ' + str(texto_apostar))
		print (texto_pozo)
		#estudiamos la mano
		#primero definimos los parametos
		mucho=0.2
		muchisimo=0.5
		Prob_Baja=0.65
		Prob_Baja_Med=0.7
		Prob_Alta_Med=0.8
		Prob_Alta=0.9

		#Respuesta a los ALL-IN
		if existe_no_ir==1 and existe_igualar==1 and existe_apostar==0 and existe_subir==0:
			Probabilidad_ganar=MonteCarlo.Probabilidades(tu_mano, lista_cartas, 1)
			if Probabilidad_ganar>Prob_Alta:
				mover(pt_igualar[0], pt_igualar[1])
				click(pt_igualar[0], pt_igualar[1])
			else:
				mover(pt_no_ir[0],pt_no_ir[1])
				click(pt_no_ir[0],pt_no_ir[1])
				pass
			pass
		#Si es despues del Flot
		if len(lista_cartas)>0:
			if existe_no_ir==1 or existe_pasar==1:
				Probabilidad_ganar=MonteCarlo.Probabilidades(tu_mano, lista_cartas, 1)
				print ('Tu Probabilidad de ganar es: {}'.format(Probabilidad_ganar))
				#baja probabilidad
				#Juega(Probabilidad_ganar)
				if existe_no_ir==1 and Probabilidad_ganar<Prob_Baja:
					mover(pt_no_ir[0],pt_no_ir[1])
					click(pt_no_ir[0],pt_no_ir[1])
				pass
				if existe_pasar==1 and Probabilidad_ganar<Prob_Baja:
					mover(pt_pasar[0],pt_pasar[1])
					click(pt_pasar[0],pt_pasar[1])
					pass
				#Igualar y Apostar
				if existe_igualar==1 and Probabilidad_ganar>Prob_Baja:
					if Probabilidad_ganar<0.70 and texto_igualar>mucho:
						mover(pt_no_ir[0], pt_no_ir[1])
						click(pt_no_ir[0], pt_no_ir[1])
						pass
					elif Probabilidad_ganar<0.8 and texto_igualar>muchisimo:
						mover(pt_no_ir[0], pt_no_ir[1])
						click(pt_no_ir[0], pt_no_ir[1])
						pass
					else:
						print(pt_igualar[0])
						print(pt_igualar[1])
						mover(pt_igualar[0], pt_igualar[1])
						click(pt_igualar[0], pt_igualar[1])
						pass
					pass
				if existe_apostar==1 and existe_pasar==1 and Probabilidad_ganar>Prob_Baja:
					if Probabilidad_ganar<0.70 and texto_apostar>mucho:
						mover(pt_pasar[0], pt_pasar[1])
						click(pt_pasar[0], pt_pasar[1])
						pass
					elif Probabilidad_ganar<0.8 and texto_apostar>muchisimo:
						mover(pt_pasar[0], pt_pasar[1])
						click(pt_pasar[0], pt_pasar[1])
						pass
					else:
						print (pt_apostar[0])
						print (pt_apostar[1])
						mover(pt_apostar[0], pt_apostar[1])
						click(pt_apostar[0], pt_apostar[1])
						pass
					pass
				if existe_apostar==1 and Probabilidad_ganar>0.8:
					if Probabilidad_ganar>Prob_Alta:
						#Busca Retirarse
						maxi=cv2.cvtColor(cv2.imread('botones/max.png'), cv2.COLOR_BGR2GRAY)
						existe_pozo=0
						w_maxi,h_maxi=maxi.shape[::-1]
						result_maxi = cv2.matchTemplate(image_1, maxi, cv2.TM_CCOEFF_NORMED)
						loc=np.where(result_maxi>=threshold)
						for pt_max in zip (*loc[::-1]):
							mover(pt_max[0],pt_max[1])
							click(pt_max[0],pt_max[1])
							pass	
						pass
						mover(pt_apostar[0], pt_apostar[1])
						click(pt_apostar[0], pt_apostar[1])
					if Probabilidad_ganar<Prob_Alta and texto_apostar>=mucho:
						mover(pt_pasar[0], pt_pasar[1])
						click(pt_pasar[0], pt_pasar[1])
						pass
					elif Probabilidad_ganar<Prob_Alta and texto_apostar<mucho:
						mover(pt_apostar[0], pt_apostar[1])
						click(pt_apostar[0], pt_apostar[1])
					pass
				if existe_subir==1 and Probabilidad_ganar>0.8:
					if Probabilidad_ganar>Prob_Alta:
						#Busca Retirarse
						maxi=cv2.cvtColor(cv2.imread('botones/max.png'), cv2.COLOR_BGR2GRAY)
						existe_max=0
						w_max,h_max=maxi.shape[::-1]
						result_max = cv2.matchTemplate(image_1, maxi, cv2.TM_CCOEFF_NORMED)
						loc=np.where(result_max>=threshold)
						for pt_max in zip (*loc[::-1]):
							mover(pt_max[0],pt_max[1])
							click(pt_max[0],pt_max[1])
							pass	
						pass
					click(pt_subir[0], pt_subir[1])
					pass
					if Probabilidad_ganar<Prob_Alta and texto_igualar<mucho:
						mover(pt_igualar[0], pt_igualar[1])
						click(pt_igualar[0], pt_igualar[1])
						pass
					elif Probabilidad_ganar<Prob_Alta and texto_igualar>=mucho:
						mover(pt_no_ir[0], pt_no_ir[1])
						click(pt_no_ir[0], pt_no_ir[1])
					pass
					pass
			pass
		#antes del Flot
		else:
			#antes de que llegue a mi el turno de jugar
			"""if existe_retirarse==1:
				try:
					Probabilidad_ganar=Prob_Iniciales.Probabilidades(tu_mano)+Prob_Iniciales.Probabilidades([tu_mano[1],tu_mano[0]])					
				except :
					pass
				if Probabilidad_ganar<Prob_Baja:
					print(pt_retirarse[0])
					print(pt_retirarse[1])
					mover(pt_retirarse[0], pt_retirarse[1])
					click(pt_retirarse[0], pt_retirarse[1])
					pass
				pass"""
			#cuando me llega el turno
			if existe_no_ir==1 or existe_pasar==1:
				Probabilidad_ganar=Prob_Iniciales.Probabilidades(tu_mano)+Prob_Iniciales.Probabilidades([tu_mano[1],tu_mano[0]])	
				print ('Tu Probabilidad de ganar es: {}'.format(Probabilidad_ganar))
				#baja probabilidad
				if existe_no_ir==1 and Probabilidad_ganar<Prob_Baja:
					mover(pt_no_ir[0],pt_no_ir[1])
					click(pt_no_ir[0],pt_no_ir[1])
				pass
				if existe_pasar==1 and Probabilidad_ganar<Prob_Baja:
					mover(pt_pasar[0],pt_pasar[1])
					click(pt_pasar[0],pt_pasar[1])
					pass
				#Igualar y Apostar
				if existe_igualar==1 and Probabilidad_ganar>Prob_Baja:
					if Probabilidad_ganar<0.70 and texto_igualar>mucho:
						mover(pt_no_ir[0], pt_no_ir[1])
						click(pt_no_ir[0], pt_no_ir[1])
						pass
					elif Probabilidad_ganar<0.8 and texto_igualar>muchisimo:
						mover(pt_no_ir[0], pt_no_ir[1])
						click(pt_no_ir[0], pt_no_ir[1])
						pass
					else:
						print(pt_igualar[0])
						print(pt_igualar[1])
						mover(pt_igualar[0], pt_igualar[1])
						click(pt_igualar[0], pt_igualar[1])
						pass
					pass
				if existe_subir==1 and existe_pasar==1 and Probabilidad_ganar>Prob_Baja:
					if Probabilidad_ganar<0.70 and texto_apostar>mucho:
						mover(pt_pasar[0], pt_pasar[1])
						click(pt_pasar[0], pt_pasar[1])
						pass
					elif Probabilidad_ganar<0.8 and texto_apostar>=muchisimo:
						mover(pt_pasar[0], pt_pasar[1])
						click(pt_pasar[0], pt_pasar[1])
						pass
					else:
						mover(pt_subir[0], pt_subir[1])
						click(pt_subir[0], pt_subir[1])
						pass
					pass
				if existe_subir==1 and Probabilidad_ganar>Prob_Alta_Med:
					if Probabilidad_ganar>Prob_Alta:
						maxi=cv2.cvtColor(cv2.imread('botones/max.png'), cv2.COLOR_BGR2GRAY)
						existe_max=0
						w_max,h_pozo=maxi.shape[::-1]
						result_max = cv2.matchTemplate(image_1, maxi, cv2.TM_CCOEFF_NORMED)
						loc=np.where(result_max>=threshold)
						for pt_max in zip (*loc[::-1]):
							mover(pt_max[0],pt_max[1])
							click(pt_max[0],pt_max[1])
							time.sleep(5)
							pass	
						pass
						mover(pt_subir[0], pt_subir[1])	
						click(pt_subir[0], pt_subir[1])
					if Probabilidad_ganar<Prob_Alta and texto_igualar<mucho:
						mover(pt_subir[0], pt_subir[1])
						click(pt_subir[0], pt_subir[1])
						pass
					elif Probabilidad_ganar<Prob_Alta and texto_igualar>mucho:
						mover(pt_no_ir[0], pt_no_ir[1])
						click(pt_no_ir[0], pt_no_ir[1])
					pass
				if existe_subir==1 and Probabilidad_ganar>0.8:
					if Probabilidad_ganar>Prob_Alta:
						#Busca Retirarse
						maxi=cv2.cvtColor(cv2.imread('botones/max.png'), cv2.COLOR_BGR2GRAY)
						existe_max=0
						w_max,h_max=maxi.shape[::-1]
						result_max = cv2.matchTemplate(image_1, maxi, cv2.TM_CCOEFF_NORMED)
						loc=np.where(result_max>=threshold)
						for pt_max in zip (*loc[::-1]):
							mover(pt_max[0],pt_max[1])
							click(pt_max[0],pt_max[1])
							pass	
						pass
						mover(pt_subir[0], pt_subir[1])
						click(pt_subir[0], pt_subir[1])
					pass
					if Probabilidad_ganar<Prob_Alta:
						mover(pt_igualar[0], pt_igualar[1])
						click(pt_igualar[0], pt_igualar[1])
						pass
						
					pass
				pass
			pass	
		pass
	#imprime la pantalla
	"""
	if len(tu_mano)>0:
		print('Loop took {} segundos'. format(time.time()-last_time))
		print(tu_mano)
		print(lista_cartas)
		passq
	"""
	cv2.imshow ('windows', cv2.cvtColor(image_2, cv2.COLOR_BGR2RGB))
	if existe_nombre==1:
		cv2.imshow ('windows1', cv2.cvtColor(zona_nombre_aux, cv2.COLOR_BGR2RGB))
		pass
	if existe_flot==1:
		cv2.imshow ('windows2', cv2.cvtColor(zona_flot_aux, cv2.COLOR_BGR2RGB))
		cv2.imshow ('windows2', cv2.cvtColor(zona_flot_aux2, cv2.COLOR_BGR2RGB))
		pass
	if existe_igualar==1:
		cv2.imshow ('windows3', cv2.cvtColor(imagen_igualar, cv2.COLOR_BGR2RGB))
		pass

	if cv2.waitKey(25) & 0xFF== ord ('q'):
		cv2.destroyAllWindows ()
		break