#include "mainwindow.h"

const int maxW = 500;
const int maxH = 27;
const int minW = 250;
const int minH = 27;

void MainWindow::initComboBox() {
    box = new QComboBox();
    box->addItem("RGB");
    box->addItem("XYZ");
    box->addItem("HSV");
    connect(box, SIGNAL(currentIndexChanged(int)), this, SLOT(change_system()));
}

void MainWindow::initColor() {
    colorDialog = new QColorDialog();
    dialogButton = new QPushButton();
    dialogButton->setText("Palette");
    connect(dialogButton, SIGNAL(clicked()), this, SLOT(paletteCalled()));
    b.setStyle(Qt::SolidPattern);
}


void initEdit(QTextEdit **t) {
    *t = new QTextEdit();
    (*t)->setMaximumSize(maxW, maxH);
    (*t)->setMinimumSize(minW, minH);
    (*t)->setText("0");
}

void MainWindow::initFields() {
    initEdit(&R);
    connect(R, SIGNAL(textChanged()), this, SLOT(valueChanged()));
    initEdit(&G);
    connect(G, SIGNAL(textChanged()), this, SLOT(valueChanged()));
    initEdit(&B);
    connect(B, SIGNAL(textChanged()), this, SLOT(valueChanged()));

}

void initSlider(QSlider **s, int minVal, int maxVal) {
    *s = new QSlider();
    (*s)->setOrientation(Qt::Horizontal);
    (*s)->setMaximumSize(maxW, maxH);
    (*s)->setMinimumSize(minW, minH);
    (*s)->setMinimum(minVal);
    (*s)->setMaximum(maxVal);
}

void MainWindow::initSliders() {
    initSlider(&Rs, 0, 255);
    connect(Rs, SIGNAL(valueChanged(int)), this, SLOT(sliderChanged_R()));
    initSlider(&Gs, 0, 255);
    connect(Gs, SIGNAL(valueChanged(int)), this, SLOT(sliderChanged_G()));
    initSlider(&Bs, 0, 255);
    connect(Bs, SIGNAL(valueChanged(int)), this, SLOT(sliderChanged_B()));
}

void MainWindow::initLabels() {
    Rl = new QLabel("R");
    Gl = new QLabel("G");
    Bl = new QLabel("B");
    warning = new QLabel();
    warning->setFixedSize(300,20);
    QFont f;
    f.setBold(true);
    Rl->setFont(f);
    Gl->setFont(f);
    Bl->setFont(f);
}



void MainWindow::initLayout() {
    QHBoxLayout* base, *r, *g, *b;
    QVBoxLayout* colors, *paint, *rgb;
    base = new QHBoxLayout();
    colors = new QVBoxLayout();
    rgb = new QVBoxLayout();
    r = new QHBoxLayout();
    g = new QHBoxLayout();
    b = new QHBoxLayout();
    paint = new QVBoxLayout();

    rgb->addWidget(box);
    rgb->addWidget(warning);

    r->addWidget(Rl);
    r->addWidget(R);
    rgb->addLayout(r);
    rgb->addWidget(Rs);

    g->addWidget(Gl);
    g->addWidget(G);
    rgb->addLayout(g);
    rgb->addWidget(Gs);

    b->addWidget(Bl);
    b->addWidget(B);
    rgb->addLayout(b);
    rgb->addWidget(Bs);

    colors->addLayout(rgb);
    colors->addSpacing(100);


    colors->addWidget(dialogButton);

    base->addLayout(colors);
    base->addLayout(paint);
    setLayout(base);
}
