import sys, os

from PySide2.QtCore import QRect, QCoreApplication
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
        desktop = QCoreApplication.instance().desktop()
        screen_counts = desktop.screenCount()
        screen_width = desktop.width()
        screen_height = desktop.height()
        if screen_counts != 1:
            if screen_width not in set([
                1920, 1680, 1600, 1440, 1400, 1366, 1360, 1280, 1152, 1024, 832, 800
            ]):
                screen_width /= desktop.screenCount()

        chat_length = len(self.chats)
        height = 10 + chat_length*95
        self.setGeometry(QRect(screen_width-540, 50, 540, height))
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
    chats = [
        "関係ないかぁ、ぐすん",
        "あー、ごめんね。まあ来世はうまくいくといいね。",
        "//昔じゃなくて今を見てよ。じゃなきゃどっか行っちゃうかもよ"
    ]

    window = ChatPopup(chats)
    window.show()
    sys.exit(app.exec_())
