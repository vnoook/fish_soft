import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QScrollArea, QFormLayout, QLineEdit, QLabel

class ScrollableForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scrollable Form")
        self.setGeometry(100, 100, 400, 300)

        # Создаем вертикальный скролл-область
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        # Создаем виджет для размещения полей ввода
        self.scroll_content = QWidget()
        self.scroll_layout = QFormLayout(self.scroll_content)

        # Создаем много полей ввода
        for i in range(20):
            label = QLabel(f"Field {i + 1}:")
            entry = QLineEdit()
            self.scroll_layout.addRow(label, entry)

        # Добавляем дополнительные поля для горизонтального скроллинга
        for j in range(30):
            label = QLabel(f"Extra Field {j + 1}:")
            entry = QLineEdit()
            self.scroll_layout.addRow(label, entry)

        # Устанавливаем содержимое скролл-области
        self.scroll_area.setWidget(self.scroll_content)

        # Создаем основной вертикальный layout
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = ScrollableForm()
    form.show()
    sys.exit(app.exec_())
