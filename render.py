#!/usr/bin/env python3

# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import os
from time import sleep
from PIL import Image
from neopixel import *

def imageLoop(strip):
    images = getImageNames()
    try:
        while True:
            for image_name in images:
                showImage(strip,image_name)
                sleep(15.0)
    except KeyboardInterrupt:
        blackOut(strip)


def motion(strip):
    base = '/home/pi/pixelbox/img/drip/'
    image_names = []
    for root, dirs, files in os.walk(base):
        for filename in files:
            image_names.append(filename)

    for image_name in sorted(image_names):
        showImage(strip,image_name,base)
        sleep(0.1)


# Image Showing.
def showImage(strip,image_name,base='/home/pi/img/'):
    loc = base+image_name
    im = Image.open(loc)
    rgb_im = im.convert('RGB')

    idx = 0
    for y in range(16): # ->
        if y%2: # odd
            for x in range(16):
                r, g, b = rgb_im.getpixel((x, y))
                strip.setPixelColor(idx, Color(g, r, b))
                idx += 1
        else: # even
            idx += 16 # buffer the index for reverse <-
            for x in range(16):
                idx -= 1
                r, g, b = rgb_im.getpixel((x, y))
                strip.setPixelColor(idx, Color(g, r, b))
            idx += 16 # restore index
    strip.show()


def getImageNames():
    image_names = []
    for root, dirs, files in os.walk("/home/pi/pixelbox/img"): 
        for filename in files:
            image_names.append(filename)
    return image_names




