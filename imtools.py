import os
from numpy import * 
from pylab import *

def get_imlist(path): 
    """ Returns a list of filenames for 
    all jpg images in a directory. """
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

def imresize(im, size): 
    """Resize an image array using PIL"""
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

def histeq(im, nbr_bins=256):
    """Histogram equalization of grayscale image. """

    #get image histogram
    imhist,bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum() #cummulative distribution function
    cdf = 255 * cdf/cdf[-1] #normalize

    #use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(), bins[:-1], cdf)

    return im2.reshape(im.shape), cdf

def compute_average(imlist):
    """Compute the average of a list of images"""

    #open first image and make into array of type float
    averageim = array(Image.open(imlist[0]), 'f')

    for imName in imList[1:]:
        try:
            averageim += array(Image.open(imName))
        except:
            print imname + '...skipped'
    averageim /= len(imlist)
    
    #convert average back to uint8
    return array(averageim, 'uint8')
