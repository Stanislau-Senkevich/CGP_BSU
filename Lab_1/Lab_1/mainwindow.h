#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QWidget>
#include <QColorDialog>
#include <QTextEdit>
#include <QSlider>
#include <QPushButton>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QPainter>
#include <QBrush>
#include <QComboBox>
#include <QLabel>

class MainWindow : public QWidget
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:

    void change_system();
    void valueChanged();
    void paletteCalled();

    void sliderChanged_R();
    void sliderChanged_G();
    void sliderChanged_B();


protected:
    QColorDialog* colorDialog;
    QTextEdit *R,*G,*B;
    QSlider *Rs, *Gs, *Bs;
    QPushButton* dialogButton;
    QLabel *Rl, *Gl, *Bl, *warning;
    QColor color;
    QBrush b;
    QPen p;
    QComboBox *box;

    void initColor();
    void initFields();
    void initSliders();
    void initLayout();
    void initComboBox();
    void initLabels();

    void paintEvent(QPaintEvent*);
    void XYZtoRGB(double *r, double *g, double *b, double x, double y, double z);
    void RGBtoXYZ(double r, double g, double b, double *x, double *y, double *z);
};
#endif // MAINWINDOW_H
