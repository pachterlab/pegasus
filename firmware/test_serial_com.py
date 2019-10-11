#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import sys
import glob
import time

startMarker = 60 # <
endMarker = 62 # >
midMarker = 44 # ,

def populate_ports():
	"""
		:raises EnvironmentError:
			On unsupported or unknown platforms
		:returns:
			A list of the serial ports available on the system
	"""
	if sys.platform.startswith('win'):
		ports = ['COM%s' % (i + 1) for i in range(256)]
	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		# this excludes your current terminal "/dev/tty"
		ports = glob.glob('/dev/tty[A-Za-z]*')
	elif sys.platform.startswith('darwin'):
		ports = glob.glob('/dev/tty.*')
	else:
		raise EnvironmentError('Unsupported platform')

	result = []
	for port in ports:
		try:
			s = serial.Serial(port)
			s.close()
			result.append(port)
		except (OSError, serial.SerialException):
			pass
	return result[-1]

def connect(port):
	s = serial.Serial()
	s.port = port
	s.baudrate = 2000000
	s.parity = serial.PARITY_NONE
	s.stopbits = serial.STOPBITS_ONE
	s.bytesize = serial.EIGHTBITS
	s.timeout = 1
	s.open()
	return s

def write_to_Arduino(s, string):
	s.write(string.encode())
	s.flushInput()
	return

def listen(s):
	char = ""
	x = "z" # any value that is not an end- or startMarker

	# wait for the start character
	while  ord(x) != startMarker:
		x = s.read()

	# save data until the end marker is found
	while ord(x) != endMarker:
		if ord(x) != startMarker:
			char = char + x.decode()

		x = s.read()

	return(char)

def talk(s, commands):
	waitingForReply = False

	for teststr in commands: # could use a while loop + numloops iterator?
		if not cmd_valid(teststr):
			continue # returns to beginning of for loop and grabs next string
		if waitingForReply == False:
			write_to_Arduino(s, teststr)
			print("Sent from PC -- " + teststr)
			waitingForReply = True

		if waitingForReply == True:
			while s.inWaiting() == 0:
				pass

			dataRecvd = listen(s)
			print("Reply Received -- " + dataRecvd)
			waitingForReply = False


		time.sleep(0.1)
	print("Send and receive complete")


# all this does is check if a command is formatted properly
# used in talk() prior to sending a command to the arduino
def cmd_valid(cmd):
	cmds = ["RUN", "STOP", "RESUME", "PAUSE", "SET_SPEED", "SET_ACCEL"]
	inds = ["000", "100", "010", "001", "110", "101", "011", "111"]
	valid = False
	if "," in cmd and cmd[0] == '<' and cmd[-1]=='>':
		testcmd = cmd[1:].split(",")[0]
		ind = cmd[1:].split(",")[1]
		if testcmd in cmds and ind in inds:
			valid = True
			return valid
	return valid

if __name__ == "__main__":
	setup_cmds = [
	"<SET_ACCEL,100,5000.0,5000.0.0,5000.0>",
	"<SET_SPEED,100,1000.0,1000.0,1000.0>",
	]

	run_cmds = [
	"<this should not work>",
	"<Neither should this>",
	"Or this",
	"Or even, this>",
	"<RUN, 123, 0.0, 0.0, 0.0>", # this shouldn't run either
	"<RUN,100,5000.0,200.0,200.0>"
	]

	stop_cmds = [
	"<STOP,100,0.0,0.0,0.0>"
	]

	port = populate_ports()
	print("\n[setup] Connecting to port: {}".format(port))
	s = connect(port)

	time.sleep(5) # wait for the arduino to initialize
	print(listen(s))

	print("\n[setup] Sending setup commands..")
	talk(s, run_cmds)

	print("\n[action] Sending run commands..")
	talk(s, run_cmds)

	time.sleep(1)

	print("\n[action] Sending stop commands..")
	talk(s, stop_cmds)

	print("\n[action] Closing port..")
	s.close()

## Set Accel to be blah
# <SET_ACCEL,111,9000.0,9000.0,9000.0>

## Set Speed to be blah
# <SET_SPEED,111,1000.0,1000.0,1000.0>

## Run at speed for 1 rotation
# <RUN,110,200,200,0>

## Run at speed for 10 rotations
# <RUN,010,0,10000,0>

## Stop
# <STOP,010,0,0,0>
