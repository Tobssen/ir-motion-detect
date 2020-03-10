import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep

SENSOR_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

camera = PiCamera()

def mein_callback(channel):
    # Hier kann alternativ eine Anwendung/Befehl etc. gestartet werden.
    print('Es gab eine Bewegung!')
    camera.capture('/home/pi/Desktop/ir-motion-detect/image.jpg')

try:
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=mein_callback)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print("Beende...")
GPIO.cleanup()
