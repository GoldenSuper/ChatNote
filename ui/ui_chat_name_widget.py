# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatnamewidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatNameWidget(object):
    def setupUi(self, ChatNameWidget):
        ChatNameWidget.setObjectName("ChatNameWidget")
        ChatNameWidget.resize(271, 31)
        ChatNameWidget.setMinimumSize(QtCore.QSize(271, 31))
        ChatNameWidget.setMaximumSize(QtCore.QSize(271, 31))
        self.btn_removeChat = QtWidgets.QPushButton(ChatNameWidget)
        self.btn_removeChat.setGeometry(QtCore.QRect(235, 0, 31, 31))
        self.btn_removeChat.setText("")
        self.btn_removeChat.setObjectName("btn_removeChat")
        self.btn_editName = QtWidgets.QPushButton(ChatNameWidget)
        self.btn_editName.setGeometry(QtCore.QRect(205, 0, 31, 31))
        self.btn_editName.setText("")
        self.btn_editName.setObjectName("btn_editName")
        self.lbl_chatName = QtWidgets.QLabel(ChatNameWidget)
        self.lbl_chatName.setGeometry(QtCore.QRect(5, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.lbl_chatName.setFont(font)
        self.lbl_chatName.setText("")
        self.lbl_chatName.setObjectName("lbl_chatName")

        self.retranslateUi(ChatNameWidget)
        QtCore.QMetaObject.connectSlotsByName(ChatNameWidget)

    def retranslateUi(self, ChatNameWidget):
        _translate = QtCore.QCoreApplication.translate
        ChatNameWidget.setWindowTitle(_translate("ChatNameWidget", "Form"))