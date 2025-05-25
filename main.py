import RPi.GPIO as GPIO
import time

PUMP_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMP_PIN, GPIO.OUT)

GPIO.output(PUMP_PIN, GPIO.HIGH)
time.sleep(15)
GPIO.output(PUMP_PIN, GPIO.LOW)

GPIO.cleanup()