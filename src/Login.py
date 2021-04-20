from PyQt5 import QtCore, QtGui, QtWidgets
import getpass

from PyQt5.QtGui import QCursor,QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame
import os


class Login_Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(495, 508)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        MainWindow.setFont(font)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 350, 411, 21))
        self.label_4.setObjectName("label_4")  
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 370, 411, 21))
        self.label_5.setObjectName("label_5")
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(40, 390, 411, 21))
        self.label_15.setObjectName("label_15")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 450, 61, 21))
        self.label_8.setObjectName("label_8")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 320, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        font.setUnderline(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.user_EID = QtWidgets.QLabel(self.centralwidget)
        self.user_EID.setGeometry(QtCore.QRect(300, 320, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.user_EID.setFont(font)
        self.user_EID.setObjectName("user_EID")
        
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(90, 200, 90, 21))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_node = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_node.setObjectName("label_node")
        self.verticalLayout_4.addWidget(self.label_node)
        
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(180, 200, 120, 21))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.node_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.node_input.setProperty("node_name", "")
        self.node_input.setObjectName("node_input")
        self.verticalLayout_5.addWidget(self.node_input)
        
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(90, 230, 90, 21))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_ns = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_ns.setObjectName("label_ns")
        self.verticalLayout_6.addWidget(self.label_ns)
        
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(180, 230, 120, 21))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ns_input = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.ns_input.setProperty("namespace", "")
        self.ns_input.setObjectName("ns_input")
        self.verticalLayout_7.addWidget(self.ns_input)
        
        self.start_trace = QtWidgets.QPushButton(self.centralwidget)
        self.start_trace.setGeometry(QtCore.QRect(332, 212, 65, 40))
        self.start_trace.setObjectName("start_trace")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 260, 151, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(400, 470, 81, 21))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 150, 120))
        self.label_11.setFont(font)
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setObjectName("label_11")
        
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(160, 60, 300, 80))
        self.label_12.setFont(font)
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setObjectName("label_12")
        
        script_path = os.path.realpath(__file__)
        script_dir = os.path.dirname(script_path)
        path_l11 = os.path.join(script_dir, 'logo.png')
        pix_l11 = QPixmap(path_l11)
        pix_l12 = QPixmap(os.path.join(script_dir, 'Title.png'))
        path_b = os.path.join(script_dir, 'button.png')
        self.label_11.setPixmap(pix_l11)
        self.label_11.setScaledContents(True)
        self.label_12.setPixmap(pix_l12)
        self.label_12.setScaledContents(True)
        
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "5G - Container Capture"))
        self.label_4.setText(_translate("MainWindow", "For \"how to use this tool\", \"any bug\", \"any new requirement\"... "))
        self.label_node.setText(_translate("MainWindow", "Node:"))
        self.node_input.setText(_translate("MainWindow", "pccc-203-11"))
        self.label_ns.setText(_translate("MainWindow", "Namespces:"))
        self.ns_input.setText(_translate("MainWindow", "beets"))
        self.start_trace.setText(_translate("MainWindow", "Start"))
        self.label_8.setText(_translate("MainWindow", "Version 1"))
        self.label_6.setText(_translate("MainWindow", "Welcome using this tool:"))
        self.user_EID.setText(_translate("MainWindow", getpass.getuser().upper()))
