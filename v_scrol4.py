import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel


class ScrollAreaExample(QMainWindow):
    def __init__(self):
        super().__init__()

        scroll_area = QScrollArea()
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        for i in range(50):
            label = QLabel(f'Label {i}')
            layout.addWidget(label)

        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(content_widget)

        self.setCentralWidget(scroll_area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScrollAreaExample()
    window.show()
    sys.exit(app.exec_())

##В этом примере создается главное окно приложения и добавляется в него QScrollArea.
##Затем создается виджет contentwidget, в который добавляются дочерние виджеты QLabel.
##После этого contentwidget устанавливается в качестве содержимого QScrollArea с помощью методов setWidgetResizable и setWidget.
##Когда приложение запускается, вы увидите QScrollArea с возможностью прокрутки, содержащий много меток QLabel.
