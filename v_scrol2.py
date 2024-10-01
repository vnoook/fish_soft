import sys
import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui


class Example(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create main layout
        main_layout = PyQt5.QtWidgets.QHBoxLayout(self)

        # Create widget to hold checkboxes
        self.checkbox_widget = PyQt5.QtWidgets.QWidget()
        checkbox_layout = PyQt5.QtWidgets.QGridLayout(self.checkbox_widget)

        # Create checkboxes (5 columns x 100 rows)
        self.checkboxes = []
        for row in range(20):
            for col in range(20):
                checkbox = PyQt5.QtWidgets.QCheckBox(f"{row * 5 + col + 1}", self)
                self.checkboxes.append(checkbox)
                checkbox.setFixedSize(PyQt5.QtCore.QSize(15, 15))  # Set checkbox size
                checkbox_layout.addWidget(checkbox, row, col)

        # Create scroll area to hold checkboxes widget
        self.scroll_area = PyQt5.QtWidgets.QScrollArea(self)
        self.scroll_area.setWidget(self.checkbox_widget)
        self.scroll_area.setWidgetResizable(False)  # Prevent resizing of checkbox widget

        # Add scroll area and scroll bar to main layout
        main_layout.addWidget(self.scroll_area)

        # Set layout and window properties
        self.setLayout(main_layout)
        self.setGeometry(300, 300, 700, 600)  # Set form size
        self.setWindowTitle('QScrollBar')
        self.show()


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
