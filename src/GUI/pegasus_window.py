# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pegasus_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(828, 706)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.jog_minus_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jog_minus_BUTTON.sizePolicy().hasHeightForWidth())
        self.jog_minus_BUTTON.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.jog_minus_BUTTON.setFont(font)
        self.jog_minus_BUTTON.setAutoDefault(False)
        self.jog_minus_BUTTON.setDefault(False)
        self.jog_minus_BUTTON.setObjectName("jog_minus_BUTTON")
        self.gridLayout_3.addWidget(self.jog_minus_BUTTON, 5, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_3.addWidget(self.line_5, 4, 0, 1, 1)
        self.jog_plus_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jog_plus_BUTTON.sizePolicy().hasHeightForWidth())
        self.jog_plus_BUTTON.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.jog_plus_BUTTON.setFont(font)
        self.jog_plus_BUTTON.setAutoDefault(False)
        self.jog_plus_BUTTON.setDefault(False)
        self.jog_plus_BUTTON.setObjectName("jog_plus_BUTTON")
        self.gridLayout_3.addWidget(self.jog_plus_BUTTON, 5, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.speed_LCD_NUM = QtWidgets.QLCDNumber(self.centralwidget)
        self.speed_LCD_NUM.setFrameShadow(QtWidgets.QFrame.Raised)
        self.speed_LCD_NUM.setLineWidth(0)
        self.speed_LCD_NUM.setObjectName("speed_LCD_NUM")
        self.gridLayout_3.addWidget(self.speed_LCD_NUM, 3, 2, 1, 1)
        self.displacement_WIDGET = CustomWidget(self.centralwidget)
        self.displacement_WIDGET.setObjectName("displacement_WIDGET")
        self.gridLayout_3.addWidget(self.displacement_WIDGET, 0, 0, 1, 1)
        self.position_LCD_NUM = QtWidgets.QLCDNumber(self.centralwidget)
        self.position_LCD_NUM.setLineWidth(0)
        self.position_LCD_NUM.setObjectName("position_LCD_NUM")
        self.gridLayout_3.addWidget(self.position_LCD_NUM, 1, 2, 1, 1)
        self.speed_WIDGET = CustomWidget(self.centralwidget)
        self.speed_WIDGET.setObjectName("speed_WIDGET")
        self.gridLayout_3.addWidget(self.speed_WIDGET, 0, 2, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        self.motor_port_COMBO_BOX = QtWidgets.QComboBox(self.centralwidget)
        self.motor_port_COMBO_BOX.setObjectName("motor_port_COMBO_BOX")
        self.horizontalLayout_8.addWidget(self.motor_port_COMBO_BOX)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_7.addWidget(self.label_12)
        self.encoder_port_COMBO_BOX = QtWidgets.QComboBox(self.centralwidget)
        self.encoder_port_COMBO_BOX.setObjectName("encoder_port_COMBO_BOX")
        self.horizontalLayout_7.addWidget(self.encoder_port_COMBO_BOX)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.connect_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.connect_BUTTON.setObjectName("connect_BUTTON")
        self.horizontalLayout_3.addWidget(self.connect_BUTTON)
        self.disconnect_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.disconnect_BUTTON.setObjectName("disconnect_BUTTON")
        self.horizontalLayout_3.addWidget(self.disconnect_BUTTON)
        self.refresh_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_BUTTON.setObjectName("refresh_BUTTON")
        self.horizontalLayout_3.addWidget(self.refresh_BUTTON)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.port_status_LABEL = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.port_status_LABEL.setFont(font)
        self.port_status_LABEL.setStyleSheet("color: rgb(252, 1, 7);\n"
"")
        self.port_status_LABEL.setObjectName("port_status_LABEL")
        self.horizontalLayout_6.addWidget(self.port_status_LABEL)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_4.setFont(font)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.units_COMBO_BOX = QtWidgets.QComboBox(self.centralwidget)
        self.units_COMBO_BOX.setObjectName("units_COMBO_BOX")
        self.horizontalLayout_4.addWidget(self.units_COMBO_BOX)
        self.microstepping_COMBO_BOX = QtWidgets.QComboBox(self.centralwidget)
        self.microstepping_COMBO_BOX.setObjectName("microstepping_COMBO_BOX")
        self.horizontalLayout_4.addWidget(self.microstepping_COMBO_BOX)
        self.jog_delta_COMBO_BOX = QtWidgets.QComboBox(self.centralwidget)
        self.jog_delta_COMBO_BOX.setObjectName("jog_delta_COMBO_BOX")
        self.horizontalLayout_4.addWidget(self.jog_delta_COMBO_BOX)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.z_displacement_SPIN_BOX = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.z_displacement_SPIN_BOX.setDecimals(3)
        self.z_displacement_SPIN_BOX.setMinimum(-9999.0)
        self.z_displacement_SPIN_BOX.setMaximum(9999.0)
        self.z_displacement_SPIN_BOX.setObjectName("z_displacement_SPIN_BOX")
        self.gridLayout_2.addWidget(self.z_displacement_SPIN_BOX, 3, 1, 1, 1)
        self.x_speed_SPIN_BOX = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.x_speed_SPIN_BOX.setDecimals(3)
        self.x_speed_SPIN_BOX.setMaximum(9999.0)
        self.x_speed_SPIN_BOX.setObjectName("x_speed_SPIN_BOX")
        self.gridLayout_2.addWidget(self.x_speed_SPIN_BOX, 1, 2, 1, 1)
        self.z_enable_CHECK_BOX = QtWidgets.QCheckBox(self.centralwidget)
        self.z_enable_CHECK_BOX.setObjectName("z_enable_CHECK_BOX")
        self.gridLayout_2.addWidget(self.z_enable_CHECK_BOX, 3, 0, 1, 1)
        self.x_enable_CHECK_BOX = QtWidgets.QCheckBox(self.centralwidget)
        self.x_enable_CHECK_BOX.setObjectName("x_enable_CHECK_BOX")
        self.gridLayout_2.addWidget(self.x_enable_CHECK_BOX, 1, 0, 1, 1)
        self.y_enable_CHECK_BOX = QtWidgets.QCheckBox(self.centralwidget)
        self.y_enable_CHECK_BOX.setObjectName("y_enable_CHECK_BOX")
        self.gridLayout_2.addWidget(self.y_enable_CHECK_BOX, 2, 0, 1, 1)
        self.y_displacement_SPIN_BOX = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.y_displacement_SPIN_BOX.setDecimals(3)
        self.y_displacement_SPIN_BOX.setMinimum(-9999.0)
        self.y_displacement_SPIN_BOX.setMaximum(9999.0)
        self.y_displacement_SPIN_BOX.setObjectName("y_displacement_SPIN_BOX")
        self.gridLayout_2.addWidget(self.y_displacement_SPIN_BOX, 2, 1, 1, 1)
        self.y_speed_SPIN_BOX = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.y_speed_SPIN_BOX.setDecimals(3)
        self.y_speed_SPIN_BOX.setMaximum(9999.0)
        self.y_speed_SPIN_BOX.setObjectName("y_speed_SPIN_BOX")
        self.gridLayout_2.addWidget(self.y_speed_SPIN_BOX, 2, 2, 1, 1)
        self.x_displacement_SPIN_BOX = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.x_displacement_SPIN_BOX.setDecimals(3)
        self.x_displacement_SPIN_BOX.setMinimum(-9999.0)
        self.x_displacement_SPIN_BOX.setMaximum(9999.0)
        self.x_displacement_SPIN_BOX.setObjectName("x_displacement_SPIN_BOX")
        self.gridLayout_2.addWidget(self.x_displacement_SPIN_BOX, 1, 1, 1, 1)
        self.z_speed_SPIN_BOX = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.z_speed_SPIN_BOX.setDecimals(3)
        self.z_speed_SPIN_BOX.setMaximum(9999.0)
        self.z_speed_SPIN_BOX.setObjectName("z_speed_SPIN_BOX")
        self.gridLayout_2.addWidget(self.z_speed_SPIN_BOX, 3, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_BUTTON.sizePolicy().hasHeightForWidth())
        self.start_BUTTON.setSizePolicy(sizePolicy)
        self.start_BUTTON.setAutoDefault(False)
        self.start_BUTTON.setDefault(False)
        self.start_BUTTON.setObjectName("start_BUTTON")
        self.horizontalLayout_2.addWidget(self.start_BUTTON)
        self.pause_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_BUTTON.sizePolicy().hasHeightForWidth())
        self.pause_BUTTON.setSizePolicy(sizePolicy)
        self.pause_BUTTON.setObjectName("pause_BUTTON")
        self.horizontalLayout_2.addWidget(self.pause_BUTTON)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stop_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_BUTTON.sizePolicy().hasHeightForWidth())
        self.stop_BUTTON.setSizePolicy(sizePolicy)
        self.stop_BUTTON.setObjectName("stop_BUTTON")
        self.verticalLayout_3.addWidget(self.stop_BUTTON)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.jog_minus_BUTTON.setText(_translate("MainWindow", "Jog -"))
        self.jog_plus_BUTTON.setText(_translate("MainWindow", "Jog +"))
        self.label_4.setText(_translate("MainWindow", "Position"))
        self.label_7.setText(_translate("MainWindow", "Speed"))
        self.label_2.setText(_translate("MainWindow", "1. Arduino Connection"))
        self.label_14.setText(_translate("MainWindow", "Motor Port:"))
        self.label_12.setText(_translate("MainWindow", "Encoder Port:"))
        self.connect_BUTTON.setText(_translate("MainWindow", "Connect"))
        self.disconnect_BUTTON.setText(_translate("MainWindow", "Disconnect"))
        self.refresh_BUTTON.setText(_translate("MainWindow", "Refresh"))
        self.label_5.setText(_translate("MainWindow", "Satus:"))
        self.port_status_LABEL.setText(_translate("MainWindow", "DISCONNECTED"))
        self.label.setText(_translate("MainWindow", "2. Units, Microstepping, Jog Delta"))
        self.label_3.setText(_translate("MainWindow", "3. Motor Settings"))
        self.z_enable_CHECK_BOX.setText(_translate("MainWindow", "Z"))
        self.x_enable_CHECK_BOX.setText(_translate("MainWindow", "X"))
        self.y_enable_CHECK_BOX.setText(_translate("MainWindow", "Y"))
        self.label_8.setText(_translate("MainWindow", "Displacement"))
        self.label_9.setText(_translate("MainWindow", "Speed"))
        self.start_BUTTON.setText(_translate("MainWindow", "Start"))
        self.pause_BUTTON.setText(_translate("MainWindow", "Pause"))
        self.stop_BUTTON.setText(_translate("MainWindow", "Stop"))

from Plotter import CustomWidget