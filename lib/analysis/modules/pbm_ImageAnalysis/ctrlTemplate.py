# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/analysis/modules/pbm_ImageAnalysis/ctrlTemplate.ui'
#
# Created: Wed Apr 18 12:58:52 2012
#      by: PyQt4 UI code generator 4.8.3
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
        Form.resize(391, 410)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        Form.setFont(font)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 9, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 10, 0, 1, 1)
        self.ImagePhys_DataStruct = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImagePhys_DataStruct.sizePolicy().hasHeightForWidth())
        self.ImagePhys_DataStruct.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_DataStruct.setFont(font)
        self.ImagePhys_DataStruct.setMaxCount(10)
        self.ImagePhys_DataStruct.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.ImagePhys_DataStruct.setFrame(False)
        self.ImagePhys_DataStruct.setObjectName(_fromUtf8("ImagePhys_DataStruct"))
        self.ImagePhys_DataStruct.addItem(_fromUtf8(""))
        self.ImagePhys_DataStruct.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.ImagePhys_DataStruct, 2, 3, 1, 1)
        self.ImagePhys_ImgMethod = QtGui.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_ImgMethod.setFont(font)
        self.ImagePhys_ImgMethod.setObjectName(_fromUtf8("ImagePhys_ImgMethod"))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.ImagePhys_ImgMethod.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.ImagePhys_ImgMethod, 8, 3, 1, 1)
        self.ImagePhys_ImgNormalize = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_ImgNormalize.setFont(font)
        self.ImagePhys_ImgNormalize.setCheckable(False)
        self.ImagePhys_ImgNormalize.setObjectName(_fromUtf8("ImagePhys_ImgNormalize"))
        self.gridLayout_2.addWidget(self.ImagePhys_ImgNormalize, 8, 0, 1, 1)
        self.ImagePhys_UnBleach = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_UnBleach.setFont(font)
        self.ImagePhys_UnBleach.setObjectName(_fromUtf8("ImagePhys_UnBleach"))
        self.gridLayout_2.addWidget(self.ImagePhys_UnBleach, 7, 0, 1, 1)
        self.ImagePhys_BleachInfo = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_BleachInfo.setFont(font)
        self.ImagePhys_BleachInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ImagePhys_BleachInfo.setFrameShadow(QtGui.QFrame.Sunken)
        self.ImagePhys_BleachInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.ImagePhys_BleachInfo.setObjectName(_fromUtf8("ImagePhys_BleachInfo"))
        self.gridLayout_2.addWidget(self.ImagePhys_BleachInfo, 7, 1, 1, 1)
        self.ImagePhys_BaseStart = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_BaseStart.setFont(font)
        self.ImagePhys_BaseStart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_BaseStart.setMinimum(-5000.0)
        self.ImagePhys_BaseStart.setMaximum(50000.0)
        self.ImagePhys_BaseStart.setObjectName(_fromUtf8("ImagePhys_BaseStart"))
        self.gridLayout_2.addWidget(self.ImagePhys_BaseStart, 9, 1, 1, 1)
        self.ImagePhys_BaseEnd = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_BaseEnd.setFont(font)
        self.ImagePhys_BaseEnd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_BaseEnd.setMinimum(-5000.0)
        self.ImagePhys_BaseEnd.setMaximum(50000.0)
        self.ImagePhys_BaseEnd.setObjectName(_fromUtf8("ImagePhys_BaseEnd"))
        self.gridLayout_2.addWidget(self.ImagePhys_BaseEnd, 10, 1, 1, 1)
        self.ImagePhys_ImgLPF = QtGui.QDoubleSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_ImgLPF.setFont(font)
        self.ImagePhys_ImgLPF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_ImgLPF.setDecimals(1)
        self.ImagePhys_ImgLPF.setMinimum(1.0)
        self.ImagePhys_ImgLPF.setMaximum(1000.0)
        self.ImagePhys_ImgLPF.setSingleStep(10.0)
        self.ImagePhys_ImgLPF.setProperty(_fromUtf8("value"), 200.0)
        self.ImagePhys_ImgLPF.setObjectName(_fromUtf8("ImagePhys_ImgLPF"))
        self.gridLayout_2.addWidget(self.ImagePhys_ImgLPF, 11, 1, 1, 1)
        self.ImagePhys_addRoi = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ImagePhys_addRoi.setFont(font)
        self.ImagePhys_addRoi.setObjectName(_fromUtf8("ImagePhys_addRoi"))
        self.gridLayout_2.addWidget(self.ImagePhys_addRoi, 9, 3, 1, 1)
        self.ImagePhys_clearRoi = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_clearRoi.setFont(font)
        self.ImagePhys_clearRoi.setObjectName(_fromUtf8("ImagePhys_clearRoi"))
        self.gridLayout_2.addWidget(self.ImagePhys_clearRoi, 10, 3, 1, 1)
        self.ImagePhys_RetrieveROI = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_RetrieveROI.setFont(font)
        self.ImagePhys_RetrieveROI.setObjectName(_fromUtf8("ImagePhys_RetrieveROI"))
        self.gridLayout_2.addWidget(self.ImagePhys_RetrieveROI, 11, 3, 1, 1)
        self.ImagePhys_Update = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_Update.setFont(font)
        self.ImagePhys_Update.setObjectName(_fromUtf8("ImagePhys_Update"))
        self.gridLayout_2.addWidget(self.ImagePhys_Update, 14, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.ImagePhys_getRatio = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_getRatio.setFont(font)
        self.ImagePhys_getRatio.setObjectName(_fromUtf8("ImagePhys_getRatio"))
        self.gridLayout_2.addWidget(self.ImagePhys_getRatio, 2, 0, 1, 1)
        self.ImagePhys_ignoreFirst = QtGui.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_ignoreFirst.setFont(font)
        self.ImagePhys_ignoreFirst.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ImagePhys_ignoreFirst.setChecked(True)
        self.ImagePhys_ignoreFirst.setObjectName(_fromUtf8("ImagePhys_ignoreFirst"))
        self.gridLayout_2.addWidget(self.ImagePhys_ignoreFirst, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 1, 1)
        self.ImagePhys_ImgHPF = QtGui.QDoubleSpinBox(self.groupBox)
        self.ImagePhys_ImgHPF.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ImagePhys_ImgHPF.setDecimals(1)
        self.ImagePhys_ImgHPF.setMaximum(100.0)
        self.ImagePhys_ImgHPF.setSingleStep(0.1)
        self.ImagePhys_ImgHPF.setProperty(_fromUtf8("value"), 0.5)
        self.ImagePhys_ImgHPF.setObjectName(_fromUtf8("ImagePhys_ImgHPF"))
        self.gridLayout_2.addWidget(self.ImagePhys_ImgHPF, 12, 1, 1, 1)
        self.ImagePhys_SaveROI = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_SaveROI.setFont(font)
        self.ImagePhys_SaveROI.setObjectName(_fromUtf8("ImagePhys_SaveROI"))
        self.gridLayout_2.addWidget(self.ImagePhys_SaveROI, 12, 3, 1, 1)
        self.ImagePhys_Downsample = QtGui.QComboBox(self.groupBox)
        self.ImagePhys_Downsample.setEditable(True)
        self.ImagePhys_Downsample.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.ImagePhys_Downsample.setObjectName(_fromUtf8("ImagePhys_Downsample"))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.ImagePhys_Downsample.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.ImagePhys_Downsample, 3, 3, 1, 1)
        self.ImagePhys_CorrTool_BL1 = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_CorrTool_BL1.setFont(font)
        self.ImagePhys_CorrTool_BL1.setObjectName(_fromUtf8("ImagePhys_CorrTool_BL1"))
        self.gridLayout_2.addWidget(self.ImagePhys_CorrTool_BL1, 13, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_2.addWidget(self.label_9, 13, 0, 1, 1)
        self.ImagePhys_ExportTiff = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_ExportTiff.setFont(font)
        self.ImagePhys_ExportTiff.setObjectName(_fromUtf8("ImagePhys_ExportTiff"))
        self.gridLayout_2.addWidget(self.ImagePhys_ExportTiff, 14, 3, 1, 1)
        self.ImagePhys_RectSelect = QtGui.QCheckBox(self.groupBox)
        self.ImagePhys_RectSelect.setChecked(True)
        self.ImagePhys_RectSelect.setObjectName(_fromUtf8("ImagePhys_RectSelect"))
        self.gridLayout_2.addWidget(self.ImagePhys_RectSelect, 14, 0, 1, 1)
        self.ImagePhys_CorrTool_HPF = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_CorrTool_HPF.setFont(font)
        self.ImagePhys_CorrTool_HPF.setObjectName(_fromUtf8("ImagePhys_CorrTool_HPF"))
        self.gridLayout_2.addWidget(self.ImagePhys_CorrTool_HPF, 12, 0, 1, 1)
        self.ImagePhys_CorrTool_LPF = QtGui.QPushButton(self.groupBox)
        self.ImagePhys_CorrTool_LPF.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_CorrTool_LPF.setFont(font)
        self.ImagePhys_CorrTool_LPF.setObjectName(_fromUtf8("ImagePhys_CorrTool_LPF"))
        self.gridLayout_2.addWidget(self.ImagePhys_CorrTool_LPF, 11, 0, 1, 1)
        self.ImagePhys_View = QtGui.QComboBox(self.groupBox)
        self.ImagePhys_View.setObjectName(_fromUtf8("ImagePhys_View"))
        self.ImagePhys_View.addItem(_fromUtf8(""))
        self.ImagePhys_View.addItem(_fromUtf8(""))
        self.ImagePhys_View.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.ImagePhys_View, 7, 3, 1, 1)
        self.ImagePhys_NormInfo = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.ImagePhys_NormInfo.setFont(font)
        self.ImagePhys_NormInfo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.ImagePhys_NormInfo.setFrameShadow(QtGui.QFrame.Sunken)
        self.ImagePhys_NormInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.ImagePhys_NormInfo.setObjectName(_fromUtf8("ImagePhys_NormInfo"))
        self.gridLayout_2.addWidget(self.ImagePhys_NormInfo, 8, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Corrections, ROI\'s and Filtering", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Baseline begin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Baseine end", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DataStruct.setItemText(0, QtGui.QApplication.translate("Form", "Flat", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_DataStruct.setItemText(1, QtGui.QApplication.translate("Form", "Interleaved", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(0, QtGui.QApplication.translate("Form", "dF/Fo", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(1, QtGui.QApplication.translate("Form", "median", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(2, QtGui.QApplication.translate("Form", "Norm\'d", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgMethod.setItemText(3, QtGui.QApplication.translate("Form", "G/R", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ImgNormalize.setText(QtGui.QApplication.translate("Form", "Normalize", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_UnBleach.setText(QtGui.QApplication.translate("Form", "Unbleach", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_BleachInfo.setText(QtGui.QApplication.translate("Form", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_addRoi.setText(QtGui.QApplication.translate("Form", "Add Roi", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_clearRoi.setText(QtGui.QApplication.translate("Form", "Clear All ROIs", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_RetrieveROI.setText(QtGui.QApplication.translate("Form", "Retrieve ROI File", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Update.setText(QtGui.QApplication.translate("Form", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Data Struct", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_getRatio.setText(QtGui.QApplication.translate("Form", "Get Ratio Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ignoreFirst.setText(QtGui.QApplication.translate("Form", "  Ignore First Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Downsample", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_SaveROI.setText(QtGui.QApplication.translate("Form", "Save ROI File", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(0, QtGui.QApplication.translate("Form", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(1, QtGui.QApplication.translate("Form", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(2, QtGui.QApplication.translate("Form", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(3, QtGui.QApplication.translate("Form", "10", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_Downsample.setItemText(4, QtGui.QApplication.translate("Form", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_CorrTool_BL1.setText(QtGui.QApplication.translate("Form", "Baseline 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_ExportTiff.setText(QtGui.QApplication.translate("Form", "Export TIFF", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_RectSelect.setText(QtGui.QApplication.translate("Form", "Select with \n"
"rectangle  box", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_CorrTool_HPF.setText(QtGui.QApplication.translate("Form", "HPF Baseline", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_CorrTool_LPF.setText(QtGui.QApplication.translate("Form", "LPF Signal", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setItemText(0, QtGui.QApplication.translate("Form", "Movie", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setItemText(1, QtGui.QApplication.translate("Form", "Reference Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_View.setItemText(2, QtGui.QApplication.translate("Form", "Std Image", None, QtGui.QApplication.UnicodeUTF8))
        self.ImagePhys_NormInfo.setText(QtGui.QApplication.translate("Form", "None", None, QtGui.QApplication.UnicodeUTF8))

