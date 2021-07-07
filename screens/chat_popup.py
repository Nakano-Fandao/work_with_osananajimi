import sys, os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

sys.path.append(os.path.join(os.path.dirname(__file__), "../UI"))
from ui_chat_popup import Ui_ChatPopup

class ChatPopup(QDialog):
    def __init__(self, chats):
        super().__init__()
        self.ui = Ui_ChatPopup()
        self.ui.setupUi(self)
        self.chats = chats
        self.setupChats()

        self.ui.chatList.clicked.connect(self.accept)

    def setupChats(self):
        chat_length = len(self.chats)
        height = 10 + chat_length*95
        self.setGeometry(QRect(300, 100, 540, height))
        for i in range(chat_length):
            QListWidgetItem(self.ui.chatList)
            chatItem = self.ui.chatList.item(i)
            chatItem.setText(QCoreApplication.translate("ChatPopup", self.chats[i], None));

    @property
    def selected_item(self):
        self.close()
        item = self.ui.chatList.selectedItems()[0].text()
        return ("", item)[item != ""]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatPopup()
    window.show()
    sys.exit(app.exec_())
