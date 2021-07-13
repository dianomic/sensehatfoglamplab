from sense_hat import SenseHat
import time
def warning(message):
    sense = SenseHat()
    x = [238, 210, 2] #yellow
    o = [0, 0, 0] # off
    r = [255,15,15] # red
    exclaimation_off = [
        o,o,o,x,x,o,o,o,
        o,o,x,x,x,x,o,o,
        o,o,x,o,o,x,o,o,
        o,x,x,o,o,x,x,o,
        o,x,x,o,o,x,x,o,
        o,x,x,x,x,x,x,o,
        x,x,x,o,o,x,x,x,
        x,x,x,x,x,x,x,x,
    ]
    exclaimation_on = [
        o,o,o,x,x,o,o,o,
        o,o,x,x,x,x,o,o,
        o,o,x,r,r,x,o,o,
        o,x,x,r,r,x,x,o,
        o,x,x,r,r,x,x,o,
        o,x,x,x,x,x,x,o,
        x,x,x,r,r,x,x,x,
        x,x,x,x,x,x,x,x,
    ]
    for i in range(5):
        sense.set_pixels(exclaimation_off)
        time.sleep(1)
        sense.set_pixels(exclaimation_on)
        time.sleep(1)
    sense.clear()