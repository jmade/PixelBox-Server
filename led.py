#!/usr/bin/env python3

# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import os
from time import sleep
from PIL import Image
from neopixel import *
from lookup import LOOKUP

# LOOKUP = {'1,0': '14', '14,11': '190', '5,9': '149', '4,2': '43', '4,14': '235', '6,4': '73', '14,8': '129', '12,0': '3', '10,13': '218', '11,7': '123', '15,0': '0', '12,3': '60', '10,4': '69', '1,10': '174', '13,14': '226', '0,2': '47', '10,6': '101', '10,9': '154', '13,9': '157', '3,2': '44', '11,14': '228', '11,10': '164', '13,0': '2', '2,10': '173', '12,1': '28', '7,0': '8', '8,9': '152', '11,4': '68', '3,8': '140', '6,5': '86', '9,14': '230', '8,12': '199', '5,15': '245', '8,13': '216', '15,13': '223', '1,3': '49', '5,5': '85', '13,15': '253', '8,7': '120', '6,11': '182', '12,13': '220', '5,6': '106', '11,15': '251', '12,11': '188', '0,10': '175', '8,8': '135', '1,1': '17', '15,5': '95', '0,0': '15', '12,15': '252', '2,13': '210', '14,15': '254', '15,12': '192', '15,1': '31', '9,6': '102', '3,1': '19', '10,15': '250', '7,2': '40', '8,5': '88', '15,9': '159', '2,11': '178', '13,5': '93', '7,3': '55', '3,9': '147', '11,12': '196', '6,1': '22', '8,11': '184', '7,1': '23', '10,11': '186', '14,5': '94', '14,0': '1', '11,9': '155', '15,7': '127', '15,11': '191', '0,8': '143', '0,14': '239', '14,9': '158', '14,10': '161', '0,11': '176', '1,4': '78', '10,12': '197', '8,10': '167', '5,2': '42', '0,5': '80', '11,5': '91', '1,7': '113', '6,0': '9', '13,8': '130', '6,10': '169', '0,12': '207', '10,7': '122', '14,6': '97', '1,15': '241', '1,6': '110', '2,6': '109', '0,3': '48', '4,9': '148', '13,13': '221', '15,6': '96', '2,12': '205', '9,5': '89', '12,14': '227', '14,13': '222', '13,3': '61', '13,6': '98', '0,7': '112', '13,11': '189', '1,9': '145', '6,3': '54', '4,4': '75', '2,8': '141', '9,10': '166', '1,12': '206', '8,15': '248', '5,14': '234', '5,0': '10', '3,12': '204', '5,13': '213', '2,9': '146', '12,4': '67', '9,15': '249', '3,14': '236', '11,11': '187', '15,2': '32', '7,15': '247', '8,1': '24', '15,10': '160', '7,6': '104', '2,15': '242', '3,0': '12', '9,0': '6', '10,14': '229', '2,4': '77', '8,2': '39', '6,6': '105', '7,8': '136', '10,2': '37', '3,5': '83', '14,14': '225', '10,5': '90', '5,10': '170', '1,11': '177', '9,3': '57', '4,10': '171', '5,12': '202', '10,8': '133', '13,4': '66', '13,12': '194', '3,6': '108', '5,4': '74', '15,15': '255', '1,14': '238', '5,3': '53', '7,14': '232', '5,8': '138', '9,2': '38', '4,1': '20', '4,7': '116', '8,6': '103', '8,14': '231', '11,1': '27', '12,2': '35', '10,3': '58', '4,5': '84', '0,13': '208', '8,3': '56', '1,5': '81', '10,0': '5', '11,13': '219', '12,9': '156', '9,8': '134', '2,5': '82', '5,7': '117', '5,1': '21', '2,3': '50', '0,4': '79', '8,0': '7', '13,2': '34', '0,15': '240', '9,12': '198', '1,2': '46', '14,3': '62', '4,0': '11', '6,8': '137', '2,2': '45', '0,6': '111', '2,7': '114', '11,2': '36', '9,1': '25', '7,9': '151', '15,4': '64', '0,1': '16', '13,7': '125', '6,15': '246', '7,13': '215', '4,11': '180', '13,1': '29', '11,6': '100', '9,11': '185', '0,9': '144', '4,6': '107', '11,0': '4', '4,13': '212', '4,8': '139', '11,8': '132', '6,13': '214', '12,5': '92', '9,13': '217', '12,8': '131', '12,6': '99', '7,10': '168', '3,13': '211', '9,4': '70', '10,10': '165', '6,7': '118', '15,14': '224', '4,12': '203', '14,12': '193', '14,4': '65', '7,11': '183', '2,14': '237', '1,13': '209', '2,0': '13', '3,3': '51', '5,11': '181', '15,3': '63', '3,15': '243', '9,9': '153', '6,2': '41', '15,8': '128', '3,7': '115', '11,3': '59', '3,4': '76', '12,7': '124', '7,5': '87', '8,4': '71', '14,7': '126', '14,2': '33', '9,7': '121', '7,7': '119', '6,14': '233', '3,10': '172', '4,15': '244', '4,3': '52', '2,1': '18', '12,12': '195', '7,12': '200', '6,12': '201', '13,10': '162', '10,1': '26', '14,1': '30', '1,8': '142', '12,10': '163', '6,9': '150', '3,11': '179', '7,4': '72'}

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

# Define functions which animate LEDs in various ways.
def blackOut(strip):
    """Turn All pixels to Black."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def runDemo(strip):
    print ('Press Ctrl-C to quit.')
    try:

        while True:
            print ('Color wipe animations.')
            colorWipe(strip, Color(255, 0, 0),10)  # Red wipe
            colorWipe(strip, Color(0, 255, 0),5)  # Blue wipe
            colorWipe(strip, Color(0, 0, 255),10)  # Green wipe
            print ('Theater chase animations.')
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            theaterChase(strip, Color(127,   0,   0))  # Red theater chase
            theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
            print ('Rainbow animations.')
            rainbow(strip)
            rainbowCycle(strip)
            theaterChaseRainbow(strip)

    except KeyboardInterrupt:
        blackOut(strip)





def extractColor(data:dict,x:int,y:int):
    key = str(x)+','+str(y)
    val = data[key]
    c = val.split(',')
    r = int(c[0])
    g = int(c[1])
    b = int(c[2])
    return Color(r,g,b)

def fix_data(data):
    new = {}
    for item in data:
        key = next(iter(item))
        new[key] = item[key]
    return new





def updatePixel(strip,data):
    key = next(iter(data))
    pixel_index = int(LOOKUP[key])

    i = key.split(',')
    x = int(i[0])
    y = int(i[1])
    color = extractColor(data,x,y)
    strip.setPixelColor(pixel_index, color)
    strip.show()



def drawData(strip,data):
    data = fix_data(data)
    idx = 0
    for y in range(16): # ->
        if y%2: # odd
            for x in range(16):
                color = extractColor(data,x,y)
                strip.setPixelColor(idx, color)
                idx += 1
        else: # even
            idx += 16 # buffer the index for reverse <-
            for x in range(16):
                idx -= 1
                color = extractColor(data,x,y)
                strip.setPixelColor(idx, color)
            idx += 16 # restore index
    strip.show()



# Image Showing.

def showImage(strip,image_name):
    loc = '/home/pi/pixelbox/img/sprites/'+image_name
    im = Image.open(loc)
    rgb_im = im.convert('RGB')

    idx = 0
    for y in range(16): # ->
        if y%2: # odd
            for x in range(16):
                r, g, b = rgb_im.getpixel((x, y))
                strip.setPixelColor(idx, Color(r, g, b))
                idx += 1
        else: # even
            idx += 16 # buffer the index for reverse <-
            for x in range(16):
                idx -= 1
                r, g, b = rgb_im.getpixel((x, y))
                strip.setPixelColor(idx, Color(r, g, b))
            idx += 16 # restore index
    strip.show()


def imageLoop(strip):
    images = getImageNames()
    counter = 5
    while counter > 0:
        for image_name in images:
            showImage(strip,image_name)
            sleep(15.0)
        counter -= 1

    blackOut(strip)

def getImageNames():
    image_names = []
    for root, dirs, files in os.walk("/home/pi/pixelbox/img/sprites/"): 
        for filename in files:
            image_names.append(filename)
    return image_names




