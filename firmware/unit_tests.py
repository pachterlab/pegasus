#!/usr/bin/env python
# -*- coding: utf-8 -*-

from serial_comm import populate_ports, connect, listen, talk
import time

setup_cmds = [
		"<SET_ACCEL,100,5000.0,5000.0.0,5000.0>",
		"<SET_SPEED,100,1000.0,1000.0,1000.0>",
	]

run_cmds = [
		"<RUN,100,5000.0,200.0,200.0>"
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

	time.sleep(2)

	print("\n[action] Closing port..")
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

def main():
	print("---------------- Testing {} ----------------").format("Valid Cmd")
	test_valid_cmd()

	print("---------------- Testing {} ----------------").format("Run")
	test_run()

	print("---------------- Testing {} ----------------").format("Stop")
	test_stop()

	print("---------------- Testing {} ----------------").format("Pause Resume")
	test_pause_resume()

	print("---------------- Complete ----------------")


if __name__ == '__main__':
	main()