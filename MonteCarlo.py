import numpy as np
import time
from itertools import combinations

def BuscarEscaleraColor(arre_de_manos):
	cont=0
	mejor_puntaje=0
	mejor_mano=[]
	resultado=[]
	resultado.append([])
	resultado.append([])
	while cont<(len(arre_de_manos)-1):
		mano_aux_escalera=[]
		mano_aux_escalera_color=[]
		puntaje_aux=0
		for x in range(0,5):
			if len(arre_de_manos[cont][x])==2:
				mano_aux_escalera.append(float(arre_de_manos[cont][x][0]))
				mano_aux_escalera_color.append(arre_de_manos[cont][x][1])
				pass
			if len(arre_de_manos[cont][x])==3:
				mano_aux_escalera.append(float(arre_de_manos[cont][x][0:2]))
				mano_aux_escalera_color.append(arre_de_manos[cont][x][2])
				pass
			pass
		mano_aux_escalera_ordenada=sorted(mano_aux_escalera)
		#print(arre_de_manos)
		#print (arre_de_manos[cont])
		#print (mano_aux_escalera_ordenada)
		if len(mano_aux_escalera_ordenada)==5:
			if mano_aux_escalera_ordenada[0]+1==mano_aux_escalera_ordenada[1] and mano_aux_escalera_ordenada[1]+1==mano_aux_escalera_ordenada[2] and mano_aux_escalera_ordenada[2]+1==mano_aux_escalera_ordenada[3] and mano_aux_escalera_ordenada[3]+1==mano_aux_escalera_ordenada[4]:
				if mano_aux_escalera_color[0]==mano_aux_escalera_color[1] and mano_aux_escalera_color[1]==mano_aux_escalera_color[2] and mano_aux_escalera_color[2]==mano_aux_escalera_color[3] and mano_aux_escalera_color[3]==mano_aux_escalera_color[4]:
					puntaje_aux=8+mano_aux_escalera_ordenada[4]/100
					pass
					
				pass
			if mano_aux_escalera_ordenada[0]==1:
				if mano_aux_escalera_ordenada[1]+1==mano_aux_escalera_ordenada[2] and mano_aux_escalera_ordenada[2]+1==mano_aux_escalera_ordenada[3] and mano_aux_escalera_ordenada[3]+1==mano_aux_escalera_ordenada[4] and mano_aux_escalera_ordenada[4]+1==14:
					if mano_aux_escalera_color[0]==mano_aux_escalera_color[1] and mano_aux_escalera_color[1]==mano_aux_escalera_color[2] and mano_aux_escalera_color[2]==mano_aux_escalera_color[3] and mano_aux_escalera_color[3]==mano_aux_escalera_color[4]:
						puntaje_aux=8+mano_aux_escalera_ordenada[4]/100
						pass
					pass
				pass
			if puntaje_aux> mejor_puntaje:
				mejor_puntaje=puntaje_aux
				mejor_mano=arre_de_manos[cont][:]
				pass
			pass
		cont+=1
		pass
	#entrega los resultados.
	resultado[0]=mejor_mano[:]
	resultado[1].append(mejor_puntaje)
	return(resultado)
	pass

def BuscarPoker(arre_de_manos):
	cont=0 
	mejor_puntaje=0
	resultado=[]
	resultado.append([])
	resultado.append([])
	mejor_mano=[]
	while cont<(len(arre_de_manos)):
		cont_aux2=0 
		carta_alta=''
		puntaje=0
		pares=0
		puntaje_aux=0
		combinaciones_pares=(list(combinations(arre_de_manos[cont],4)))
		while cont_aux2<len(combinaciones_pares):
			if len(combinaciones_pares[cont_aux2][0])==2 and len(combinaciones_pares[cont_aux2][1])==2 and len(combinaciones_pares[cont_aux2][2])==2 and len(combinaciones_pares[cont_aux2][3])==2:		
				if combinaciones_pares[cont_aux2][0][0]==combinaciones_pares[cont_aux2][1][0]  and combinaciones_pares[cont_aux2][0][0]==combinaciones_pares[cont_aux2][2][0] and combinaciones_pares[cont_aux2][0][0]==combinaciones_pares[cont_aux2][3][0]:
					if puntaje_aux<7 +float(combinaciones_pares[cont_aux2][0][0])/100:
						puntaje_aux= 7 +float(combinaciones_pares[cont_aux2][0][0])/100
						pass
					if combinaciones_pares[cont_aux2][0][0]=='1':
						puntaje_aux=7.14
						pass
					pass
				pass
			if len(combinaciones_pares[cont_aux2][0])==3 and len(combinaciones_pares[cont_aux2][1])==3 and len(combinaciones_pares[cont_aux2][2])==3 and len(combinaciones_pares[cont_aux2][3])==3:
				if combinaciones_pares[cont_aux2][0][0:2]==combinaciones_pares[cont_aux2][1][0:2] and combinaciones_pares[cont_aux2][0][0:2]==combinaciones_pares[cont_aux2][2][0:2] and combinaciones_pares[cont_aux2][0][0:2]==combinaciones_pares[cont_aux2][3][0:2]:
					if puntaje_aux<7 +float(combinaciones_pares[cont_aux2][0][0:2])/100:
						puntaje_aux=7 +float(combinaciones_pares[cont_aux2][0][0:2])/100
						pass
				pass
			cont_aux2+=1
			pass
		if puntaje_aux> mejor_puntaje:
			mejor_puntaje=puntaje_aux
			mejor_mano=arre_de_manos[cont][:]
			pass
		cont+=1
	#entrega los resultados.
	resultado[0]=mejor_mano[:]
	resultado[1].append(mejor_puntaje)
	return(resultado)

	pass

def BuscarFull(arre_de_manos):
	cont=0
	mejor_puntaje=0
	mejor_mano=[]
	resultado=[]
	resultado.append([])
	resultado.append([])
	while cont<(len(arre_de_manos)):
		arre_de_manos_aux=[]
		arre_de_manos_aux.append(arre_de_manos[cont])
		resultado_mano2=0
		trio_afirmativo=0
		par_afirmativo=0
		resultado_mano_aux2=[]
		#El problema es que toma los trios como doble pares. No estA solucionado en doble par porque no es necesario.
		resultado_mano_aux2=BuscarDoblePar(arre_de_manos_aux)					#entrega un arreglo (mano) y un resultado de 0, 2.2,...., 2.14
		if resultado_mano_aux2[1][0]>0:		
			resultado_mano2=resultado_mano_aux2[1][0]
			par_afirmativo=1
			#print(arre_de_manos_aux)
			#print(resultado_mano_aux2)
			pass
		resultado_mano_aux2=[]
		resultado_mano_aux2=BuscarTrio(arre_de_manos_aux)						#entrega un arreglo (mano) y un resultado de 0, 3.2,...., 3.14
		#print(arre_de_manos_aux)
		#print(resultado_mano_aux2)
		if resultado_mano_aux2[1][0]>0:		
			resultado_mano2=resultado_mano_aux2[1][0]
			#print('entro')
			trio_afirmativo=1
		pass

		if trio_afirmativo==1 and par_afirmativo==1 and resultado_mano2>mejor_puntaje:
			mejor_puntaje=6+resultado_mano2-3
			mejor_mano=arre_de_manos[cont]
			#print('entro')
			pass
		cont+=1
		pass

	#entrega los resultados.
	resultado[0]=mejor_mano[:]
	resultado[1].append(mejor_puntaje)
	return(resultado)

	pass

def BuscarColor(arre_de_manos):
	cont=0
	mejor_puntaje=0
	mejor_mano=[]
	resultado=[]
	resultado.append([])
	resultado.append([])
	while cont<(len(arre_de_manos)-1):
		mano_aux_color=[]
		carta_alta_color=0
		for x in range(0,5):
			if len (arre_de_manos[cont][x])==2:
				mano_aux_color.append(arre_de_manos[cont][x][1])
				if carta_alta_color<float(arre_de_manos[cont][x][0]):
					carta_alta_color=float(arre_de_manos[cont][x][0])
					pass
				if arre_de_manos[cont][x][0]=='1':
					carta_alta_color=14
					pass
				pass
			if len (arre_de_manos[cont][x])==3:
				mano_aux_color.append(arre_de_manos[cont][x][2])
				if carta_alta_color<float(arre_de_manos[cont][x][0:2]):
					carta_alta_color=float(arre_de_manos[cont][x][0:2])
					pass
				pass

			
			pass
		
		if mano_aux_color[0]==mano_aux_color[1] and mano_aux_color[1]==mano_aux_color[2] and mano_aux_color[2]==mano_aux_color[3] and mano_aux_color[3]==mano_aux_color[4]:
			if mejor_puntaje<(5+carta_alta_color/100):
				mejor_puntaje=(5+carta_alta_color/100)
				mejor_mano=arre_de_manos[cont][:]
				pass
			pass
		cont+=1
		pass

	#entrega los resultados.
	resultado[0]=mejor_mano[:]
	resultado[1].append(mejor_puntaje)
	return(resultado)

	pass

def BuscarEscalera(arre_de_manos):
	cont=0
	mejor_puntaje=0
	mejor_mano=[]
	resultado=[]
	resultado.append([])
	resultado.append([])
	while cont<(len(arre_de_manos)-1):
		mano_aux_escalera=[]
		puntaje_aux=0
		for x in range(0,5):
			if len(arre_de_manos[cont][x])==2:
				mano_aux_escalera.append(float(arre_de_manos[cont][x][0]))
				pass
			if len(arre_de_manos[cont][x])==3:
				mano_aux_escalera.append(float(arre_de_manos[cont][x][0:2]))
				pass
			pass
		mano_aux_escalera_ordenada=sorted(mano_aux_escalera)
		#print(arre_de_manos)
		#print (arre_de_manos[cont])
		#print (mano_aux_escalera_ordenada)
		if len(mano_aux_escalera_ordenada)==5:
			if mano_aux_escalera_ordenada[0]+1==mano_aux_escalera_ordenada[1] and mano_aux_escalera_ordenada[1]+1==mano_aux_escalera_ordenada[2] and mano_aux_escalera_ordenada[2]+1==mano_aux_escalera_ordenada[3] and mano_aux_escalera_ordenada[3]+1==mano_aux_escalera_ordenada[4]:
				puntaje_aux=4+mano_aux_escalera_ordenada[4]/100
				pass
			if mano_aux_escalera_ordenada[0]==1:
				if mano_aux_escalera_ordenada[1]+1==mano_aux_escalera_ordenada[2] and mano_aux_escalera_ordenada[2]+1==mano_aux_escalera_ordenada[3] and mano_aux_escalera_ordenada[3]+1==mano_aux_escalera_ordenada[4] and mano_aux_escalera_ordenada[4]+1==14:
					puntaje_aux=4+mano_aux_escalera_ordenada[4]/100
					pass
				pass
			if puntaje_aux> mejor_puntaje:
				mejor_puntaje=puntaje_aux
				mejor_mano=arre_de_manos[cont][:]
				pass
			pass
		cont+=1
		pass
	#entrega los resultados.
	resultado[0]=mejor_mano[:]
	resultado[1].append(mejor_puntaje)
	return(resultado)
	pass


def BuscarTrio(arre_de_manos):
	cont=0 
	mejor_puntaje=0
	resultado=[]
	resultado.append([])
	resultado.append([])
	mejor_mano=[]
	while cont<(len(arre_de_manos)):
		cont_aux2=0 
		carta_alta=''
		puntaje=0
		pares=0
		puntaje_aux=0
		combinaciones_pares=(list(combinations(arre_de_manos[cont],3)))
		while cont_aux2<len(combinaciones_pares):
			if len(combinaciones_pares[cont_aux2][0])==2 and len(combinaciones_pares[cont_aux2][1])==2 and len(combinaciones_pares[cont_aux2][2])==2:		
				if combinaciones_pares[cont_aux2][0][0]==combinaciones_pares[cont_aux2][1][0] and combinaciones_pares[cont_aux2][0][0]==combinaciones_pares[cont_aux2][2][0]:
					if puntaje_aux<3 +float(combinaciones_pares[cont_aux2][0][0])/100:
						puntaje_aux= 3 +float(combinaciones_pares[cont_aux2][0][0])/100
						pass
					if combinaciones_pares[cont_aux2][0][0]=='1':
						puntaje_aux=3.14
						pass
					pass
				pass
			if len(combinaciones_pares[cont_aux2][0])==3 and len(combinaciones_pares[cont_aux2][1])==3 and len(combinaciones_pares[cont_aux2][2])==3:
				if combinaciones_pares[cont_aux2][0][0:2]==combinaciones_pares[cont_aux2][1][0:2] and combinaciones_pares[cont_aux2][0][0:2]==combinaciones_pares[cont_aux2][2][0:2]:
					if puntaje_aux<3 +float(combinaciones_pares[cont_aux2][0][0:2])/100:
						puntaje_aux= 3 +float(combinaciones_pares[cont_aux2][0][0:2])/100
						pass
				pass
			cont_aux2+=1
			pass
		if puntaje_aux> mejor_puntaje:
			mejor_puntaje=puntaje_aux
			mejor_mano=arre_de_manos[cont][:]
			pass
		cont+=1

		pass
	#entrega los resultados.
	resultado[0]=mejor_mano[:]
	resultado[1].append(mejor_puntaje)
	return(resultado)

	pass

def BuscarDoblePar(arre_de_manos):
	cont=0 
	mejor_puntaje=0
	resultado=[]
	resultado.append([])
	resultado.append([])
	mejor_mano=[]
	#esta funcion distingue trio, pero no poker
	while cont<(len(arre_de_manos)):
		cont_aux2=0 
		carta_alta=''
		puntaje=0
		pares=0
		puntaje_aux=0
		combinaciones_pares=(list(combinations(arre_de_manos[cont],2)))
		while cont_aux2<len(combinaciones_pares):
			if len(combinaciones_pares[cont_aux2][0])==2 and len(combinaciones_pares[cont_aux2][1])==2:		
				if combinaciones_pares[cont_aux2][0][0]==combinaciones_pares[cont_aux2][1][0]:
					pares+=1
					if puntaje_aux==2 +float(combinaciones_pares[cont_aux2][0][0])/100:
						pares-=1
						pass
					if puntaje_aux<2 +float(combinaciones_pares[cont_aux2][0][0])/100:
						puntaje_aux= 2 +float(combinaciones_pares[cont_aux2][0][0])/100
						pass
					if combinaciones_pares[cont_aux2][0][0]=='1':
						puntaje_aux=2.14
						pass
					pass
				pass
			if len(combinaciones_pares[cont_aux2][0])==3 and len(combinaciones_pares[cont_aux2][1])==3:
				if combinaciones_pares[cont_aux2][0][0:2]==combinaciones_pares[cont_aux2][1][0:2]:
					pares=pares+1
					if puntaje_aux<2 +float(combinaciones_pares[cont_aux2][0][0:2])/100:
						puntaje_aux= 2 +float(combinaciones_pares[cont_aux2][0][0:2])/100
						pass
				pass
			cont_aux2+=1
			pass
		if pares<2:
			puntaje_aux=0
			pass
		if puntaje_aux> mejor_puntaje:
			mejor_puntaje=puntaje_aux
			mejor_mano=arre_de_manos[cont][:]
			pass
		cont+=1

		pass
	#entrega los resultados.
	resultado[0]=mejor_mano[:]
	resultado[1].append(mejor_puntaje)
	return(resultado)
	pass

def BuscarPar(arre_de_manos):
	cont=0
	resultado=[]
	resultado.append([])
	resultado.append([])
	mejor_mano=[]
	mejor_puntaje=0
	while cont<(len(arre_de_manos)-1):
		cont_aux2=0
		carta_alta=''
		puntaje=0
		while cont_aux2<(len(arre_de_manos[cont])-1):
			carta_alta_aux=''
			puntaje_aux=0
			cont_aux21=cont_aux2+1
			while cont_aux21<(len(arre_de_manos[cont])):
				if len(arre_de_manos[cont][cont_aux2])==2 and len(arre_de_manos[cont][cont_aux21])==2:		
					if arre_de_manos[cont][cont_aux2][0]==arre_de_manos[cont][cont_aux21][0]:
						puntaje_aux=1+float(arre_de_manos[cont][cont_aux2][0])/100
						if arre_de_manos[cont][cont_aux2][0]=='1':
							puntaje_aux=1.14
							pass
						pass
					pass
				if len(arre_de_manos[cont][cont_aux2])==3 and len(arre_de_manos[cont][cont_aux21])==3:
					if arre_de_manos[cont][cont_aux2][0:2]==arre_de_manos[cont][cont_aux21][0:2]:
						puntaje_aux=1+float(arre_de_manos[cont][cont_aux2][0:2])/100
					pass

				cont_aux21+=1
				pass
			if puntaje_aux>puntaje:
				puntaje=puntaje_aux
				pass
			cont_aux2+=1
		if puntaje> mejor_puntaje:
			mejor_puntaje=puntaje
			mejor_mano=arre_de_manos[cont][:]
			pass
		cont+=1
		pass
	resultado[0]=mejor_mano[:]
	resultado[1].append(mejor_puntaje)
	return(resultado)
	pass

def BuscarCartaAlta(arre_de_manos):
	cont=0
	resultado=[]
	resultado.append([])
	resultado.append([])
	mejor_mano=[]
	mejor_puntaje=0
	while cont<(len(arre_de_manos)-1):
		cont_aux2=0
		carta_alta=''
		puntaje=0
		while cont_aux2<(len(arre_de_manos[cont])):
			carta_alta_aux=''
			puntaje_aux=0
			if arre_de_manos[cont][cont_aux2]=='2c' or arre_de_manos[cont][cont_aux2]=='2d' or arre_de_manos[cont][cont_aux2]=='2p' or arre_de_manos[cont][cont_aux2]=='2t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.02
				pass
			if arre_de_manos[cont][cont_aux2]=='3c' or arre_de_manos[cont][cont_aux2]=='3d' or arre_de_manos[cont][cont_aux2]=='3p' or arre_de_manos[cont][cont_aux2]=='3t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.03
				pass
			if arre_de_manos[cont][cont_aux2]=='4c' or arre_de_manos[cont][cont_aux2]=='4d' or arre_de_manos[cont][cont_aux2]=='4p' or arre_de_manos[cont][cont_aux2]=='4t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.04
				pass
			if arre_de_manos[cont][cont_aux2]=='5c' or arre_de_manos[cont][cont_aux2]=='5d' or arre_de_manos[cont][cont_aux2]=='5p' or arre_de_manos[cont][cont_aux2]=='5t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.05
				pass
			if arre_de_manos[cont][cont_aux2]=='6c' or arre_de_manos[cont][cont_aux2]=='6d' or arre_de_manos[cont][cont_aux2]=='6p' or arre_de_manos[cont][cont_aux2]=='6t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.06
				pass
			if arre_de_manos[cont][cont_aux2]=='7c' or arre_de_manos[cont][cont_aux2]=='7d' or arre_de_manos[cont][cont_aux2]=='7p' or arre_de_manos[cont][cont_aux2]=='7t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.07
				pass
			if arre_de_manos[cont][cont_aux2]=='8c' or arre_de_manos[cont][cont_aux2]=='8d' or arre_de_manos[cont][cont_aux2]=='8p' or arre_de_manos[cont][cont_aux2]=='8t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.08
				pass
			if arre_de_manos[cont][cont_aux2]=='9c' or arre_de_manos[cont][cont_aux2]=='9d' or arre_de_manos[cont][cont_aux2]=='9p' or arre_de_manos[cont][cont_aux2]=='9t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.09
				pass
			if arre_de_manos[cont][cont_aux2]=='10c' or arre_de_manos[cont][cont_aux2]=='10d' or arre_de_manos[cont][cont_aux2]=='10p' or arre_de_manos[cont][cont_aux2]=='10t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.10
				pass
			if arre_de_manos[cont][cont_aux2]=='11c' or arre_de_manos[cont][cont_aux2]=='11d' or arre_de_manos[cont][cont_aux2]=='11p' or arre_de_manos[cont][cont_aux2]=='11t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.11
				pass
			if arre_de_manos[cont][cont_aux2]=='12c' or arre_de_manos[cont][cont_aux2]=='12d' or arre_de_manos[cont][cont_aux2]=='12p' or arre_de_manos[cont][cont_aux2]=='12t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.12
				pass
			if arre_de_manos[cont][cont_aux2]=='13c' or arre_de_manos[cont][cont_aux2]=='13d' or arre_de_manos[cont][cont_aux2]=='13p' or arre_de_manos[cont][cont_aux2]=='13t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.13
				pass
			if arre_de_manos[cont][cont_aux2]=='1c' or arre_de_manos[cont][cont_aux2]=='1d' or arre_de_manos[cont][cont_aux2]=='1p' or arre_de_manos[cont][cont_aux2]=='1t':
				carta_alta_aux=arre_de_manos[cont][cont_aux2]
				puntaje_aux=0.14
				pass
			if puntaje_aux>puntaje:
				puntaje=puntaje_aux
				carta_alta=carta_alta_aux[:]
				pass
			cont_aux2+=1
		if puntaje> mejor_puntaje:
			mejor_puntaje=puntaje
			mejor_mano=arre_de_manos[cont][:]
			pass
		cont+=1
		pass
	resultado[0]=mejor_mano[:]
	resultado[1].append(mejor_puntaje)
	return(resultado)
	pass

def BuscarMejorMano(arre_de_manos):
	resultado_mano=[[],[0]]
	

	resultado_mano_aux=BuscarCartaAlta(arre_de_manos)					#entrega un arreglo (mano) y un resultado de 0, 0.02,...., 0.14
	if resultado_mano_aux[1][0]>resultado_mano[1][0]:
		resultado_mano=resultado_mano_aux[:] 				
		pass
	resultado_mano_aux=BuscarPar(arre_de_manos)							#entrega un arreglo (mano) y un resultado de 0, 1.2,...., 1.14
	if resultado_mano_aux[1][0]>resultado_mano[1][0]:					
		resultado_mano=resultado_mano_aux[:]
		pass
	resultado_mano_aux=BuscarDoblePar(arre_de_manos)					#entrega un arreglo (mano) y un resultado de 0, 2.2,...., 2.14
	if resultado_mano_aux[1][0]>resultado_mano[1][0]:		
		resultado_mano=resultado_mano_aux[:]
		pass
	resultado_mano_aux=BuscarTrio(arre_de_manos)						#entrega un arreglo (mano) y un resultado de 0, 3.2,...., 3.14
	if resultado_mano_aux[1][0]>resultado_mano[1][0]:		
		resultado_mano=resultado_mano_aux[:]
		pass		
	resultado_mano_aux=BuscarEscalera(arre_de_manos)					#entrega un arreglo (mano) y un resultado de 0, 4.2,...., 4.14
	if resultado_mano_aux[1][0]>resultado_mano[1][0]:		
		resultado_mano=resultado_mano_aux[:]
		pass
	resultado_mano_aux=BuscarColor(arre_de_manos)						#entrega un arreglo (mano) y un resultado de 0, 5.2,...., 5.14
	if resultado_mano_aux[1][0]>resultado_mano[1][0]:		
		resultado_mano=resultado_mano_aux[:]
		pass
	resultado_mano_aux=BuscarFull(arre_de_manos)						#entrega un arreglo (mano) y un resultado de 0, 6.2,...., 6.14
	if resultado_mano_aux[1][0]>resultado_mano[1][0]:		
		resultado_mano=resultado_mano_aux[:]
		pass
	resultado_mano_aux=BuscarPoker(arre_de_manos)						#entrega un arreglo (mano) y un resultado de 0, 7.2,...., 7.14
	if resultado_mano_aux[1][0]>resultado_mano[1][0]:		
		resultado_mano=resultado_mano_aux[:]
		pass
	resultado_mano_aux=BuscarEscaleraColor(arre_de_manos)				#entrega un arreglo (mano) y un resultado de 0, 8.2,...., 8.14
	if resultado_mano_aux[1][0]>resultado_mano[1][0]:		
		resultado_mano=resultado_mano_aux[:]
		pass
	"""	
	if BuscarEscaleraReal(arre_de_manos)[1][0]>resultado_mano[1][0]:
		resultado_mano=BuscarEscaleraReal(arre_de_manos)			#entrega un arreglo (mano) y un resultado de 0, 9
		pass
	"""

	return (resultado_mano)	
	pass



def Probabilidades(mi_mano, flot_aux,numero_jugadores):
	#seteo inicial leido de la jugada.
	#mi_mano=combinacionaes_mi_mano[cont_mano_inicial][:]
	#mi_mano=['2d','4t']
	#flot_aux=[]
	#numero_jugadores=1

	#Saco del maso las cartas de mi mano.
	#Este es el cuerpo de Monte Carlo
	loop=1
	last_time = time.time()
	ganados=0
	perdidos=0
	if 	len(mi_mano)>0:
		for x in range(1,500):
			#Definimos el maso
			maso=['1c','2c','3c','4c','5c','6c','7c','8c','9c','10c','11c','12c','13c',
			'1d','2d','3d','4d','5d','6d','7d','8d','9d','10d','11d','12d','13d',
			'1p','2p','3p','4p','5p','6p','7p','8p','9p','10p','11p','12p','13p',
			'1t','2t','3t','4t','5t','6t','7t','8t','9t','10t','11t','12t','13t']
			#sacamos mis cartas
			
			cont=0
			while cont <= len(mi_mano)-1:
				maso.pop(maso.index(mi_mano[cont]))
				cont=cont+1
			#definimos los arreglos de los demas jugadores y del FLOT
			flot=[]
			flot=flot_aux[:]
			mano_jugadores=[]
			#Tiro los dados y Saco del maso las cartas del FLOT
			cont=0
				#saco las cartas del flot ya conocidas
			while cont <= len(flot)-1:
				maso.pop(maso.index(flot[cont]))
				cont+=1

				#genero mas cartas y las saco
			while len(flot) <= 4:
				carta=''
				carta=maso[np.random.randint(1,len(maso),size=1)[0]]
				flot.append(carta)
				maso.pop(maso.index(carta))
				pass
			#Tiro los dados y saco del maso las cartas de los Jugadores
			cont=0
			while cont < numero_jugadores:
				mano_jugadores.append([])
				cont_aux=0
				while cont_aux<2:
					carta=''
					carta=maso[np.random.randint(1,len(maso),size=1)[0]]
					mano_jugadores[cont].append(carta)
					maso.pop(maso.index(carta))
					cont_aux+=1
					pass
				
				cont+=1
				pass

			#imprimimos las variables del juego.
			"""
			print('------------------------------------------')
			print ('van {} vueltas'.format(loop))
			print(mi_mano)
			print(mano_jugadores)
			print(flot)
			"""
			loop+=1
			#Buscamos los resultados
			comb3=(list(combinations(flot,3)))
			comb4=(list(combinations(flot,4)))	
			
			
			#hay que convertir la lista en arreglo
			cont=0
			comb3_aux=[]
			while cont<len(comb3):
				cont_aux2=0
				comb3_aux.append([])
				while cont_aux2<(len(comb3[cont])):
					comb3_aux[cont].append(comb3[cont][cont_aux2])
					cont_aux2+=1
					pass
				cont+=1
				pass
			cont=0
			comb4_aux=[]
			while cont<len(comb4):
				cont_aux2=0
				comb4_aux.append([])
				while cont_aux2<(len(comb4[cont])):
					comb4_aux[cont].append(comb4[cont][cont_aux2])
					cont_aux2+=1
					pass
				cont+=1
				pass
			
			comb3=comb3_aux[:]
			comb4=comb4_aux[:]

			#primero con mi mano
			cont=0
			mis_manos=[]
			while cont< len(comb3):
				mis_manos.append(mi_mano+comb3[cont])	
				cont+=1
				pass
			cont=0
			mi_mejor_mano_aux0=[]
			mi_mejor_mano_aux0.append(mi_mano[0])
			mi_mejor_mano_aux1=[]
			mi_mejor_mano_aux1.append(mi_mano[1])
			while cont<len(comb4):
				mis_manos.append(mi_mejor_mano_aux0+comb4[cont])
				mis_manos.append(mi_mejor_mano_aux1+comb4[cont])
				cont+=1
				pass
			mi_mejor_mano=BuscarMejorMano(mis_manos) #este arreglo tiene la mano y la calificacion
			#print ('Mi mejor Manos es {}'.format(mi_mejor_mano))
			pass

			#ahora con cada jugador, VEO INMEDIATAMENTE SI GANO
			gane=1
			cont_aux2=0
			while cont_aux2<numero_jugadores:
				manos_jugador=[]
				#primero genero las manos con 3 cartas del flot
				while cont< len(comb3):
					manos_jugador.append(mano_jugadores[cont_aux2]+comb3[cont])	
					cont+=1
					pass
				#segundo las con 
				cont=0
				manos_jugador_aux0=[]
				manos_jugador_aux0.append(mano_jugadores[cont_aux2][0])
				manos_jugador_aux1=[]
				manos_jugador_aux1.append(mano_jugadores[cont_aux2][1])
				while cont<len(comb4):
					manos_jugador.append(manos_jugador_aux0+comb4[cont])
					manos_jugador.append(manos_jugador_aux1+comb4[cont])
					cont+=1
					pass
				jugador_mejor_mano=BuscarMejorMano(manos_jugador) #este arreglo tiene la mano y la calificacion
				#print ('La mejor Mano del Jugador {} es {}'.format((cont_aux2+1), jugador_mejor_mano))
				#print('')
				
				if jugador_mejor_mano[1][0]>mi_mejor_mano[1][0]:
					gane=0
					pass

				cont_aux2+=1
				pass

			if gane==1:
				ganados+=1
				#print ('GANE, MIERDA!!!')
			else :
				perdidos+=1
				#print ('Perdi y la CTM')
				
		#print('Loop {} de {}, tomo {} segundos'. format(cont_mano_inicial,len(combinacionaes_mi_mano), time.time()-last_time))
		#print('Probabilidad de victoria:{}'.format(float(ganados)/(float(ganados)+float(perdidos))))
		return(float(ganados)/(float(ganados)+float(perdidos)))


		resultados_mi_mano_inicial.append([])
		resultados_mi_mano_inicial[cont_mano_inicial].append(mi_mano)
		resultados_mi_mano_inicial[cont_mano_inicial].append([])
		resultados_mi_mano_inicial[cont_mano_inicial][1]=[float(ganados)/(float(ganados)+float(perdidos))]
		
		pass
	pass
	