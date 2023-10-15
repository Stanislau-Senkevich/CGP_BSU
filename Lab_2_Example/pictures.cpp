#include "pictures.h"
#include "ui_widget.h"

using namespace std;

Pictures::Pictures(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
    setFixedSize(1187,449);
    initModelView();
    initTable();
    setWindowTitle("Лабораторная работа №2");
}


void Pictures::getPictureInfo(const QModelIndex &index, const QImage& img, const QImageWriter& a) {
    ui->FileName->setText(model->fileName(index));
    ui->Size->setText(QString::number(img.size().width() )+ "x" + QString::number(img.size().height()));
    ui->Contraction->setText(QString::number(a.compression()));
    ui->Color_depth->setText(QString::number(img.bitPlaneCount()));
    ui->Resolution->setText(QString::number(img.physicalDpiX()));
}

void Pictures::dirUp(const QFileInfo& fileInfo, QListView* listView) {
    QDir dir = fileInfo.dir();
    dir.cdUp();
    model->index(dir.absolutePath());
    listView->setRootIndex(model->index(dir.absolutePath()));
}

bool Pictures::correctResolution(const QString& resolution) {
    QString r = resolution.toLower();
    return r == ".jpg" || r == ".gif" || r == ".tif" || r == ".bmp" || r == ".png" || r == ".pcx";
}

void Pictures::addItem(int i, const QString& res, const QList<QUrl>& list, const QFile& temp) {
    info->setItem(i, 2, new QTableWidgetItem(res));
    QString fileName = "";
    for(int i = temp.fileName().lastIndexOf('/') + 1; i < temp.fileName().lastIndexOf('.'); i++)
    {
        fileName.append(temp.fileName()[i]);
    }
    info->setItem(i,0,new QTableWidgetItem(fileName));
    QImage im(list[i].toLocalFile());
    QImageWriter a(list[i].toLocalFile());
    info->setItem(i, 1, new QTableWidgetItem(QString::number(im.size().width())+"x"+QString::number(im.size().height())));
    info->setItem(i, 3, new QTableWidgetItem(QString::number(im.bitPlaneCount())));
    info->setItem(i, 4, new QTableWidgetItem(QString::number(a.compression())));
}

Pictures::~Pictures()
{
    delete ui;
}
