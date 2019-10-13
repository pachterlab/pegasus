# pegasus: open source stepper motor control
__________________________________
A modular, reliable, and easy-to-use stepper motor controller written in Python and Arduino. Control up to 3 stepper motors simulatenously.

## The tl;dr

The pegasus system allows you to communicate with an Arduino from python to run up to 3 stepper motors, using the Arduino, CNC Motor Shield, and any of the [Pololu Stepper Motor Drivers](https://www.pololu.com/category/120/stepper-motor-drivers). 

## What is included?
* Arduino firmware for use with an Arudino Uno
* A python script to test running a motor.

## What do I need? (Everything is available via Amazon)
* An [Arduino Uno](https://www.amazon.com/Arduino-A000066-ARDUINO-UNO-R3/dp/B008GRTSV6/ref=sr_1_3?keywords=arduino&qid=1570988503&sr=8-3) (or cheap knockoff)
* [Arduino to Computer cable](https://www.amazon.com/AmazonBasics-USB-2-0-Cable-Male/dp/B00NH11KIK/ref=sr_1_3?keywords=arduino+cable&qid=1570989005&sr=8-3)
* [CNC Motor Shield](https://www.amazon.com/HiLetgo®-Engraver-Printer-Expansion-Arduino/dp/B01D2HL9T8/ref=sr_1_5?keywords=cnc+motor+shield&qid=1570988531&sr=8-5) for the Arduino
* Pololu [Stepper Motor Driver](https://www.amazon.com/KINGPRINT-DRV8825-Stepper-Driver-Printer/dp/B075XH1TSJ/ref=sr_1_4?keywords=pololu+stepper+motor+driver&qid=1570988556&sr=8-4)
* [Stepper Motor](https://www.amazon.com/STEPPERONLINE-Stepper-Bipolar-Connector-compatible/dp/B00PNEQKC0/ref=sr_1_4?keywords=stepper+motor&qid=1570988610&sr=8-4)
* [Power cable](https://www.amazon.com/ALITOVE-Converter-5-5x2-1mm-100V-240V-Security/dp/B078RT3ZPS/ref=sr_1_12?keywords=power+cable+to+terminal&qid=1570988714&sr=8-12)
* [Adapter wire](https://www.amazon.com/43x2pcs-Connectors-Security-Lighting-MILAPEAK/dp/B072BXB2Y8/ref=sr_1_11?keywords=power+cable+to+terminal&qid=1570988714&sr=8-11)

## Getting Started
Setup the hardware by following this [instructional video](https://www.youtube.com/watch?v=Xl02fsRCJ7U). connect the arduino to your computer, and connect the CNC shield to a power outlet.

Clone or download this repository:
```
$ git clone https://github.com/sbooeshaghi/pegasus.git
```

Open up the [Arduino IDE](https://www.arduino.cc/en/main/software) and load up `motor_serial_com.ino`. Select the right port, connect to the Arduino, and upload the firmware.

Go to the terminal and run the test script
```
$ chmod +x test_serial_com.py
$ ./test_serial_com.py
```

The code should do the following:
1. Establish a connection with the Arduino,
2. Send over "setup" commands,
3. Send a Run commend, telling the motor to move,
4. Send a Pause command, 
5. Send a Resume command
6. Send a Stop command.

This is the command structure for sending a command from the Python Script to the Arduino :
```
"<mode,motorID,arg_m1,arg_m2,arg_m3>" # no spaces! the command is a string!
```

The possible commands are:
```
Where mode is one of [RUN, STOP, RESUME, PAUSE, SET_SPEED, SET_ACCEL]
motorID is one of int [000, 100, 010, 001, 110, 101, 011, 111] 
arg_m1 is [any floating number]
arg_m2 is [any floating number]
aeg_m3 is [any floating number]
```

## A possible failure
Make sure that the port the code connects to is the correct port. Notice in the following example, my computer connected to the wrong port (Bluetooth port). 

 ```
 $ ./test_serial_com.py
 [setup] Connecting to port: /dev/tty.Bluetooth-Incoming-Port
Traceback (most recent call last):
  File "./test_serial_com.py", line 145, in <module>
    print(listen(s))
  File "./test_serial_com.py", line 60, in listen
    while  ord(x) != startMarker:
TypeError: ord() expected a character, but string of length 0 found
```

If you get the above error then chances are you either 1. don't have the Arduino connected, 2. tried to run the test code while the Arduino firmware was being uploaded to the arduino or 3. the code selected the wrong port programmatically. Check out the `populate_ports()` in the python script. The return `return result[-1]` automatically returns the last port in the list of `result` ports.

## Acknowledgements
This work would not have been possible without the help of the wonderful [Serial Communications Basics Tutorial](https://forum.arduino.cc/index.php?topic=396450.0) by Robin2 at the [Arduino Forum](https://forum.arduino.cc/index.php) and the really awesome [AccelStepper Library](http://www.airspayce.com/mikem/arduino/AccelStepper/classAccelStepper.html) made by Mike McCauley. Also a big thank you to [Professor Lior Pachter](https://liorpachter.wordpress.com) for supporting my work while doing a PhD in [his lab at Caltech](https://pachterlab.github.io).
