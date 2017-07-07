import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)       # chon kieu BCM
GPIO.setup(18, GPIO.OUT)     # thiet lap ngo ra

while True:                  # vong lap vo tan
  GPIO.output(18, GPIO.HIGH) # LED sang
  time.sleep(1)              # cho 1s  
  GPIO.output(18, GPIO.LOW)  # LED tat
  time.sleep(1)              # cho 1s