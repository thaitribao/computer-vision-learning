from PIL import Image
from pylab import * 
from numpy import *
import matplotlib.pyplot as plt
import imtools

# Enable plt.ion() to allow interactive mode. Useful for ginput(x)
# plt.ion()

im = array(Image.open('.jpg').convert("L"))
imshow(im, cmap='gray')
show()
im2,cdf = imtools.histeq(im)
imshow(im2, cmap='gray')
show()






