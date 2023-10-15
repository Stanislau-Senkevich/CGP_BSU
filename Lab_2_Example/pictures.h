#ifndef PICTURES_H
#define PICTURES_H

#include <QWidget>
#include <QDir>
#include <QFileSystemModel>
#include <QModelIndex>
#include <QGridLayout>
#include <QListView>
#include <QImageWriter>
#include <QTableWidget>
#include <QFileDialog>
#include <QHeaderView>

QT_BEGIN_NAMESPACE
namespace Ui { class Widget; }
QT_END_NAMESPACE

class Pictures : public QWidget
{
    Q_OBJECT

public:
    Pictures(QWidget *parent = nullptr);
    ~Pictures();

private slots:
    void on_listView_doubleClicked(const QModelIndex &index);
    void dialogClose();
    void on_multiChoice_clicked();

private:
    Ui::Widget *ui;
    QFileSystemModel *model;
    QGridLayout *backgr;
    QListView *listView;
    QTableWidget *info=nullptr;
    QDialog *table;

    void initModelView();
    void initTable();
    void getPictureInfo(const QModelIndex &index, const QImage& img, const QImageWriter& a);
    void dirUp(const QFileInfo& fileInfo, QListView* listView);
    bool correctResolution(const QString& resolution);
    void addItem(int i, const QString& res, const QList<QUrl>& list, const QFile& temp);

};
#endif // PICTURES_H
