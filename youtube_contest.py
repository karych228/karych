#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QRadioButton, QHBoxLayout, QMessageBox

app = QApplication([])

main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Crazy People')
main_win.move(900,70)
main_win.resize(400,200)

winner = QLabel('В каком году канал получил "золотую кнопку" от YouTube?')
a = QRadioButton("2005")
b = QRadioButton("2010")
c = QRadioButton("2015")
d = QRadioButton("2020")


e = QHBoxLayout()
f = QHBoxLayout()
g = QHBoxLayout()

h = QHBoxLayout()
v_line = QVBoxLayout()



e.addWidget(winner)
f.addWidget(a)
f.addWidget(b)
g.addWidget(c)
g.addWidget(d)
v_line.addLayout(e)
v_line.addLayout(f)
v_line.addLayout(g)
v_line.addLayout(h)
main_win.setLayout(v_line)
def click_true():
    i = QMessageBox()
    i.setText('Верно! Вы выиграли гироскутер')
    i.exec_()


def click_false():
    i = QMessageBox()
    i.setText('Нет, в 2015 году. Вы выиграли фирменный плакат')
    i.exec_()
c.clicked.connect(click_true)
b.clicked.connect(click_false)
d.clicked.connect(click_false)
a.clicked.connect(click_false)
app.exec_()

#подключение библиотек

#создание приложения и главного окна
 
#создание виджетов главного окна
 
#расположение виджетов по лэйаутам

#обработка нажатий на переключатели
 
#отображение окна приложения 