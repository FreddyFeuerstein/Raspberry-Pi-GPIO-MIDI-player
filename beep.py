# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import wiringpi

from pprint import pprint 
import sys

outpin = 18  # The Pin that the buzzer isconnected to

def tone(freq, length):
	ms = float(length) / 1000
	print('freq %d length %f sec' % (freq, ms))
	wiringpi.softToneWrite(outpin, freq)
	sleep(ms)
	wiringpi.softToneWrite(outpin, 0)

def parseParam():
	result = []
	argvs = sys.argv  # コマンドライン引数を格納したリストの取得
	
	delimiters = ["-n", "-new", "-r", "-d", "-D"]
	
	# beep.py -f freq -l millisecond -n -f freq2 -l millisecond2
	current = []
	freq = 200
	length = 100
	last_flag = ""
	for i in range(1, len(sys.argv) ):
		arg = argvs[i]
		# print "index = %d arg = %s" % (i, arg)

		if ( last_flag == '-r' ):
			# print("repeat %s", arg)
			# pprint(current)
			for var in range(0, int(arg)):
				result.extend(current)
			last_flag = ""; current = [];

		if ( arg.startswith('-') ):
			last_flag = arg;
		else:
			# param
			if ( last_flag == '-f' ):
				freq = int(float(arg))
			elif ( last_flag == '-l' ):
				length = int(arg)
			elif ( last_flag == '-d' or last_flag == '-D'):
				freq = 0
				length = int(arg)
			last_flag = ""

		if ( delimiters.count(arg) > 0 or i == (len(sys.argv) - 1) ):
			beep = { 'freq' : freq, 'length' : length }
			result.append(beep)
			current.append(beep)
	
	return result

def parseSimpleParam():
	argvs = sys.argv  # コマンドライン引数を格納したリストの取得
	freq = int(float(argvs[1]))
	length = float(argvs[2])
	return [{ 'freq' : freq, 'length' : length }]

def main():
	if ( len(sys.argv) < 3 ):
		print('Usage: # python %s freq millisecond' % sys.argv[0])
		print('Usage: # python %s -f freq -l millisec -n -f freq2 -l millisec2...' % sys.argv[0])
		quit();

	if ( len(sys.argv) == 3 ):
		beepList = parseSimpleParam()
	else:
		beepList = parseParam()

	if ( len(beepList) == 0 ):
		print('Usage: # python %s -f freq -l millisec -n -f freq2 -l millisec2...' % sys.argv[0])
		quit()

	## sounding 
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(outpin, GPIO.OUT)

	wiringpi.wiringPiSetupGpio() 
	wiringpi.softToneCreate(outpin)

	for beep in beepList:
		if (beep['freq'] == 0):
			length = float(beep['length']) / 1000
			print("Wait %f ms" % length)
			sleep(length)
		else:
			tone(beep['freq'], beep['length'])

try:
	main()
finally:
	GPIO.cleanup()

