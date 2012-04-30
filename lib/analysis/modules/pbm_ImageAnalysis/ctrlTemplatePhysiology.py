# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/analysis/modules/pbm_ImageAnalysis/ctrlTemplatePhysiology.ui'
#
# Created: Wed Apr 18 22:43:06 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(315, 410)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        Form.setFont(font)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Physiology Analysis Functions", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 1, 1, 2, 1)
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_2.addWidget(self.line_2, 0, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.groupBox)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget = QtGui.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(150, -20, 146, 396))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.ImagePhys_DetectSpikes = QtGui.QPushButton(self.widget)
        self.ImagePhys_DetectSpikes.setGeometry(QtCore.QRect(0, 225, 137, 32))
        self.ImagePhys_DetectSpikes.setMinimumSize(QtCore.QSize(5, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.ImagePhys_DetectSpikes.setFont(font)
        self.ImagePhys_DetectSpikes.setText(QtGui.QApplication.translate("Form", "Detect Spikes", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DetectSpikes.setObjectName(_fromUtf8("ImagePhys_DetectSpikes"))
        self.ImagePhys_burstISI = QtGui.QDoubleSpinBox(self.widget)
        self.ImagePhys_burstISI.setGeometry(QtCore.QRect(0, 140, 106, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_burstISI.setFont(font)
        self.ImagePhys_burstISI.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_burstISI.setDecimals(1)
        self.ImagePhys_burstISI.setMinimum(1.0)
        self.ImagePhys_burstISI.setMaximum(1000.0)
        self.ImagePhys_burstISI.setSingleStep(10.0)
        self.ImagePhys_burstISI.setProperty("value", 100.0)
        self.ImagePhys_burstISI.setObjectName(_fromUtf8("ImagePhys_burstISI"))
        self.ImagePhys_withinBurstISI = QtGui.QDoubleSpinBox(self.widget)
        self.ImagePhys_withinBurstISI.setGeometry(QtCore.QRect(0, 165, 106, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_withinBurstISI.setFont(font)
        self.ImagePhys_withinBurstISI.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_withinBurstISI.setDecimals(1)
        self.ImagePhys_withinBurstISI.setMinimum(1.0)
        self.ImagePhys_withinBurstISI.setMaximum(1000.0)
        self.ImagePhys_withinBurstISI.setSingleStep(2.0)
        self.ImagePhys_withinBurstISI.setProperty("value", 40.0)
        self.ImagePhys_withinBurstISI.setObjectName(_fromUtf8("ImagePhys_withinBurstISI"))
        self.ImagePhys_minBurstSpikes = QtGui.QSpinBox(self.widget)
        self.ImagePhys_minBurstSpikes.setGeometry(QtCore.QRect(0, 190, 106, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_minBurstSpikes.setFont(font)
        self.ImagePhys_minBurstSpikes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_minBurstSpikes.setMinimum(2)
        self.ImagePhys_minBurstSpikes.setMaximum(20)
        self.ImagePhys_minBurstSpikes.setProperty("value", 3)
        self.ImagePhys_minBurstSpikes.setObjectName(_fromUtf8("ImagePhys_minBurstSpikes"))
        self.ImagePhys_STA = QtGui.QPushButton(self.widget_2)
        self.ImagePhys_STA.setGeometry(QtCore.QRect(0, 205, 141, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.ImagePhys_STA.setFont(font)
        self.ImagePhys_STA.setText(QtGui.QApplication.translate("Form", "Spike-triggered Average", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_STA.setObjectName(_fromUtf8("ImagePhys_STA"))
        self.ImagePhys_RevSTA = QtGui.QPushButton(self.widget_2)
        self.ImagePhys_RevSTA.setEnabled(False)
        self.ImagePhys_RevSTA.setGeometry(QtCore.QRect(0, 260, 141, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.ImagePhys_RevSTA.setFont(font)
        self.ImagePhys_RevSTA.setText(QtGui.QApplication.translate("Form", "Rev STA", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_RevSTA.setObjectName(_fromUtf8("ImagePhys_RevSTA"))
        self.ImagePhys_BTA = QtGui.QPushButton(self.widget_2)
        self.ImagePhys_BTA.setGeometry(QtCore.QRect(0, 230, 141, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.ImagePhys_BTA.setFont(font)
        self.ImagePhys_BTA.setText(QtGui.QApplication.translate("Form", "Burst-triggered Average", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_BTA.setObjectName(_fromUtf8("ImagePhys_BTA"))
        self.line_5 = QtGui.QFrame(self.widget_2)
        self.line_5.setGeometry(QtCore.QRect(5, 195, 131, 20))
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(15, 60, 123, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setText(QtGui.QApplication.translate("Form", "Event Thresh", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.ImagePhys_PhysLPF = QtGui.QDoubleSpinBox(self.widget_2)
        self.ImagePhys_PhysLPF.setGeometry(QtCore.QRect(143, 35, 112, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_PhysLPF.setFont(font)
        self.ImagePhys_PhysLPF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_PhysLPF.setMinimum(-5000.0)
        self.ImagePhys_PhysLPF.setMaximum(50000.0)
        self.ImagePhys_PhysLPF.setProperty("value", 2500.0)
        self.ImagePhys_PhysLPF.setObjectName(_fromUtf8("ImagePhys_PhysLPF"))
        self.ImagePhys_PhysThresh = QtGui.QDoubleSpinBox(self.widget_2)
        self.ImagePhys_PhysThresh.setGeometry(QtCore.QRect(143, 60, 112, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_PhysThresh.setFont(font)
        self.ImagePhys_PhysThresh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_PhysThresh.setSuffix(QtGui.QApplication.translate("Form", " pA", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PhysThresh.setDecimals(1)
        self.ImagePhys_PhysThresh.setMinimum(0.0)
        self.ImagePhys_PhysThresh.setMaximum(2000.0)
        self.ImagePhys_PhysThresh.setSingleStep(5.0)
        self.ImagePhys_PhysThresh.setProperty("value", 50.0)
        self.ImagePhys_PhysThresh.setObjectName(_fromUtf8("ImagePhys_PhysThresh"))
        self.ImagePhys_PhysSign = QtGui.QComboBox(self.widget_2)
        self.ImagePhys_PhysSign.setGeometry(QtCore.QRect(140, 87, 118, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_PhysSign.setFont(font)
        self.ImagePhys_PhysSign.setObjectName(_fromUtf8("ImagePhys_PhysSign"))
        self.ImagePhys_PhysSign.addItem(_fromUtf8(""))
        self.ImagePhys_PhysSign.setItemText(0, QtGui.QApplication.translate("Form", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_PhysSign.addItem(_fromUtf8(""))
        self.ImagePhys_PhysSign.setItemText(1, QtGui.QApplication.translate("Form", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7 = QtGui.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(15, 35, 123, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setText(QtGui.QApplication.translate("Form", "LPF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(15, 89, 123, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("Form", "Event Sign", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_6 = QtGui.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(15, 15, 123, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText(QtGui.QApplication.translate("Form", "Physiology", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(5, 175, 131, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setText(QtGui.QApplication.translate("Form", "Minimum # spikes/burst", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_8 = QtGui.QLabel(self.widget_2)
        self.label_8.setGeometry(QtCore.QRect(5, 150, 123, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setText(QtGui.QApplication.translate("Form", "Max burst ISI (msec)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(5, 125, 123, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setText(QtGui.QApplication.translate("Form", "Min Interburst Interval", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 2, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.ImagePhys_PhysSign.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

