#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore
import traceback, sys

# ##############################
# MULTITHREADING : SIGNALS CLASS
# ##############################
class WorkerSignals(QtCore.QObject):
    '''
    Defines the signals available from a running worker thread.
    Supported signals are:
    finished
        No data
    error
        `tuple` (exctype, value, traceback.format_exc() )
    result
        `object` data returned from processing, anything
    '''
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(int)

# #############################
# MULTITHREADING : WORKER CLASS
# #############################


class Thread(QtCore.QThread):
	def __init__(self, fn, *args, **kwargs):
		parent = None
		super(Thread, self).__init__(parent)
		self.runs = True
		self.fn = fn
		self.args = args
		self.kwargs = kwargs
		self.signals = WorkerSignals()

	def run(self):
		try:
			result = self.fn(*self.args, **self.kwargs)
		except:
			pass # uncomment when done debugging
			# traceback.print_exc()
			# exctype, value = sys.exc_info()[:2]
			# self.signals.error.emit((exctype, value, traceback.format_exc()))
		else:
			self.signals.result.emit(result)  # Return the result of the processing
		finally:
			self.signals.finished.emit()  # Done
			self.stop()

			print("Job completed")

	def stop(self):
		self.runs = False