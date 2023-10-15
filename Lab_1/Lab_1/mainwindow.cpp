#include "mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QWidget(parent)
{
    setSizePolicy(QSizePolicy::Expanding,QSizePolicy::Expanding);
    setWindowTitle("Colors");
    initColor();
    initComboBox();
    initFields();
    initSliders();
    initLabels();
    initLayout();
    setMaximumSize(450,450);
    setMinimumSize(350,350);
}

void MainWindow::paintEvent(QPaintEvent*) {
    QPainter* painter = new QPainter(this);
    painter->setBrush(b);
    painter->setBackground(b);
    painter->setPen(p);
    painter->drawRect(width()/8,height()/2 + height()/6 ,width()/8*6,height()/6);
    painter->end();
}

double F(double x) {
    if (x > 0.0031308) {
        return 1.055*pow(x,0.41666) - 0.055;
    } else {
        return 12.92*x;
    }
}

double g(double x) {
    if (x > 0.04045) {
        return pow((x+0.055)/1.055, 2.4);
    }
    return x/12.92;
}

void MainWindow::XYZtoRGB(double *r, double *g, double *b, double x, double y, double z) {
    *r = 3.2406 * x /100 -1.5372 *y/100 -0.4986*z/100;
    *r = F(*r)*255;
    *g = -0.9689 * x /100 + 1.8758 *y/100 + 0.0415*z/100;
    *g = F(*g)*255;
    *b = 0.0557 * x / 100 - 0.2040*y/100 + 1.0570*z/100;
    *b = F(*b)*255;
    return;
}

void MainWindow::RGBtoXYZ(double r, double gr, double b, double *x, double *y, double *z) {
    double Rn, Gn, Bn;
    Rn = g(r/255)*100;
    Gn = g(gr/255)*100;
    Bn = g(b/255)*100;

    *x = 0.412453*Rn + 0.357580*Gn + 0.180423 * Bn;
    *y = 0.212671*Rn + 0.715160*Gn + 0.072169 * Bn;
    *z = 0.019334*Rn + 0.119193*Gn + 0.950227 * Bn;
    return;
}

MainWindow::~MainWindow()
{
}

