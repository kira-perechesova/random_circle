import sys
import random
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        R = random.randint(20, 100)
        self.qp.setBrush(QColor(*[random.randint(0, 255) for _ in range(3)]))
        self.qp.drawEllipse(QPointF(self.coords_[0], self.coords_[1]), R, R)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Рисование')

        self.circle_button = QPushButton('circle', self)
        self.circle_button.setGeometry(100, 100, 100, 100)
        self.circle_button.clicked.connect(self.mousePressEvent)

    def mousePressEvent(self, event):
        self.coords_ = [random.randint(0, 800), random.randint(0, 800)]
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())