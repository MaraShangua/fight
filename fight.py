import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import uic

class second(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("second_ui.ui", self)
        self.show()

class first(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("first_ui.ui", self)

    def slot(self):
        # 두번째 창 실행
        self.w = second()
        self.w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = first()
    window.show()
    sys.exit(app.exec_())
