import sys
import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui


# класс главного окна
class WindowMain(PyQt5.QtWidgets.QMainWindow):
    """Класс главного окна"""

    # описание главного окна
    def __init__(self):
        super().__init__()

        # переменные
        pass

        # главное окно, надпись на нём и размеры
        self.setWindowTitle('setWindowTitle')
        self.setGeometry(450, 100, 700, 490)

        # ОБЪЕКТЫ НА ФОРМЕ
        # label_
        self.label_ = PyQt5.QtWidgets.QLabel(self)
        self.label_.setObjectName('label_')
        self.label_.setText('label_')
        self.label_.setGeometry(PyQt5.QtCore.QRect(10, 10, 150, 40))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.label_.setFont(font)
        self.label_.adjustSize()
        self.label_.setToolTip(self.label_.objectName())

        # toolButton_
        self.toolButton_ = PyQt5.QtWidgets.QPushButton(self)
        self.toolButton_.setObjectName('toolButton_')
        self.toolButton_.setText('...')
        self.toolButton_.setGeometry(PyQt5.QtCore.QRect(10, 40, 50, 20))
        self.toolButton_.setFixedWidth(50)
        # self.toolButton_.clicked.connect(self.select_file)
        self.toolButton_.setToolTip(self.toolButton_.objectName())

        # lineEdit_
        self.lineEdit_ = PyQt5.QtWidgets.QLineEdit(self)
        self.lineEdit_.setObjectName('lineEdit_')
        self.lineEdit_.setPlaceholderText('lineEdit_')
        self.lineEdit_.setText('lineEdit_')
        self.lineEdit_.setGeometry(PyQt5.QtCore.QRect(10, 160, 110, 20))
        self.lineEdit_.setClearButtonEnabled(True)
        self.lineEdit_.setEnabled(False)
        self.lineEdit_.setToolTip(self.lineEdit_.objectName())

        # pushButton_
        self.pushButton_ = PyQt5.QtWidgets.QPushButton(self)
        self.pushButton_.setObjectName('pushButton_')
        self.pushButton_.setEnabled(False)
        self.pushButton_.setText('pushButton_')
        self.pushButton_.setGeometry(PyQt5.QtCore.QRect(10, 360, 180, 25))
        self.pushButton_.setFixedWidth(130)
        # self.pushButton_.clicked.connect(self.init_thread)
        self.pushButton_.setToolTip(self.pushButton_.objectName())

        # EXIT
        # button_exit
        self.button_exit = PyQt5.QtWidgets.QPushButton(self)
        self.button_exit.setObjectName('button_exit')
        self.button_exit.setText('Выход')
        self.button_exit.setGeometry(PyQt5.QtCore.QRect(10, 450, 180, 25))
        self.button_exit.setFixedWidth(50)
        self.button_exit.clicked.connect(self.click_on_btn_exit)
        self.button_exit.setToolTip(self.button_exit.objectName())

    # событие - нажатие на кнопку Выход
    @staticmethod
    def click_on_btn_exit():
        sys.exit()


# создание основного окна
def main_app():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app_window_main = WindowMain()
    app_window_main.show()
    sys.exit(app.exec_())


# запуск основного окна
if __name__ == '__main__':
    main_app()
