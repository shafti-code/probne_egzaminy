import sys
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QLabel, QPushButton, QSlider, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QWidget

class rgbColorPicker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__current_color = QColor(255, 255, 255)

        self.setWindowTitle("Wzornik kolorów RGB. Wykonał: 0000000000")
        self.setStyleSheet("background-color: #FFF8DC;")
        self.setGeometry(400, 200, 1000, 600)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(20)
        centralWidget.setLayout(main_layout)

        self.__rectangle = QWidget()
        self.__rectangle.setMinimumHeight(150)
        self.__rectangle.setMaximumHeight(150)
        self.__rectangle.setStyleSheet("background-color: white;")
        main_layout.addWidget(self.__rectangle)

        self.__main_label = QLabel("Dobierz kolor suwakami i zapisz przyciskiem:")
        self.__main_label.setStyleSheet("color: black;")
        main_layout.addWidget(self.__main_label)

        HLayout1 = QHBoxLayout()

        self.__labelR = QLabel("R")
        self.__labelR.setStyleSheet("color: black;")
        HLayout1.addWidget(self.__labelR)

        self.__sliderR = QSlider(Qt.Orientation.Horizontal)
        self.__sliderR.setRange(0, 255)
        self.__sliderR.setValue(255)
        HLayout1.addWidget(self.__sliderR)

        self.__labelR2 = QLabel("255")
        self.__labelR2.setStyleSheet("color: black;")
        HLayout1.addWidget(self.__labelR2)

        main_layout.addLayout(HLayout1)

        HLayout2 = QHBoxLayout()

        self.__labelG = QLabel("G")
        self.__labelG.setStyleSheet("color: black;")
        HLayout2.addWidget(self.__labelG)

        self.__sliderG = QSlider(Qt.Orientation.Horizontal)
        self.__sliderG.setRange(0, 255)
        self.__sliderG.setValue(255)
        HLayout2.addWidget(self.__sliderG)

        self.__labelG2 = QLabel("255")
        self.__labelG2.setStyleSheet("color: black;")
        HLayout2.addWidget(self.__labelG2)

        main_layout.addLayout(HLayout2)

        HLayout3 = QHBoxLayout()

        self.__labelB = QLabel("B")
        self.__labelB.setStyleSheet("color: black;")
        HLayout3.addWidget(self.__labelB)

        self.__sliderB = QSlider(Qt.Orientation.Horizontal)
        self.__sliderB.setRange(0, 255)
        self.__sliderB.setValue(255)
        HLayout3.addWidget(self.__sliderB)

        self.__labelB2 = QLabel("255")
        self.__labelB2.setStyleSheet("color: black;")
        HLayout3.addWidget(self.__labelB2)

        main_layout.addLayout(HLayout3)

        self.__pushButton = QPushButton()
        self.__pushButton.setStyleSheet("""
            QPushButton {
                background-color: #CD853F;
                padding: 20px;
                border: none;
                color: white;
            }
            QPushButton:hover {
                background-color: #CD853F;
                border: none;
            }
        """)
        self.__pushButton.setText("Pobierz")
        main_layout.addWidget(self.__pushButton)

        self.__resultLabel = QLabel()
        self.__resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__resultLabel.setStyleSheet("color: black; padding: 20px; background-color: black;")
        self.__resultLabel.setText("255, 255, 255")
        main_layout.addWidget(self.__resultLabel)

        self.__sliderR.valueChanged.connect(self.__set_label_values)
        self.__sliderG.valueChanged.connect(self.__set_label_values)
        self.__sliderB.valueChanged.connect(self.__set_label_values)

        self.__pushButton.clicked.connect(self.__set_widget_color)

        self.__set_widget_color()

    def __set_label_values(self):
        R = self.__sliderR.value()
        G = self.__sliderG.value()
        B = self.__sliderB.value()

        self.__current_color = QColor(R, G, B)

        self.__labelR2.setText(str(R))
        self.__labelG2.setText(str(G))
        self.__labelB2.setText(str(B))

        self.__rectangle.setStyleSheet(f"background-color: {self.__current_color.name()};")
    def __set_widget_color(self):

        self.__resultLabel.setStyleSheet(f"color: black; padding: 20px; background-color: {self.__current_color.name()};")
        self.__resultLabel.setText( f"{self.__current_color.red()}, {self.__current_color.green()}, {self.__current_color.blue()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = rgbColorPicker()
    win.show()
    sys.exit(app.exec())
