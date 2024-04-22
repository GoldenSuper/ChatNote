from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5 import QtCore

from ui.ui_main_window import Ui_MainWindow
from ui.ui_chat_name_widget import Ui_ChatNameWidget
from connect_db import ConnectDB


class ChatNameWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_ChatNameWidget()
        self.ui.setupUi(self)

        self.lbl_chatName = self.ui.lbl_chatName



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sawc_chatsList = self.ui.sawc_chatsList
        self.VLayout = QVBoxLayout(self.sawc_chatsList)
        self.VLayout.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.VLayout.setContentsMargins(0, 5, 0, 0)


        self.initChats(extesion=".db")
    

    def initChats(self, extesion: str):
        chatNamesList = ConnectDB.GetChatsNames(extesion)
        for el in chatNamesList:
            widget = ChatNameWidget()
            widget.lbl_chatName.setText(el)
            self.VLayout.addWidget(widget)
        