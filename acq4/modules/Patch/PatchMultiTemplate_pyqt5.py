# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acq4/modules/Patch/PatchMultiTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(307, 609)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_4 = QtWidgets.QSplitter(Form)
        self.splitter_4.setOrientation(Qt.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(Qt.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.startBtn.setCheckable(True)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        self.recordBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.recordBtn.setCheckable(True)
        self.recordBtn.setObjectName("recordBtn")
        self.horizontalLayout.addWidget(self.recordBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.modeLayout = QtWidgets.QVBoxLayout()
        self.modeLayout.setObjectName("modeLayout")
        self.verticalLayout.addLayout(self.modeLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.delayTimeSpin = SpinBox(self.layoutWidget)
        self.delayTimeSpin.setMinimum(1.0)
        self.delayTimeSpin.setMaximum(10000.0)
        self.delayTimeSpin.setSingleStep(1.0)
        self.delayTimeSpin.setObjectName("delayTimeSpin")
        self.horizontalLayout_2.addWidget(self.delayTimeSpin)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pulseTimeSpin = SpinBox(self.layoutWidget)
        self.pulseTimeSpin.setSingleStep(1.0)
        self.pulseTimeSpin.setObjectName("pulseTimeSpin")
        self.horizontalLayout_3.addWidget(self.pulseTimeSpin)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.cycleTimeSpin = SpinBox(self.layoutWidget)
        self.cycleTimeSpin.setSingleStep(1.0)
        self.cycleTimeSpin.setProperty("value", 0.2)
        self.cycleTimeSpin.setObjectName("cycleTimeSpin")
        self.horizontalLayout_5.addWidget(self.cycleTimeSpin)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.averageSpin = QtWidgets.QSpinBox(self.layoutWidget)
        self.averageSpin.setMinimum(1)
        self.averageSpin.setMaximum(100)
        self.averageSpin.setProperty("value", 1)
        self.averageSpin.setObjectName("averageSpin")
        self.horizontalLayout_4.addWidget(self.averageSpin)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(Qt.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.patchPlot = PlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patchPlot.sizePolicy().hasHeightForWidth())
        self.patchPlot.setSizePolicy(sizePolicy)
        self.patchPlot.setObjectName("patchPlot")
        self.commandPlot = PlotWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandPlot.sizePolicy().hasHeightForWidth())
        self.commandPlot.setSizePolicy(sizePolicy)
        self.commandPlot.setObjectName("commandPlot")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(Qt.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.widget = QtWidgets.QWidget(self.splitter_3)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.restingPotentialLabel = QtWidgets.QLabel(self.widget)
        self.restingPotentialLabel.setMinimumSize(Qt.QSize(140, 0))
        font = Qt.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.restingPotentialLabel.setFont(font)
        self.restingPotentialLabel.setAlignment(Qt.Qt.AlignLeading|Qt.Qt.AlignLeft|Qt.Qt.AlignVCenter)
        self.restingPotentialLabel.setObjectName("restingPotentialLabel")
        self.gridLayout.addWidget(self.restingPotentialLabel, 3, 1, 1, 1)
        self.fitErrorCheck = QtWidgets.QCheckBox(self.widget)
        self.fitErrorCheck.setObjectName("fitErrorCheck")
        self.gridLayout.addWidget(self.fitErrorCheck, 6, 0, 1, 1)
        self.drawFitCheck = QtWidgets.QCheckBox(self.widget)
        self.drawFitCheck.setChecked(True)
        self.drawFitCheck.setObjectName("drawFitCheck")
        self.gridLayout.addWidget(self.drawFitCheck, 0, 1, 1, 1)
        self.inputResistanceCheck = QtWidgets.QCheckBox(self.widget)
        font = Qt.QFont()
        font.setPointSize(11)
        self.inputResistanceCheck.setFont(font)
        self.inputResistanceCheck.setChecked(True)
        self.inputResistanceCheck.setObjectName("inputResistanceCheck")
        self.gridLayout.addWidget(self.inputResistanceCheck, 1, 0, 1, 1)
        self.accessResistanceLabel = QtWidgets.QLabel(self.widget)
        font = Qt.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.accessResistanceLabel.setFont(font)
        self.accessResistanceLabel.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.accessResistanceLabel.setObjectName("accessResistanceLabel")
        self.gridLayout.addWidget(self.accessResistanceLabel, 2, 1, 1, 1)
        self.inputResistanceLabel = QtWidgets.QLabel(self.widget)
        font = Qt.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.inputResistanceLabel.setFont(font)
        self.inputResistanceLabel.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.inputResistanceLabel.setObjectName("inputResistanceLabel")
        self.gridLayout.addWidget(self.inputResistanceLabel, 1, 1, 1, 1)
        self.accessResistanceCheck = QtWidgets.QCheckBox(self.widget)
        font = Qt.QFont()
        font.setPointSize(11)
        self.accessResistanceCheck.setFont(font)
        self.accessResistanceCheck.setObjectName("accessResistanceCheck")
        self.gridLayout.addWidget(self.accessResistanceCheck, 2, 0, 1, 1)
        self.restingCurrentLabel = QtWidgets.QLabel(self.widget)
        self.restingCurrentLabel.setMinimumSize(Qt.QSize(120, 0))
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.restingCurrentLabel.setFont(font)
        self.restingCurrentLabel.setAlignment(Qt.Qt.AlignLeading|Qt.Qt.AlignLeft|Qt.Qt.AlignVCenter)
        self.restingCurrentLabel.setObjectName("restingCurrentLabel")
        self.gridLayout.addWidget(self.restingCurrentLabel, 4, 1, 1, 1)
        self.capacitanceCheck = QtWidgets.QCheckBox(self.widget)
        self.capacitanceCheck.setObjectName("capacitanceCheck")
        self.gridLayout.addWidget(self.capacitanceCheck, 5, 0, 1, 1)
        self.restingPotentialCheck = QtWidgets.QCheckBox(self.widget)
        font = Qt.QFont()
        font.setPointSize(11)
        self.restingPotentialCheck.setFont(font)
        self.restingPotentialCheck.setObjectName("restingPotentialCheck")
        self.gridLayout.addWidget(self.restingPotentialCheck, 3, 0, 1, 1)
        self.restingCurrentCheck = QtWidgets.QCheckBox(self.widget)
        self.restingCurrentCheck.setObjectName("restingCurrentCheck")
        self.gridLayout.addWidget(self.restingCurrentCheck, 4, 0, 1, 1)
        self.capacitanceLabel = QtWidgets.QLabel(self.widget)
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.capacitanceLabel.setFont(font)
        self.capacitanceLabel.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.capacitanceLabel.setObjectName("capacitanceLabel")
        self.gridLayout.addWidget(self.capacitanceLabel, 5, 1, 1, 1)
        self.fitErrorLabel = QtWidgets.QLabel(self.widget)
        font = Qt.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.fitErrorLabel.setFont(font)
        self.fitErrorLabel.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.fitErrorLabel.setObjectName("fitErrorLabel")
        self.gridLayout.addWidget(self.fitErrorLabel, 6, 1, 1, 1)
        self.resetBtn = QtWidgets.QToolButton(self.widget)
        self.resetBtn.setObjectName("resetBtn")
        self.gridLayout.addWidget(self.resetBtn, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 7, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.plotLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.plotLayout.setContentsMargins(0, 0, 0, 0)
        self.plotLayout.setSpacing(0)
        self.plotLayout.setObjectName("plotLayout")
        self.verticalLayout_2.addWidget(self.splitter_4)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(-1)
        Qt.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = Qt.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.startBtn.setText(_translate("Form", "Start"))
        self.recordBtn.setText(_translate("Form", "Record"))
        self.label_4.setText(_translate("Form", "Delay Length"))
        self.delayTimeSpin.setSuffix(_translate("Form", "s"))
        self.label_3.setText(_translate("Form", "Pulse Length"))
        self.pulseTimeSpin.setSuffix(_translate("Form", "s"))
        self.label.setText(_translate("Form", "Cycle Time"))
        self.cycleTimeSpin.setSuffix(_translate("Form", "s"))
        self.label_2.setText(_translate("Form", "Average"))
        self.restingPotentialLabel.setText(_translate("Form", "0"))
        self.fitErrorCheck.setText(_translate("Form", "Fit Error"))
        self.drawFitCheck.setText(_translate("Form", "Draw Fit"))
        self.inputResistanceCheck.setText(_translate("Form", "Input Res."))
        self.accessResistanceLabel.setText(_translate("Form", "0"))
        self.inputResistanceLabel.setText(_translate("Form", "0"))
        self.accessResistanceCheck.setText(_translate("Form", "Access Res."))
        self.restingCurrentLabel.setText(_translate("Form", "0"))
        self.capacitanceCheck.setText(_translate("Form", "Capacitance"))
        self.restingPotentialCheck.setText(_translate("Form", "Rest Potential"))
        self.restingCurrentCheck.setText(_translate("Form", "Rest Current"))
        self.capacitanceLabel.setText(_translate("Form", "0"))
        self.fitErrorLabel.setText(_translate("Form", "0"))
        self.resetBtn.setText(_translate("Form", "Reset History"))

from acq4.pyqtgraph import PlotWidget, SpinBox
