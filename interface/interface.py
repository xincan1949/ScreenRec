# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 22))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBaidu_API_USES_the_general_scene_text_recognition_API_provided_by_Baidu = QtWidgets.QAction(MainWindow)
        self.actionBaidu_API_USES_the_general_scene_text_recognition_API_provided_by_Baidu.setObjectName("actionBaidu_API_USES_the_general_scene_text_recognition_API_provided_by_Baidu")
        self.actionshenchenshao = QtWidgets.QAction(MainWindow)
        self.actionshenchenshao.setObjectName("actionshenchenshao")
        self.menufile.addAction(self.actionshenchenshao)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox.activated['int'].connect(self.comboBox.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "超好用的截屏识别助手"))
        self.label.setText(_translate("MainWindow", "识别方式："))
        self.pushButton.setText(_translate("MainWindow", "识别文字"))
        self.comboBox.setItemText(0, _translate("MainWindow", "本地（PaddleHub）"))
        self.comboBox.setItemText(1, _translate("MainWindow", "百度API（标准版）"))
        self.comboBox.setItemText(2, _translate("MainWindow", "百度API（高精度版）"))
        self.checkBox.setText(_translate("MainWindow", "保留文字版式"))
        self.checkBox_2.setText(_translate("MainWindow", "复制到剪切板"))
        self.menufile.setTitle(_translate("MainWindow", "Author"))
        self.actionBaidu_API_USES_the_general_scene_text_recognition_API_provided_by_Baidu.setText(_translate("MainWindow", "Baidu API USES the general scene text recognition API provided by Baidu"))
        self.actionshenchenshao.setText(_translate("MainWindow", "shaoshenchen"))
