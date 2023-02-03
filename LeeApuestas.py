from PIL import Image
import nltk, webbrowser, csv, time, urllib, urllib2
import webbrowser, requests
from urllib import urlopen
import  pytesseract
import cv2, time
import numpy as np

def TextoApuesta(imagen):
	#imagen
	image_gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('local-filename.jpg', image_gray)
	img = Image.open('local-filename.jpg').convert('L')
	ret,img = cv2.threshold(np.array(img), 125, 255, cv2.THRESH_BINARY)

	# Older versions of pytesseract need a pillow image
	# Convert back if needed
	img = Image.fromarray(img.astype(np.uint8))
	try:
		texto = pytesseract.image_to_string(img).replace(',','.').replace(' ','').replace('o','0').replace('US$','').replace('-','').replace('\n','').replace('Z','2').replace('S','5')
		pass
	except :
		texto = 0
		pass
	return(texto)
pass