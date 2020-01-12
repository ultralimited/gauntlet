#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [2, 3, 4, 5, 6, 12, 13, 16, 17, 22, 23, 24, 25, 26, 27]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop
def tableUp():
	GPIO.output(27, GPIO.LOW)
	print("Table Up")
	sleep(0.25)

def tableDown():
	GPIO.output(27, GPIO.HIGH)
	print("Table Down")
	sleep(0.25)
	
def go():
	time.sleep(0.25);
	GPIO.output(4, GPIO.LOW)
	print ("fork on")
	time.sleep(0.25);

	GPIO.output(17, GPIO.LOW)
	print ("index on")

  
	time.sleep(3);

  
	GPIO.output(27, GPIO.LOW)
	print ("table up");

	time.sleep(2);
  
	GPIO.output(4, GPIO.HIGH)
	print ("fork OFF")
	time.sleep(0.25);

	GPIO.output(17, GPIO.HIGH)
	print ("index OFF")
	time.sleep(0.25);
	GPIO.output(23, GPIO.LOW)
	print ("RESET index ")


  
	print ("PRINTING")   
	GPIO.output(26, GPIO.LOW)
	print ("PRINT 1")
	GPIO.output(16, GPIO.LOW)
	print ("PRINT 2")
	GPIO.output(13, GPIO.LOW)
	print ("PRINT 3")
	GPIO.output(6, GPIO.LOW)
	print ("PRINT 4")
	GPIO.output(12, GPIO.LOW)
	print ("PRINT 5")
	GPIO.output(5, GPIO.LOW)
	print ("PRINT 6")
	GPIO.output(25, GPIO.LOW)
	print ("PRINT 7")
	GPIO.output(24, GPIO.LOW)
	print ("PRINT 8")


	time.sleep(3);


	GPIO.output(23, GPIO.HIGH)
	print ("RESET READY")

	time.sleep(0.25);
  
	GPIO.output(27, GPIO.HIGH)
	print ("table down")

  
	print ("FLOOD")
	GPIO.output(26, GPIO.HIGH)
	print ("FLOOD 1")
	GPIO.output(16, GPIO.HIGH)
	print ("FLOOD 2")
	GPIO.output(13, GPIO.HIGH)
	print ("FLOOD 3")
	GPIO.output(6, GPIO.HIGH)
	print ("FLOOD 4")
	GPIO.output(12, GPIO.HIGH)
	print ("FLOOD 5")
	GPIO.output(5, GPIO.HIGH)
	print ("FLOOD 6")
	GPIO.output(25, GPIO.HIGH)
	print ("FLOOD 7")
	GPIO.output(24, GPIO.HIGH)
	print ("FLOOD 8")
	
 
def prePrint():
	time.sleep(0.25);
	GPIO.output(4, GPIO.LOW)
	
	print ("fork on")
	time.sleep(0.25);

	GPIO.output(17, GPIO.LOW)
	print ("index on")
  
	time.sleep(3);
  
	GPIO.output(27, GPIO.LOW)
	print ("table up");

	time.sleep(1);
  
	GPIO.output(4, GPIO.HIGH)
	print ("fork OFF")
	time.sleep(0.15);

	GPIO.output(17, GPIO.HIGH)
	print ("index OFF")
	time.sleep(0.15);
	GPIO.output(23, GPIO.LOW)
	print ("RESET index ")

def flood():
	print ("FLOOD")
	GPIO.output(26, GPIO.HIGH)
	print ("FLOOD 1")
	GPIO.output(16, GPIO.HIGH)
	print ("FLOOD 2")
	GPIO.output(13, GPIO.HIGH)
	print ("FLOOD 3")
	GPIO.output(6, GPIO.HIGH)
	print ("FLOOD 4")
	GPIO.output(12, GPIO.HIGH)
	print ("FLOOD 5")
	GPIO.output(5, GPIO.HIGH)
	print ("FLOOD 6")
	GPIO.output(25, GPIO.HIGH)
	print ("FLOOD 7")
	GPIO.output(24, GPIO.HIGH)
	print ("FLOOD 8")

def printHeads(heads):
	prePrint()
	
	print('Heads', heads)
	if heads[0]:
		print("1 go")
		GPIO.output(26, GPIO.LOW)

		
	if heads[1]:
		print("2 go")
		GPIO.output(16, GPIO.LOW)

	if heads[2]:
		print("3 go")
		GPIO.output(13, GPIO.LOW)
		
	if heads[3]:
		print("4 go")
		GPIO.output(6, GPIO.LOW)

	if heads[4]:
		print("5 go")
		GPIO.output(12, GPIO.LOW)

	if heads[5]:
		print("6 go")
		GPIO.output(5, GPIO.LOW)

	if heads[6]:
		print("7 go")
		GPIO.output(25, GPIO.LOW)

	if heads[7]:
		print("8 go")
		GPIO.output(24, GPIO.LOW)
		
	time.sleep(4.5);
	
	flood()
    
	time.sleep(2.5);
    
	print('Heads', heads)
	if heads[0]:
		print("1 go")
		GPIO.output(26, GPIO.LOW)

		
	if heads[1]:
		print("2 go")
		GPIO.output(16, GPIO.LOW)

	if heads[2]:
		print("3 go")
		GPIO.output(13, GPIO.LOW)
		
	if heads[3]:
		print("4 go")
		GPIO.output(6, GPIO.LOW)

	if heads[4]:
		print("5 go")
		GPIO.output(12, GPIO.LOW)

	if heads[5]:
		print("6 go")
		GPIO.output(5, GPIO.LOW)

	if heads[6]:
		print("7 go")
		GPIO.output(25, GPIO.LOW)

	if heads[7]:
		print("8 go")
		GPIO.output(24, GPIO.LOW)
    
	time.sleep(4.5);


	GPIO.output(23, GPIO.HIGH)
	print ("RESET READY")

	time.sleep(0.15);
  
	GPIO.output(27, GPIO.HIGH)
	print ("table down")

	flood()

	


# find more information on this script at
# http://youtu.be/oaf_zQcrg7g


