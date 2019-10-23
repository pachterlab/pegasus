#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')
from serial_comm import populate_ports, connect, listen, talk
import time

setup_cmds = [
		"<SET_ACCEL,100,5000.0,1500.0.0,1500.0>",
		"<SET_SPEED,100,400.0,400.0,400.0>",
	]

run_cmds = [
		"<RUN,100,5000.0,200.0,200.0>"
	]

run_short_cmds = [
		"<RUN,100,200.0,200.0,200.0>",
		"<RUN,100,-200.0,-200.0,-200.0>",
	]

stop_cmds = [
		"<STOP,100,0.0,0.0,0.0>"
	]

pause_cmds = [
		"<PAUSE,100,0.0,0.0,0.0>"
	]

resume_cmds = [
		"<RESUME,100,0.0,0.0,0.0>"
	]

invalid_cmds = [
		"<this should not work>",
		"<Neither should this>",
		"Or this",
		"Or even, this>",
		"<RUN, 123, 0.0, 0.0, 0.0>", # this shouldn't run either
	]

def test_valid_cmd():
	port = populate_ports()[-1]
	print("\n[setup] Connecting to port: {}".format(port))
	s = connect(port)

	time.sleep(5) # wait for the arduino to initialize
	print(listen(s))

	print("\n[setup] Sending setup commands..")
	talk(s, setup_cmds)

	time.sleep(1)

	print("\n[action] Sending invalid run commands.. nothing should happen..")
	talk(s, invalid_cmds)

	print("\n[action] Closing port..")
	s.close()

	return


def test_run():
	port = populate_ports()[-2]
	print("\n[setup] Connecting to port: {}".format(port))
	s = connect(port)

	time.sleep(5) # wait for the arduino to initialize
	print(listen(s))

	print("\n[setup] Sending setup commands..")
	talk(s, setup_cmds)

	time.sleep(1)

	print("\n[action] Sending run commands..")
	# talk(s, run_cmds)
	talk(s, [run_short_cmds[0]])
	time.sleep(1.5)
	talk(s, [run_short_cmds[1]])

	time.sleep(2)

	print("\n[action] Closing port..")
	s.close()

	return

def test_run_silent():
	port = populate_ports()[-2]
	s = connect(port)

	time.sleep(5) # wait for the arduino to initialize

	talk(s, setup_cmds)

	time.sleep(1)

	talk(s, [run_short_cmds[0]])
	time.sleep(1.5)
	talk(s, [run_short_cmds[1]])
	time.sleep(1.5)
	talk(s, [run_short_cmds[0]])
	time.sleep(1.5)
	talk(s, [run_short_cmds[1]])
	time.sleep(1.5)
	talk(s, [run_short_cmds[0]])
	time.sleep(1.5)
	talk(s, [run_short_cmds[1]])

	time.sleep(2)

	s.close()

	return

def test_stop():
	port = populate_ports()[-1]
	print("\n[setup] Connecting to port: {}".format(port))
	s = connect(port)

	time.sleep(5) # wait for the arduino to initialize
	print(listen(s))

	print("\n[setup] Sending setup commands..")
	talk(s, setup_cmds)

	time.sleep(1)

	print("\n[action] Sending run commands..")
	talk(s, run_cmds)

	time.sleep(1)

	print("\n[action] Sending stop commands..")
	talk(s, stop_cmds)

	print("\n[action] Closing port..")
	s.close()

	return

def test_pause_resume():
	port = populate_ports()[-1]
	print("\n[setup] Connecting to port: {}".format(port))
	s = connect(port)

	time.sleep(5) # wait for the arduino to initialize
	print(listen(s))

	print("\n[setup] Sending setup commands..")
	talk(s, setup_cmds)

	time.sleep(1)

	print("\n[action] Sending run commands..")
	talk(s, run_cmds)

	time.sleep(1)

	print("\n[action] Sending pause commands..")
	talk(s, pause_cmds)

	time.sleep(1)

	print("\n[action] Sending resume commands..")
	talk(s, resume_cmds)


	print("\n[action] Closing port..")
	s.close()

	return

def test_profile_1():
	port = populate_ports()[-1]
	print("\n[setup] Connecting to port: {}".format(port))
	s = connect(port)

	time.sleep(5)
	print(listen(s))

	print("\n[setup] Sending setup commands..")
	talk(s, setup_cmds)

	time.sleep(1)

	print("\n[action] Sending first profile.. speed = 0")
	talk(s, ["<SET_SPEED,100,0,0,0>"])
	talk(s, ["<RUN,100,5000,0,0>"])
	time.sleep(2)
	print("\n[action] Sending first profile.. speed = 400")
	# talk(s, ["<STOP,100,0,0,0>"])
	talk(s, ["<SET_SPEED,100,400,0,0>"])
	talk(s, ["<RUN,100,5000,0,0>"])
	time.sleep(2)
	print("\n[action] Sending first profile.. speed = 200")
	# talk(s, ["<STOP,100,0,0,0>"])
	talk(s, ["<SET_SPEED,100,200,0,0>"])
	talk(s, ["<RUN,100,5000,0,0>"])
	time.sleep(2)
	print("\n[action] Sending first profile.. speed = 800")
	# talk(s, ["<STOP,100,0,0,0>"])
	talk(s, ["<SET_SPEED,100,800,0,0>"])
	talk(s, ["<RUN,100,5000,0,0>"])
	time.sleep(2)
	print("\n[action] Stopping..")
	talk(s, ["<STOP,100,0,0,0>"])

	print("\n[action] Closing port..")
	s.close()

def main():
	# print("---------------- Testing {} ----------------").format("Valid Cmd")
	# test_valid_cmd()

	# print("---------------- Testing {} ----------------".format("Run"))
	# test_run()

	# print("---------------- Testing {} ----------------").format("Stop")
	# test_stop()

	# print("---------------- Testing {} ----------------").format("Pause Resume")
	# test_pause_resume()

	print("---------------- Testing {} ----------------".format("Speed Profile 1"))
	test_profile_1()
	print("---------------- Complete ----------------")


if __name__ == '__main__':
	main()
