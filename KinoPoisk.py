import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtGui import QIcon

def getHarryPotter():
    webbrowser.open('https://www.kinopoisk.ru/film/689')

def getStrandela():
    webbrowser.open('https://www.kinopoisk.ru/series/915196/')

def getAloneatHome():
    webbrowser.open('https://www.kinopoisk.ru/film/8124//')


def getStrangerThings():
    webbrowser.open('https://www.kinopoisk.ru/film/8124/?utm_referrer=yandex.ru')


def getSlovopacana():
    webbrowser.open('https://www.kinopoisk.ru/series/5304403/?utm_referrer=www.google.com')

def getPristols():
    webbrowser.open('https://www.kinopoisk.ru/series/464963/')

app = QApplication([])
window = QWidget()
window.setWindowTitle('Кинопоиск')
window.resize(400, 200)

main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 =QHBoxLayout()

text = QLabel('Выберите фильм:')
button1 = QPushButton('Гарри Поттер')
button2 = QPushButton('Очень странные дела')
button3 = QPushButton('Один дома')
button4 = QPushButton('Внешние отмели')
button5 = QPushButton('Слово пацана')
button6 = QPushButton('Игра престолов')

button1.clicked.connect(getHarryPotter)
button2.clicked.connect(getStrandela)
button3.clicked.connect(getAloneatHome)
button4.clicked.connect(getStrangerThings)
button5.clicked.connect(getSlovopacana)
button6.clicked.connect(getPristols)

line1.addWidget(button1, alignment=Qt.AlignCenter)
line1.addWidget(button2, alignment=Qt.AlignCenter)
line1.addWidget(button3, alignment=Qt.AlignCenter)
line2.addWidget(button4, alignment=Qt.AlignCenter)
line2.addWidget(button5, alignment=Qt.AlignCenter)
line2.addWidget(button6, alignment=Qt.AlignCenter)

main_line.addWidget(text, alignment=Qt.AlignCenter)
main_line.addLayout(line1)
main_line.addLayout(line2)

window.setLayout(main_line)
window.show()
app.exec()
