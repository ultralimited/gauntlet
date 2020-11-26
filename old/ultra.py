#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 21, 20]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.LOW)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
  GPIO.output(2, GPIO.LOW)
  print ("LOW")
  time.sleep(2);
  GPIO.output(2, GPIO.HIGH)
  print ("HIGH")
  time.sleep(2);
  GPIO.output(2, GPIO.LOW)
  print ("LOW")
  time.sleep(2);
  GPIO.output(2, GPIO.HIGH)
  print ("HIGH")
  time.sleep(2);
  GPIO.cleanup()
  print ("Good bye!")

# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")
