#!/usr/bin/env python
# -*- coding: utf-8 -*-
# main.py
import pegasus_window
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog

import sys
import os
import time
import threading

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
from serial_comm import populate_ports, connect, talk, listen
from multi import Thread


class MainWindow(QtWidgets.QMainWindow, pegasus_window.Ui_MainWindow):
## Initiators
	def __init__(self):

		# Setting the UI to a class variable and connecting all GUI Components
		super(MainWindow, self).__init__()
		self.ui = pegasus_window.Ui_MainWindow()
		self.ui.setupUi(self)

		# Variables
		self.all_units = ["steps/s"] 
		self.all_microstepping_values = ['1', '2', '4', '8', '16', '32']
		self.all_jog_deltas = ["0.01", "0.1", "1.0", "10.0", "100.0"]

		# This will need to be changed
		self.accels = [2000.0, 2000.0, 2000.0]

		self.enable_boxes = [getattr(self.ui, i+"_enable_CHECK_BOX") for i in ["x", "y", "z"]]
		self.displacement_boxes = [getattr(self.ui, i+"_displacement_SPIN_BOX") for i in ["x", "y", "z"]]
		self.speed_boxes = [getattr(self.ui, i+"_speed_SPIN_BOX") for i in ["x", "y", "z"]]

		self.status = [0,0,0]
		self.displacements = [0.0,0.0,0.0]
		self.speeds = [0.0,0.0,0.0]


		self.ui.x_enable_CHECK_BOX
		self.ui.y_enable_CHECK_BOX


		# Populators
		self.populate_ports()
		self.populate_units()
		self.populate_microstepping()
		self.populate_jog_delta()


		# Slotting
		self.ui.refresh_BUTTON.clicked.connect(self.populate_ports)
		self.ui.motor_port_COMBO_BOX.currentIndexChanged.connect(self.set_port)
		self.ui.encoder_port_COMBO_BOX.currentIndexChanged.connect(self.set_port)

		self.ui.connect_BUTTON.clicked.connect(self.connect)
		self.ui.disconnect_BUTTON.clicked.connect(self.disconnect)

		self.ui.units_COMBO_BOX.currentIndexChanged.connect(self.set_units)
		self.ui.microstepping_COMBO_BOX.currentIndexChanged.connect(self.set_microstepping)
		self.ui.jog_delta_COMBO_BOX.currentIndexChanged.connect(self.set_jog_delta)

		self.ui.jog_plus_BUTTON.clicked.connect(lambda:self.control(self.ui.jog_plus_BUTTON))
		self.ui.jog_minus_BUTTON.clicked.connect(lambda:self.control(self.ui.jog_minus_BUTTON))

		self.ui.start_BUTTON.clicked.connect(lambda:self.control(self.ui.start_BUTTON))
		self.ui.stop_BUTTON.clicked.connect(lambda:self.control(self.ui.stop_BUTTON))
		self.ui.pause_BUTTON.clicked.connect(lambda:self.control(self.ui.pause_BUTTON))

		for box in self.enable_boxes:
			box.stateChanged.connect(self.set_enable)
		for box in self.displacement_boxes:
			box.valueChanged.connect(self.set_displacement)
		for box in self.speed_boxes:
			box.valueChanged.connect(self.set_speed)

		## Setup a separate thread to listen to the encoder arduino to report values to the GUI
		self.encoder_thread = threading.Thread(target=self.encoder)


		## Initiation multicore capabilities
		self.threadpool = QtCore.QThreadPool()
		print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

## Populators
	def populate_ports(self):
		self.ui.motor_port_COMBO_BOX.clear()
		self.ui.encoder_port_COMBO_BOX.clear()

		ports = populate_ports()
		self.ui.motor_port_COMBO_BOX.addItems(ports)
		self.ui.encoder_port_COMBO_BOX.addItems(ports)
		self.ui.motor_port_COMBO_BOX.setCurrentIndex(0)
		self.ui.encoder_port_COMBO_BOX.setCurrentIndex(0)

		self.motor_port = ports[0]
		self.encoder_port = ports[0]

	# Populate the microstepping amounts for the dropdown menu
	def populate_microstepping(self):
		self.ui.microstepping_COMBO_BOX.addItems(self.all_microstepping_values)
		self.ui.microstepping_COMBO_BOX.setCurrentIndex(0)

		self.microstepping = self.all_microstepping_values[0]

	def populate_units(self):
		self.ui.units_COMBO_BOX.addItems(self.all_units)
		self.ui.units_COMBO_BOX.setCurrentIndex(0)

		self.units = self.all_units[0]

	def populate_jog_delta(self):
		self.ui.jog_delta_COMBO_BOX.addItems(self.all_jog_deltas)
		self.ui.jog_delta_COMBO_BOX.setCurrentIndex(0)

		self.jog_delta = self.all_jog_deltas[0]

## Functors
	def connect(self):
		try:
			motor_port_declared = self.motor_port
			encoder_port_declared = self.encoder_port
			try:
				self.motor_serial = connect(motor_port_declared)
				self.encoder_serial = connect(encoder_port_declared)

				self.motor_port_connected = True
				self.encoder_port_connected = True

				# Send over accels before saying successful
				time.sleep(2)
				self._setup_accel()

				# Start the encoder thread
				self.thread = Thread(self.encoder)
				self.thread.finished.connect(lambda:self.thread_finished(self.thread))
				self.thread.start()
				

				self.ui.port_status_LABEL.setText("CONNECTED")
				self.ui.port_status_LABEL.setStyleSheet("color: green")

				self.statusBar().showMessage("Successfully connected to boards.")
			except Exception as e:
				print(e)
				self.statusBar().showMessage("Cannot connect to boards. Try again..")
				# raise CannotConnectException
		except AttributeError:
			self.statusBar().showMessage("Please plug in the boards and select a proper ports, then press connect.")

	def disconnect(self):
		try:
			if self.motor_port_connected and self.encoder_port_connected:
				try:
					self.thread.stop()
					time.sleep(2)

					self.motor_serial.close()
					self.encoder_serial.close()

					self.motor_port_connected = False
					self.encoder_port_connected = False

					self.ui.port_status_LABEL.setText("DISCONNECTED")
					self.ui.port_status_LABEL.setStyleSheet("color: rgb(252, 1, 7)")
					self.statusBar().showMessage("Successfully disconnected from the boards.")
				except:
					self.statusBar().showMessage("Error disconnecting")
		except:	
			self.statusBar().showMessage("You were never connected")



	def control(self, btn):
		data = map(str, self.displacements)
		ind = "".join(map(str, self.status))
		cmd_text = "STOP"

		if btn.text() == "Stop":
			cmd_text = "STOP"
		elif btn.text() == "Start":
			cmd_text = "RUN"
		elif btn.text() == "Pause":
			cmd_text = "PAUSE"
		elif btn.text() == "Resume":
			cmd_text = "RESUME"
		elif btn.text() == "Jog +":
			cmd_text = "RUN"
			data = [self.jog_delta]*3
		elif btn.text() == "Jog -":
			cmd_text = "RUN"
			data = [str(-1*float(self.jog_delta))]*3

		cmd = ["<{},{},{},{},{}>".format(cmd_text, ind, *data)]

		return talk(self.motor_serial, cmd)

	def encoder(self):
		while self.encoder_serial.inWaiting() == 0:
				pass
		self.encoder_serial.flushInput()

		while True:
			while self.encoder_serial.inWaiting() == 0:
				pass


			data = listen(self.encoder_serial).split(",")
			t_tmp, x_tmp, v_tmp = data
			self.ui.position_LCD_NUM.display(x_tmp)
			self.ui.speed_LCD_NUM.display(v_tmp)
			# print("{}\t{}\t{}".format(t_tmp, x_tmp, v_tmp))

	def thread_finished(self, th):
		print("Your thread has completed. Now terminating..")
		th.stop()
		print("Thread has been terminated.")


## Setters
	def set_port(self):
		self.motor_port = self.ui.motor_port_COMBO_BOX.currentText()
		self.encoder_port = self.ui.encoder_port_COMBO_BOX.currentText()
	def set_units(self):
		self.units = self.ui.units_COMBO_BOX.currentText()
	def set_microstepping(self):
		self.microstepping = self.ui.microstepping_COMBO_BOX.currentText()
	def set_jog_delta(self):
		self.jog_delta = self.ui.jog_delta_COMBO_BOX.currentText()
	def set_enable(self):
		for i in range(len(self.enable_boxes)):
			if self.enable_boxes[i].isChecked():
				self.status[i] = 1
			else:
				self.status[i] = 0
	def set_displacement(self):
		for i in range(len(self.displacement_boxes)):
			self.displacements[i] = float(self.displacement_boxes[i].value())
	def set_speed(self):
		for i in range(len(self.speed_boxes)):
			self.speeds[i] = float(self.speed_boxes[i].value())
		self._setup_speed()

	def _setup_speed(self): # called after every speed change
		data = map(str, self.speeds)
		ind = "111"
		cmd = ["<{},{},{},{},{}>".format("SET_SPEED", ind, *data)]
		return talk(self.motor_serial, cmd)

	def _setup_accel(self): # called immediately after connecting to the arduino
		data = map(str, self.accels)
		ind = "111"
		cmd = ["<{},{},{},{},{}>".format("SET_ACCEL", ind, *data)]
		return talk(self.motor_serial, cmd)

### On close
	def closeEvent(self, event):
		print("Closing the GUI..")
		self.disconnect()
		event.accept()


def main():
	# a new app instance
	app = QtWidgets.QApplication(sys.argv)
	window = MainWindow()
	window.setWindowTitle("Pegasus Motor Controller")
	window.show()

	# without this, the script exits immediately.
	ret = app.exec_()
	sys.exit(ret)


if __name__ == "__main__":
	main()
