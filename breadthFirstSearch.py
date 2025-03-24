import os
import numpy as np
from PIL import Image

nolliPATH = r"C:\Users\hyche\Desktop\AR5802 Options 2\Pix2Pix\breadthFirstSearch\testMaps\testMap2.png"
#poiPATH = 
outputFolder = r"C:\Users\hyche\Desktop\AR5802 Options 2\Pix2Pix\breadthFirstSearch\outputs"


# create function to convert greyscale image to bitmap
def bitmap(path):
    img = Image.open(path)
    img_array = img.convert('1')
    img_array = np.array(img_array)
    return(img_array.flatten())


walkable = bitmap(nolliPATH)
print(walkable   )