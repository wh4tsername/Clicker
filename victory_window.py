from import_modules import *


class OkButton(QPushButton):
    def __init__(self, window):
        super().__init__("Ok", window)
        self.width = 70
        self.height = 25
        self.top = window.height - self.height - 5
        self.left = window.width / 2 - self.width / 2 - 5 / 2
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.clicked.connect(window.close)


class VictoryLabel(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = window.width - 10
        self.height = window.height - 40
        self.top = 5
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setPixmap(QPixmap("img/victory.png"))
        self.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)


class Frame(QLabel):
    def __init__(self, window):
        super().__init__(window)
        self.width = window.width - 10
        self.height = window.height - 40
        self.top = 5
        self.left = 5
        self.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.move(self.left, self.top)
        self.setFrameStyle(QLabel.Box)


class VictoryWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.top = 0
        self.left = 0
        self.width = 250
        self.height = 150
        self.title = "Victory!"
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width,
                          self.height)
        self.move(self.left, self.top)

        # buttons
        self.ok_button = OkButton(self)

        # labels
        self.help_label = VictoryLabel(self)

        # frame
        self.frame = Frame(self)

        self.show()
