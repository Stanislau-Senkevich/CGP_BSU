from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QImage, QPainter

import sys
import time
import pygame as pg

w = 1200
h = 1200
MID = (w / 2, h / 2)
DARKGREY = (70, 70, 70)
WHITE = (200, 200, 200)
GRAY = (100, 100, 100)
BLUE = (70, 70, 130)
BLACK = (0, 0, 0)
OXY = (40, 40, 40)
step = 10
x = w / 2
y = h / 2


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Меню")
        self.setFixedSize(235, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        pbc = QtWidgets.QPushButton("Окружность", self)
        pbl = QtWidgets.QPushButton("Пошаговый алгоритм", self)
        pbb = QtWidgets.QPushButton("Алгоритм Брезенхэма", self)
        pbcda = QtWidgets.QPushButton("Алгоритм DDA-линии", self)

        layout.addWidget(pbc)
        layout.addWidget(pbl)
        layout.addWidget(pbb)
        layout.addWidget(pbcda)

        pbc.setFixedSize(220, 30)
        pbl.setFixedSize(220, 30)
        pbb.setFixedSize(220, 30)
        pbcda.setFixedSize(220, 30)

        pbc.clicked.connect(self.circlePB)
        pbl.clicked.connect(self.stepLine)
        pbb.clicked.connect(self.bresenhamLine)
        pbcda.clicked.connect(self.ddaLine)

    def circlePB(self):
        self.hide()
        r, ok = QtWidgets.QInputDialog.getInt(self, 'Input R',
                                              'Enter R: ')

        if ok:
            drawCircle(r * 10)
        self.show()

    def stepLine(self):
        self.hide()
        X1, ok1 = QtWidgets.QInputDialog.getInt(self, 'Input x1',
                                                'Enter X1: ')
        Y1, ok2 = QtWidgets.QInputDialog.getInt(self, 'Input y1',
                                                'Enter Y1: ')
        X2, ok3 = QtWidgets.QInputDialog.getInt(self, 'Input x2',
                                                'Enter X2: ')
        Y2, ok4 = QtWidgets.QInputDialog.getInt(self, 'Input y2',
                                                'Enter Y2: ')

        if ok1 and ok2 and ok3 and ok4:
            drawLineStep(int(X1) * 10 + x, y - int(Y1) * 10, int(X2) * 10 + x, y - int(Y2) * 10)
        self.show()

    def bresenhamLine(self):
        self.hide()
        X1, ok1 = QtWidgets.QInputDialog.getInt(self, 'Input x1',
                                                'Enter X1: ')
        Y1, ok2 = QtWidgets.QInputDialog.getInt(self, 'Input y1',
                                                'Enter Y1: ')
        X2, ok3 = QtWidgets.QInputDialog.getInt(self, 'Input x2',
                                                'Enter X2: ')
        Y2, ok4 = QtWidgets.QInputDialog.getInt(self, 'Input y2',
                                                'Enter Y2: ')

        if ok1 and ok2 and ok3 and ok4:
            drawLineBresenham(int(X1) * 10 + x, y - int(Y1) * 10, int(X2) * 10 + x, y - int(Y2) * 10)
        self.show()

    def ddaLine(self):
        self.hide()
        X1, ok1 = QtWidgets.QInputDialog.getInt(self, 'Input x1',
                                                'Enter X1: ')
        Y1, ok2 = QtWidgets.QInputDialog.getInt(self, 'Input y1',
                                                'Enter Y1: ')
        X2, ok3 = QtWidgets.QInputDialog.getInt(self, 'Input x2',
                                                'Enter X2: ')
        Y2, ok4 = QtWidgets.QInputDialog.getInt(self, 'Input y2',
                                                'Enter Y2: ')

        if ok1 and ok2 and ok3 and ok4:
            start = time.time()
            drawDDA(int(X1) * 10 + x, y - int(Y1) * 10, int(X2) * 10 + x, y - int(Y2) * 10)
            finish = time.time()
            print("DDA-линия", finish - start)
        self.show()



def draw_cords(window):
    coefficient = 10
    for i in range(0, w // coefficient):
        pg.draw.line(window, OXY, (coefficient * i + 5, 0), (coefficient * i + 5, h))
    for i in range(0, h // coefficient):
        pg.draw.line(window, OXY, (0, coefficient * i + 5), (w, coefficient * i + 5))
    pg.draw.line(window, BLACK, (0, y), (w - 10, y), 2)
    pg.draw.line(window, BLACK, (x, 10), (x, h), 2)
    pg.draw.polygon(window, BLACK, ((x - 7, 14), (x + 7, 14), (x, 7)))
    pg.draw.polygon(window, BLACK, ((w - 14, y - 7), (w - 14, y + 7), (w - 7, y)))
    for i in range(0, w, coefficient):
        pg.draw.line(window, BLACK, (i, y - 3), (i, y + 3))
    for i in range(0, h, coefficient):
        pg.draw.line(window, BLACK, (x - 3, i), (x + 3, i))

    font = pg.font.Font('freesansbold.ttf', 13)
    Xtxt = font.render('X', True, BLACK, DARKGREY)
    Ytxt = font.render('Y', True, BLACK, DARKGREY)
    textRectX = Xtxt.get_rect()
    textRectY = Ytxt.get_rect()
    textRectX.center = (w - 10, y - 15)
    textRectY.center = (x + 15, 15)
    window.blit(Xtxt, textRectX)
    window.blit(Ytxt, textRectY)


def mul(A, B):
    ans = [0, 0]
    for i in range(0, 2):
        for j in range(0, 2):
            ans[i] += A[i][j] * B[j]
    return ans


def draw(pos, w):
    pg.draw.rect(w, WHITE, pg.Rect(pos[0] - 5, pos[1] - 5, 10, 10))


def circle(r):
    cords = []
    xStep = 0
    yStep = r
    cords.append([xStep, -yStep])
    while abs(xStep) < abs(yStep):
        mW = abs((xStep + step) ** 2 + yStep ** 2 - r ** 2)
        mH = abs(xStep ** 2 + (yStep - step) ** 2 - r ** 2)
        mD = abs((xStep + step) ** 2 + (yStep - step) ** 2 - r ** 2)
        if min(mH, mW, mD) == mH:
            yStep -= step
        elif min(mH, mW, mD) == mW:
            xStep += step
        elif min(mH, mW, mD) == mD:
            xStep += step
            yStep -= step
        cords.append([xStep, yStep])
    matr1 = ((0, 1),
             (1, 0))
    matr2 = ((-1, 0),
             (0, 1))
    matr3 = ((1, 0),
             (0, -1))

    cords2 = []
    for i in cords:
        cords2.append(mul(matr1, i))
    for i in cords2:
        cords.append(i)
    cords2.clear()
    for i in cords:
        cords2.append(mul(matr2, i))
    for i in cords2:
        cords.append(i)
    cords2.clear()
    for i in cords:
        cords2.append(mul(matr3, i))
    for i in cords2:
        cords.append(i)
    cords2.clear()
    return cords


def stepLineGetCords(x1, y1, x2, y2):
    if x1 == x2:
        cords = [[x1, y1]]
        for i in range(min(y1, y2), max(y1, y2) + 10, 10):
            cords.append([x1, i])
        return cords
    k = (y2 - y1) / (x2 - x1)
    b = (y1 * (x2 - x1) - x1 * (y2 - y1)) / (x2 - x1)

    x1 = (x1 // 10) * 10
    x2 = (x2 // 10) * 10
    y1 = (y1 // 10) * 10
    y2 = (y2 // 10) * 10
    ans = [[x1, y1]]

    if abs(x2 - x1) > abs(y2 - y1):
        for i in range(x1, x2 + 10, 10):
            newY = i * k + b
            newY = (newY // 10) * 10
            ans.append([i, newY])
    else:
        for i in range(y2, y1 + 10, 10):
            newX = (i - b) / k
            newX = (newX // 10) * 10
            ans.append([newX, i])
    return ans


def bresenhamLineGetCords(x1, y1, x2, y2):
    if x1 != x2:
        alph = -(1 / 2)
        k = (y2 - y1) / (x2 - x1)
    else:
        cords = [[x1, y1]]
        for i in range(min(y1, y2), max(y1, y2) + 10, 10):
            cords.append([x1, i])
            return cords

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    x1 = (x1 // 10) * 10
    x2 = (x2 // 10) * 10
    y1 = (y1 // 10) * 10
    ans = [[x1, y1]]

    if abs(x2 - x1) <= abs(y2 - y1):
        c = 10
    else:
        c = 0

    for i in range(x1 + 10, x2 + 10, 10):
        if alph > 0:
            y1 += 10
            alph -= 1
        if alph < -1:
            y1 -= 10
            alph += 1
        ans.append([i, y1 - c])
        alph += k
    return ans


def drawLineBresenham(x1, y1, x2, y2):
    pg.init()
    pg.display.set_caption("Алгоритм Брезенхэма")
    window = pg.display.set_mode((w, h))
    window.fill(DARKGREY)
    draw_cords(window)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    start = time.time()

    if abs(x2 - x1) > abs(y2 - y1):
        cords1 = bresenhamLineGetCords(x1, y1, x2, y2)
    else:
        matr = [[0, 1],
                [1, 0]]
        cords1 = bresenhamLineGetCords(y1, x1, y2, x2)
        for i in range(0, len(cords1)):
            cords1[i] = mul(matr, cords1[i])

    for i in cords1:
        draw((i[0], i[1]), window)
    pg.draw.line(window, BLUE, (x1, y1), (x2, y2), 3)
    finish = time.time()
    print("Алгоритм Брезенхэма ", finish - start)
    pg.display.flip()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()


def drawLineStep(x1, y1, x2, y2):
    pg.init()
    pg.display.set_caption("Пошаговый алгоритм")
    window = pg.display.set_mode((w, h))
    window.fill(DARKGREY)
    draw_cords(window)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    start = time.time()
    if x2 < x1:
        x2, x1 = x1, x2
        y2, y1 = y1, y2
    cords1 = stepLineGetCords(x1, y1, x2, y2)
    for j in cords1:
        draw((j[0], j[1]), window)
    pg.draw.line(window, BLUE, (x1, y1), (x2, y2), 3)
    finish = time.time()
    print("Пошаговый алгоритм", finish - start)
    pg.display.flip()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()


def drawDDA(x1, y1, x2, y2):
    pg.init()
    pg.display.set_caption("DDA-линия")
    window = pg.display.set_mode((w, h))
    window.fill(DARKGREY)
    draw_cords(window)
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    start = time.time()
    cords1 = dda(x1, y1, x2, y2)
    for j in cords1:
        draw((j[0], j[1]), window)
    pg.draw.line(window, BLUE, (x1, y1), (x2, y2), 3)
    finish = time.time()
    print("DDA-линия", finish - start)
    pg.display.flip()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()


def drawCircle(R):
    pg.init()
    pg.display.set_caption("Окружность")
    window = pg.display.set_mode((w, h))
    window.fill(DARKGREY)
    draw_cords(window)
    start = time.time()
    cords1 = circle(R)
    for j in cords1:
        draw((x + j[0], y - j[1]), window)
    pg.draw.circle(window, BLUE, MID, R, 3)
    finish = time.time()
    print("Окружность", finish - start)
    pg.display.flip()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()


def dda(x1, y1, x2, y2):
    Dx = (x2 - x1)
    Dy = (y2 - y1)
    if abs(Dy) > abs(Dx):
        L = Dy
        step = -10
    else:
        L = Dx
        step = 10
    ans = [[x1 // 10 * 10, y1 // 10 * 10]]
    for i in range(0, L, step):
        x1 = x1 + (Dx / L) * step
        y1 = y1 + (Dy / L) * step
        ans.append([x1 // 10 * 10, y1 // 10 * 10])
    return ans
