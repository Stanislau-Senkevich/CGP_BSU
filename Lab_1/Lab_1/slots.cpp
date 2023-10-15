#include "mainwindow.h"

void MainWindow::paletteCalled() {
    QColor save = colorDialog->getColor();
    int ind = box->currentIndex();
    box->setCurrentIndex(0);
    R->setText(QString::number(save.red()));
    G->setText(QString::number(save.green()));
    B->setText(QString::number(save.blue()));
    box->setCurrentIndex(ind);
}


void MainWindow::valueChanged() {
    if (box->currentText() == "RGB") {
        double r,g,b;
        r = R->toPlainText().toDouble();
        g = G->toPlainText().toDouble();
        b = B->toPlainText().toDouble();

        color.setRgb(r,g,b);
        Rs->setValue(int(r));
        Gs->setValue(int(g));
        Bs->setValue(int(b));

    } else if (box->currentText() == "XYZ") {
        double x = R->toPlainText().toDouble();
        double y = G->toPlainText().toDouble();
        double z = B->toPlainText().toDouble();
        double r,g,b;
        XYZtoRGB(&r, &g, &b, x, y, z);
        if (r > 255 || r < 0 || b > 255 || b < 0 || g > 255 || g < 0) {
            warning->setText("Bounds were reached.");
        } else {
            warning->setText("");
            color.setRgb(r,g,b);
        }


        Rs->setValue(x*10000);
        Gs->setValue(y*10000);
        Bs->setValue(z*10000);
    } else {
        int h = R->toPlainText().toInt();
        int s = G->toPlainText().toInt();
        int v = B->toPlainText().toInt();
        color.setHsv(h,s,v);

        Rs->setValue(h);
        Gs->setValue(s);
        Bs->setValue(v);
    }
    b.setColor(color);
    update();
}

void MainWindow::sliderChanged_R() {
    if (box->currentText() == "RGB") {
       R->setText(QString::number(Rs->value()));

    } else if (box->currentText() == "XYZ") {
       R->setText(QString::number(Rs->value()/10000.));

    } else {
        R->setText(QString::number(Rs->value()));
    }
}

void MainWindow::sliderChanged_G() {
    if (box->currentText() == "RGB") {
       G->setText(QString::number(Gs->value()));

    } else if (box->currentText() == "XYZ") {
       G->setText(QString::number(Gs->value()/10000.));

    } else {
       G->setText(QString::number(Gs->value()));
    }
}

void MainWindow::sliderChanged_B() {
    if (box->currentText() == "RGB") {
       B->setText(QString::number(Bs->value()));

    } else if (box->currentText() == "XYZ") {
       B->setText(QString::number(Bs->value()/10000.));

    } else {
       B->setText(QString::number(Bs->value()));
    }
}

void MainWindow::change_system() {
    if (box->currentText() == "RGB") {
        QColor save = color;
        Rs->setMinimum(0);
        Rs->setMaximum(255);
        Gs->setMinimum(0);
        Gs->setMaximum(255);
        Bs->setMinimum(0);
        Bs->setMaximum(255);
        Rl->setText("R");
        Gl->setText("G");
        Bl->setText("B");
        R->setText(QString::number(save.red()));
        G->setText(QString::number(save.green()));
        B->setText(QString::number(save.blue()));
        warning->setText("");

    } else if (box->currentText() == "XYZ") {
        int r,g,b;
        color.getRgb(&r,&g,&b);
        double x,y,z;
        RGBtoXYZ(r,g,b,&x,&y,&z);

        Rs->setMinimum(0);
        Rs->setMaximum(1000000);
        Gs->setMinimum(0);
        Gs->setMaximum(1000000);
        Bs->setMinimum(0);
        Bs->setMaximum(1000000);
        Rl->setText("X");
        Gl->setText("Y");
        Bl->setText("Z");

        R->setText(QString::number(x));
        G->setText(QString::number(y));
        B->setText(QString::number(z));
        color.setRgb(r,g,b);
    } else {
        int h,s,v;
        color.getHsv(&h, &s, &v);

        Rs->setMinimum(0);
        Rs->setMaximum(360);
        Gs->setMinimum(0);
        Gs->setMaximum(255);
        Bs->setMinimum(0);
        Bs->setMaximum(255);
        Rl->setText("H");
        Gl->setText("S");
        Bl->setText("V");
        warning->setText("");

        R->setText(QString::number(h));
        G->setText(QString::number(s));
        B->setText(QString::number(v));
    }
}
