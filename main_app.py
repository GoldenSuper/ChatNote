from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDialog, QMessageBox, QPushButton
from PyQt5 import QtCore

from ui.ui_main_window import Ui_MainWindow
from ui.ui_chat_name_widget import Ui_ChatNameWidget
from ui.ui_input_dialog import Ui_InputDialog
from ui.ui_message_widget import Ui_MessageWidget
from connect_db import ConnectDB


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.sawc_chatsList = self.ui.sawc_chatsList

        self.VLayout = QVBoxLayout(self.sawc_chatsList)
        self.VLayout.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.VLayout.setContentsMargins(0, 5, 0, 0)

        self.btn_addNewChat = self.ui.btn_addNewChat
        self.btn_addNewChat.clicked.connect(self.btn_addNewChat_onclicked)

        self.initChats(extesion=".db")
    

    def initChats(self, extesion: str):
        chatNamesList = ConnectDB.GetChatsNames(extesion)
        for el in chatNamesList:
            widget = ChatNameWidget(self)
            widget.lbl_chatName.setText(el)
            self.VLayout.addWidget(widget)
    
    def btn_addNewChat_onclicked(self):
        widget = ChatNameWidget(self)
        dialog = CreateChatDialog(self, widget)
        dialog.show()
        dialog.exec()


class MessageWidget(QWidget):
    def __init__(self, mainwindow: MainWindow) -> None:
        super().__init__()

        self.ui = Ui_MessageWidget()
        self.ui.setupUi(self)

        self.mainwindow = mainwindow

        self.lbl_messageText = self.ui.lbl_messageText
        self.btn_editMessage = self.ui.btn_editMessage
        self.btn_removeMessage = self.ui.btn_removeMessage

        self.btn_editMessage.clicked.connect(self.btn_editMessage_onclicked)
        self.btn_removeMessage.clicked.connect(self.btn_removeMessage_onclicked)
    
    def btn_editMessage_onclicked(self):
        pass

    def btn_removeMessage_onclicked(self):
        self.deleteLater()


class ChatNameWidget(QWidget):
    def __init__(self, mainwindow: MainWindow) -> None:
        super().__init__()

        self.ui = Ui_ChatNameWidget()
        self.ui.setupUi(self)

        self.mainwindow = mainwindow

        self.lbl_chatName = self.ui.lbl_chatName
        self.btn_editName = self.ui.btn_editName
        self.btn_removeChat = self.ui.btn_removeChat

        self.mouseReleaseEvent = self.widget_onclicked
        self.btn_editName.clicked.connect(self.btn_editName_onclicked)
        self.btn_removeChat.clicked.connect(self.btn_removeChat_onclicked)

    def btn_editName_onclicked(self) -> None:
        dialog = ChangeChatNameDialog(self.mainwindow, self)
        dialog.show()
        dialog.exec()

    def btn_removeChat_onclicked(self) -> None:
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Удаление чата")
        msgBox.setText(f"Вы точно хотите удалить чат {self.lbl_chatName.text()}?")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        msgBox.buttonClicked.connect(self.btnBox_removeChat_onclicked)

        msgBox.show()
        msgBox.exec_()

    def btnBox_removeChat_onclicked(self, btn):
        if btn.text() == "OK":
            self.deleteLater()
            del self
            
            
    def widget_onclicked(self, event) -> None:
        #open chat
        print("click")
        pass


class InputDialog(QDialog):
    def __init__(self, mainwindow: MainWindow) -> None:
        super().__init__()

        self.ui = Ui_InputDialog()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.mainwindow = mainwindow
        self.textEdit = self.ui.textEdit
        self.buttonBox = self.ui.buttonBox


class CreateChatDialog(InputDialog):
    def __init__(self, mainwindow: MainWindow, widget: ChatNameWidget) -> None:
        super().__init__(mainwindow)

        self.widget = widget
        self.setWindowTitle("Создать чат")
        self.buttonBox.accepted.connect(self.accepted)

    def accepted(self):
        if 0 < len(self.textEdit.toPlainText()) <= 16: 
            self.widget.lbl_chatName.setText(self.textEdit.toPlainText())
            self.mainwindow.VLayout.addWidget(self.widget)
            
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Длина названия должна быть от 1 до 16 символов.")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Ok)

            msgBox.exec_()


class ChangeChatNameDialog(InputDialog):
    def __init__(self, mainwindow: MainWindow, widget: ChatNameWidget) -> None:
        super().__init__(mainwindow)

        self.widget = widget
        self.setWindowTitle("Изменить название")
        self.buttonBox.accepted.connect(self.accepted)

    def accepted(self):
        if 0 < len(self.textEdit.toPlainText()) <= 16: 
            self.widget.lbl_chatName.setText(self.textEdit.toPlainText())
            
        else:
            msgBox = QMessageBox()
            msgBox.setWindowTitle("Ошибка")
            msgBox.setText("Длина названия должна быть от 1 до 16 символов.")
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setStandardButtons(QMessageBox.Ok)

            msgBox.exec_()