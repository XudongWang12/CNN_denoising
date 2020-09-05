#import tesserocr
import pytesseract
from PIL import Image
image=Image.open('qx.jpg')
 
#image.show()
#test = tesserocr.image_to_text(image)
test = pytesseract.image_to_string(image, lang='chi_sim+eng')
with open('data.txt','w',encoding='utf-8') as f:
    f.write(test)
