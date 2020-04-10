import cv2
import pytesseract as pts
import enchant
from PIL import Image
import os


def checkFormat(img):
    if not img.endswith('.tiff'):
        image = Image.open(img)
        name, ext = os.path.splitext(img)
        image.save('{}.tiff'.format(name))
        img = "{}.tiff".format(name)
    return img

def resize(img, hight , width):

    img = cv2.imread(img)
    dim = (int(hight), int(width))
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return img

def Threshold(img):

    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU  )[1] #+cv2.THRESH_BINARY_INV 
    return thresh

def showImg(img):
    cv2.imshow("original", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



def loadData(img):

    data = pts.image_to_string(img, lang='eng', config='--psm 6')

    words = data.split()

    eng = enchant.Dict("en_US")
    for word in words:
        if not eng.check(word):
            #words.append(eng.suggest(word)[0])
            words.remove(word)


    text = ' '.join(words)

    return text.lower()





