#!/usr/bin/env python3

from time import sleep
from neopixel import *
from lookup import LOOKUP
import random
from colors import lighter, darker

RAIN_COLOR = Color(0,100,152)
RAIN_TUPLE = (0,100,152)

GRAD = [
    Color(17, 147, 255),
    Color(40, 157, 255),
    Color(76, 173, 255),
    Color(81, 175, 255),
    Color(86, 176, 255),
    Color(178, 204, 255),
    Color(178, 220, 255),
    Color(191, 226, 255),
]

# from pixel_rain import start_rain, end_rain

should_rain = True

def end_rain():
    should_rain = False
    return

def start_rain(strip,timing=40):
    blackOut(strip)
    rain(timing,strip)
    blackOut(strip)
    return



def blackOut(strip):
    """Turn All pixels to Black."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()


class Position(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def index(self) -> int:
    key = str(self.x)+','+str(self.y)
    pixel_index = int(LOOKUP[key])
    return pixel_index

  def last(self):
    last_y = self.y - 1
    if last_y < 0:
        last_y = 0

    return Position(self.x,last_y)

  def lastLast(self):
    last_y = self.y - 2
    if last_y < 0:
        last_y = 0
    return Position(self.x,last_y)




class Pixel(object):
  def __init__(self, color, position, speed, lifetime=1):
    self.color = color
    self.position = position
    self.speed = speed
    self.lifetime = int((lifetime * 16 - 1))
    self.age = 0

  def grow_older(self) -> bool:
    self.colorForAge()
    new_age = self.age + 1
    self.age = new_age
    if new_age > self.lifetime:
        return False
    else:
        return True

  def colorForAge(self):
      def findColorForYPos(y):
         idx = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7][y]
         color = GRAD[idx]
         return color
      new_color = findColorForYPos(self.age)
      self.color = new_color

  # decrements the positon.y by 1 and aging in the process
  def lower(self) -> bool:
    new_y = self.position.y + 1
    if new_y > 15:
        new_y = 15
    new_pos = Position(self.position.x,new_y)

    self.position = new_pos
    # aging
    return self.grow_older()

  def render(self,strip):
    idx = self.position.index()
    strip.setPixelColor(idx, self.color)

  def blackout(self,strip):
    if self.age > 0:
        idx = self.position.last().index()
        strip.setPixelColor(idx, Color(0,0,0))

  # def trail(self,strip):
  #   lastLast_pos_idx = self.position.lastLast().index()
  #   strip.setPixelColor(lastLast_pos_idx, Color(127,127,127))

  #   last_pos_idx = self.position.last().index()
  #   strip.setPixelColor(last_pos_idx, Color(255,0,0))


def rain(timing,strip):
    pixels = []
    pixels.append(generate_pixel())
    rain_loop(pixels,strip,timing)

def rain_loop(pixels,strip,timing):
    dead = []
    speed = 1
    raindrops = 512
    while raindrops > 0:

        pixels,dead = rain_fall(pixels,dead,strip,speed)
        raindrops -= 1

        speed += 1
        if speed == 4:
            speed = 1

        sleep(timing/1000.0)
    return

def rain_fall(pixels,dead,strip,speed):
    # pob of 1/5 to make a new rain drop
    pixels = add_rain_drop(pixels)

    # handle the dead
    for p in dead:
        idx = p.position.index()
        strip.setPixelColor(idx, Color(0,0,0))
    dead = []

    # prepare the fallen, and new dead
    fallen_pixels = []
    dead_pixels = []

    for p in pixels:
        if p.speed <= speed:
            p.blackout(strip)
            p.render(strip)
            lower_result = p.lower()
            if lower_result:
                fallen_pixels.append(p)
            else:
                dead_pixels.append(p)
        else:
            fallen_pixels.append(p)
    strip.show()

    return fallen_pixels,dead_pixels


def add_rain_drop(pixels):
    new_drop = random.randint(0,5)
    if new_drop <= 1:
        pixels.append(generate_pixel())
        return pixels
    else:
        return pixels

def generate_x(intenisty=16) -> int:
    potentials = [ random.randint(0,15) for i in range(intenisty) ]
    r_idx = random.randint(0,(len(potentials) - 1))
    return potentials[r_idx]

def rgb_to_color(rgb) -> Color:
    return Color(rgb[0], rgb[1], rgb[2])

def generate_color() -> Color:
    red_rgb = (255,0,0)
    lightened = lighter(red_rgb)
    return rgb_to_color(lightened)

def generate_pixel() -> Pixel:
    rand_x = generate_x()
    color = generate_color()
    return Pixel(color,Position(rand_x,0),1)









