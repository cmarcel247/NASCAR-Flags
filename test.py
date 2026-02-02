import time

from rpi_ws281x import PixelStrip, Color

LED_COUNT = 60
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

if __name__ == '__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(255, 0, 0))
        strip.show()
        time.sleep(50 / 1000)