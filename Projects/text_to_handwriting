#install pywhatkit first
pip install pywhatkit
#for installing cv2 
pip install opencv-python

#Code starts from here
import pywhatkit as kit
import cv2
kit.text_to_handwriting('Well... What??', save_to='texttohandwriting.png')
img = cv2.imread('texttohandwriting.png')
cv2.imshow('Text to Handwriting',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
