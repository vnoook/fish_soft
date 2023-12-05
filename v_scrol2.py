import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QScrollBar


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Scroll Bar Example')
        self.setGeometry(100, 100, 500, 500)

        self.text_edit = QTextEdit()
        self.text_edit.setPlainText(
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam suscipit luctus nulla, nec bibendum magna'
            ' commodo vel. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;'
            ' Etiam vestibulum vehicula nulla, vitae luctus dolor aliquam et. Donec interdum, tortor ut finibus rhoncus,'
            ' est orci egestas arcu, quis finibus nisl leo ac sapien. Nam in sem vel dolor faucibus molestie. Proin vel'
            ' risus cursus, imperdiet urna at, luctus erat. Fusce eu nulla vitae lectus pretium pulvinar.'
            ' Nullam fringilla, magna eu tincidunt faucibus, enim libero dictum purus, at malesuada ipsum quam bibendum'
            ' ex. Curabitur et nunc aliquam, consectetur turpis aliquam, molestie ipsum. Proin accumsan maximus'
            ' vestibulum. Morbi ut eleifend libero. Sed consectetur odio justo, quis placerat lectus ornare a.""")

        self.scrollbar = QScrollBar()
        self.scrollbar.setMaximum(int(self.text_edit.document().size().height()))
        self.scrollbar.sliderMoved.connect(self.text_edit.verticalScrollBar().setValue)

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.scrollbar)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
