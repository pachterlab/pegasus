#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Convert:
	def __init__(self, steps_per_rev=200, pitch=0.8, microsteps=4):

		self.steps_per_rev = steps_per_rev # 200 steps per rev
		self.pitch = pitch # one rev is 0.8mm dist
		self.microsteps = microsteps
	
	def steps2mm(self, steps):
		mm = steps/self.steps_per_rev/self.microsteps*self.pitch
		return mm
	
	def mm2steps(self, mm):
		steps = mm/self.pitch*self.steps_per_rev*self.microsteps
		return steps
	
	
	def steps2mL(self, steps, syringe_area):
		mL = self.mm32mL(self.steps2mm(steps)*syringe_area)
		return mL
	
	def steps2uL(self, steps, syringe_area):
		uL = self.mm32uL(self.steps2mm(steps)*syringe_area)
		return uL
	
	
	
	
	def mL2steps(self, mL, syringe_area):
		# note syringe_area is in mm^2
		steps = self.mm2steps(self.mL2mm3(mL)/syringe_area)
		return steps
	
	def uL2steps(self, uL, syringe_area):
		steps = self.mm2steps(self.uL2mm3(uL)/syringe_area)
		return steps
	
	
	def mL2uL(self, mL):
		return mL*1000.0
	
	def mL2mm3(self, mL):
		return mL*1000.0
	
	
	def uL2mL(self, uL):
		return uL/1000.0
	
	def uL2mm3(self, uL):
		return uL
	
	
	def mm32mL(self, mm3):
		return mm3/1000.0
	
	def mm32uL(self, mm3):
		return mm3
	
	def persec2permin(self, value_per_sec):
		value_per_min = value_per_sec*60.0
		return value_per_min
	
	def persec2perhour(self, value_per_sec):
		value_per_hour = value_per_sec*60.0*60.0
		return value_per_hour
	
	
	def permin2perhour(self, value_per_min):
		value_per_hour = value_per_min*60.0
		return value_per_hour
	
	def permin2persec(self, value_per_min):
		value_per_sec = value_per_min/60.0
		return value_per_sec
	
	
	def perhour2permin(self, value_per_hour):
		value_per_min = value_per_hour/60.0
		return value_per_min
	
	def perhour2persec(self, value_per_hour):
		value_per_sec = value_per_hour/60.0/60.0
		return value_per_sec
	
	def convert_displacement(self, displacement, units, syringe_area):
		length = units.split("/")[0]
		time = units.split("/")[1]
		inp_displacement = displacement
		# convert length first
		if length == "mm":
			displacement = mm2steps(displacement)
		elif length == "mL":
			displacement = mL2steps(displacement, syringe_area)
		elif length == "µL":
			displacement = uL2steps(displacement, syringe_area)
	
		print('______________________________')
		print("INPUT  DISPLACEMENT: " + str(inp_displacement) + ' ' + length)
		print("OUTPUT DISPLACEMENT: " + str(displacement) + ' steps')
		print('\n############################################################\n')
		return displacement
	
	def convert_speed(self, inp_speed, units, syringe_area):
		length = units.split("/")[0]
		time = units.split("/")[1]
	
	
		# convert length first
		if length == "mm":
			speed = mm2steps(inp_speed)
		elif length == "mL":
			speed = mL2steps(inp_speed, syringe_area)
		elif length == "µL":
			speed = uL2steps(inp_speed, syringe_area)
	
	
		# convert time next
		if time == "s":
			pass
		elif time == "min":
			speed = permin2persec(speed)
		elif time == "hr":
			speed = perhour2persec(speed)
	
	
	
		print("INPUT  SPEED: " + str(inp_speed) + ' ' + units)
		print("OUTPUT SPEED: " + str(speed) + ' steps/s')
		return speed
	
	def convert_accel(self, accel, units, syringe_area):
		length = units.split("/")[0]
		time = units.split("/")[1]
		inp_accel = accel
		accel = accel
	
		# convert length first
		if length == "mm":
			accel = mm2steps(accel)
		elif length == "mL":
			accel = mL2steps(accel, syringe_area)
		elif length == "µL":
			accel = uL2steps(accel, syringe_area)
	
		# convert time next
		if time == "s":
			pass
		elif time == "min":
			accel = permin2persec(permin2persec(accel))
		elif time == "hr":
			accel = perhour2persec(perhour2persec(accel))
	
		print('______________________________')
		print("INPUT  ACCEL: " + str(inp_accel) + ' ' + units + '/' + time)
		print("OUTPUT ACCEL: " + str(accel) + ' steps/s/s')
		return accel


'''
	Syringe Volume (mL)	|		Syringe Area (mm^2)
-----------------------------------------------
	1				|			17.34206347
	3				|			57.88559215
	5				|			112.9089185
	10				|			163.539454
	20				|			285.022957
	30				|			366.0961536
	60				|			554.0462538
IMPORTANT: These are for BD Plastic syringes ONLY!! Others will vary.
	'''



