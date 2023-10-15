#include "pictures.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Pictures w;
    w.show();
    return a.exec();
}
