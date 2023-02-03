# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
from unidecode import unidecode

img=Image.open('local-filename.jpg')
#print image_to_string(Image.open('local-filename.png'))
print (unidecode(pytesseract.image_to_string(img)))