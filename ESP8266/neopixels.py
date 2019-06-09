import machine, time, os, neopixel
numpixels = 60
np = neopixel.NeoPixel(machine.Pin(4), numpixels)

def demo():
    # fade in/out

    for i in range(0, 4 * 256, 8):
        for j in range(numpixels):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        time.sleep(0.01)
        np.write()

demo()
while (True):
    demo()
