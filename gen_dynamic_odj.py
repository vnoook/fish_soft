import pprint
import sys
import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui
import pprint as pp


class Window(PyQt5.QtWidgets.QWidget):
    checkbox_number = 0

    def __init__(self):
        super().__init__()

        self.vlayout = PyQt5.QtWidgets.QVBoxLayout()

        self.pushButton_add = PyQt5.QtWidgets.QPushButton('+', self)
        self.pushButton_add.clicked.connect(self.add_checkbox)

        self.pushButton_del = PyQt5.QtWidgets.QPushButton('-', self)
        self.pushButton_del.clicked.connect(self.del_checkbox)

        self.vlayout.addWidget(self.pushButton_add)
        self.vlayout.addWidget(self.pushButton_del)

        # self.checkBox = PyQt5.QtWidgets.QCheckBox(self)
        # self.vlayout.addWidget(self.checkBox)
        self.setLayout(self.vlayout)

        self.dict_obj = {}

    def add_checkbox(self):
        Window.checkbox_number = Window.checkbox_number + 1
        checkbox_name = 'checkbox_' + str(Window.checkbox_number)

        self.checkBox = PyQt5.QtWidgets.QCheckBox()
        self.checkBox.setObjectName(checkbox_name)
        self.checkBox.setText(checkbox_name)
        self.checkBox.setToolTip(self.checkBox.objectName())
        self.checkBox.clicked.connect(self.click_checkbox)

        self.dict_obj[Window.checkbox_number] = self.checkBox
        pp.pprint(self.dict_obj)
        print('*'*50)

        self.vlayout.addWidget(self.checkBox)

    def del_checkbox(self):
        if Window.checkbox_number > 0:
            Window.checkbox_number = Window.checkbox_number - 1
            print(Window.checkbox_number)
        pass

    def click_checkbox(self):
        print(self.sender().objectName())
        pass


# создание основного окна
def main_app():
    application = PyQt5.QtWidgets.QApplication(sys.argv)
    application.setStyle('Fusion')
    window = Window()
    window.setWindowTitle('Динамическое добавление объектов')
    window.resize(400, 300)
    window.show()
    sys.exit(application.exec_())


# запуск основного окна
if __name__ == '__main__':
    main_app()