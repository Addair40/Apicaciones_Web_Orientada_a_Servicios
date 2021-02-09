from PIL import Image 
import pytesseract 
from googletrans import Translator

img = Image.open('image.jpg')
result = pytesseract.image_to_string(img)
print(result)

p = Translator()
p_translated = p.translate(result, dest='spanish')
translated = str(p_translated.text)
print(translated)

