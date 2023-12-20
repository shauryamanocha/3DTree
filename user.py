import board
import neopixel

from tree import Tree
from led import Led
import math
import numpy as np


class User():
    def __init__(self):
        print("User Init")
        self.NUM_LEDS = 250
        self.t = 0
        self.np = neopixel.NeoPixel(board.D18,250,pixel_order = neopixel.RGB,auto_write = False)
        leds = []

        with open('positions.csv', 'r') as csvfile:
            for line in csvfile:
                row = line.split(",")
                leds.append(Led(float(row[1]), float(row[2]), float(row[3])))

        self.tree = Tree(leds=leds)

    def wheel(self,pos):
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b)

    def repeat(self):
        self.color_wheel()
        #self.color_by_angle()
        #self.seizure()
        #self.stripe()
        self.np.write()
        self.t += 1
        self.t%=100000
    def seizure(self):
        for i in range(len( self.tree.leds)):
            led = self.tree.leds[i]
            led.color = [np.random.randint(0,60),np.random.randint(0,60),np.random.randint(0,5)]
            self.np[i] = led.color
    def color_by_angle(self):
        for i in range(len(self.tree.leds)):
            led = self.tree.leds[i]
            led.color = self.wheel((int((math.degrees(led.angle)+90+10*self.t)%360)*(255/360)))

            self.np[i] = (led.color[1]//4, led.color[0]//4, led.color[2]//4)

    def stripe(self):
        for i in range(len(self.tree.leds)):
                led = self.tree.leds[i]
                z = (self.t*10)%2000
                if abs(led.pos[2] - z) < 100:
                    led.color = (60,0,0)
                else:
                    led.color = (60,60,60)
                self.np[i] = led.color

    def color_wheel(self):
        for i in range(len(self.tree.leds)):
            led = self.tree.leds[i]
            lookup = [
                (60, 0, 0),
                (60, 60,60),
            ]
            angle = math.degrees(led.angle)+90
            angle += led.pos[2]*0.8
            angle += self.t*2.5
            angle %= 360
            led.color = lookup[math.floor(
                angle/(360/len(lookup)))]
            self.np[i] = (led.color[0], led.color[1], led.color[2])

    def light_at_index(self, i, c):
        self.np.fill((0, 0, 0))
        self.np[i] = c
        self.np.write()

