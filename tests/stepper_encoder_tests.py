#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')
from serial_comm import populate_ports, connect, listen, talk
import time
from encoder_tests import test_stream
from unit_tests import test_run_silent

import threading


def main():
	t1 = threading.Thread(target=test_stream) 
	t2 = threading.Thread(target=test_run_silent)
	
	t1.start()
	t2.start()
	
	t1.join()
	t1.join()
	
	print("Done")

if __name__ == '__main__':
	main()