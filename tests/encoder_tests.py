#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')
from serial_comm import populate_ports, connect, listen, talk
import time
import matplotlib.pyplot as plt


def test_stream():
	print(populate_ports())
	port = populate_ports()[1]
	print("\n[setup] Connecting to port: {}".format(port))
	s = connect(port)

	time.sleep(5) # wait for the arduino to initialize
	print(listen(s))


	plt.ion() ## Note this correction
	fig=plt.figure()
	t = []
	x = []
	v = []

	while True:
		while s.inWaiting() == 0:
			pass


		data = listen(s).split(",")
		data = [float(i) for i in data]
		t_tmp, x_tmp, v_tmp = data
		print("{}\t{}\t{}".format(t_tmp, x_tmp, v_tmp))
		t.append(t_tmp)
		x.append(x_tmp)
		v.append(v_tmp)

		plt.scatter(t_tmp, x_tmp)
		plt.pause(0.0001)


    	#print(t_tmp, "\t", x_tmp, "\t", v_tmp)
	#plt.show()
	s.close()

def main():
	print("---------------- Testing {} ----------------".format("Stream"))

	test_stream()
	print("---------------- Complete ----------------")


if __name__ == '__main__':
	main()
