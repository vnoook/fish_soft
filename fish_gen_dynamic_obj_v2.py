import sys
import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui
import pprint as pp


class Window(PyQt5.QtWidgets.QWidget):
    checkbox_counter = 0

    def __init__(self):
        super().__init__()

        # self.checkBox = None
        self.dict_obj = {}

        self.pushButton_add = PyQt5.QtWidgets.QPushButton('+', self)
        self.pushButton_add.setGeometry(10, 10, 40, 40)
        self.pushButton_add.clicked.connect(self.add_obj)

        self.pushButton_del = PyQt5.QtWidgets.QPushButton('-', self)
        self.pushButton_del.setGeometry(60, 10, 40, 40)
        self.pushButton_del.clicked.connect(self.del_obj)

    def add_obj(self):
        Window.checkbox_counter = Window.checkbox_counter + 1
        checkbox_name = 'checkbox_' + str(Window.checkbox_counter)

        checkBox = PyQt5.QtWidgets.QCheckBox(self)
        checkBox.setObjectName(checkbox_name)
        checkBox.setVisible(True)
        checkBox.setText(checkbox_name)
        checkBox.setToolTip(checkBox.objectName())
        checkBox.clicked.connect(self.click_checkbox)
        # self.checkBox.setGeometry(10, 50, 40, 40)
        checkBox.resize(20, 20)
        checkBox.adjustSize()
        checkBox.move(10, 50+(30*(Window.checkbox_counter-1)))
        checkBox.show()

        self.dict_obj[Window.checkbox_counter] = checkBox

        pp.pprint(self.dict_obj)
        print('*'*50)

    def del_obj(self):
        if Window.checkbox_counter > 0:
            self.dict_obj[Window.checkbox_counter].deleteLater()

            del self.dict_obj[Window.checkbox_counter]
            Window.checkbox_counter = Window.checkbox_counter - 1

            pp.pprint(self.dict_obj)
            print('*' * 50)

    def click_checkbox(self):
        print(f'{self.sender() = }')
        print(f'{self.sender().objectName() = }')
        print()

        obj1 = self.findChild(type(self.sender()), self.sender().objectName())
        print(f'findChild ... {obj1 = }')
        print(f'{obj1.objectName() = }')
        print()

        obj2 = self.findChildren(type(self.sender()))
        print(f'findChildren ... {obj2 = }')
        print(list(x.objectName() for x in obj2))
        print()

        print(f'список всех объектов в главном ообъекте')
        pp.pprint(self.children())
        print()


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
