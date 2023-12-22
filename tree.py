from led import Led
import math


class Tree():
    def __init__(self, leds):
        self.leds = leds
        self.center = [
            sum([led.pos[0] for led in leds])/len(leds),
            sum([led.pos[1] for led in leds])/len(leds),
        ]

        print(self.center)
        for led in self.leds:
            # xy = led.pos[0:1]
            # normal = np.linalg.norm(xy-self.center)
            # led.set_normal(normal)

            y = led.pos[1]-self.center[1]
            x = led.pos[0]-self.center[0]

            if x < 0:
                led.set_angle(math.atan(y/x)+math.pi)
            elif x > 0:
                led.set_angle(math.atan(y/x))
            else:
                led.set_angle(math.pi/2)

