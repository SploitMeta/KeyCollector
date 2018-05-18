from PIL import Image
import pytesseract
import re 

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def toText(image):
	loadedImage = Image.open(image)
	outputText = pytesseract.image_to_string(loadedImage, lang = 'eng')
	return outputText

def getKey(post):
    code = re.findall(r'[a-zA-Z0-9?]+-[a-zA-Z0-9?]+-[a-zA-Z0-9?]+', post)  
    return code



inputPicture="7.png"
textFromPicture = toText(inputPicture)
keys= getKey(textFromPicture)
print(keys)
