#include "pictures.h"
#include "ui_widget.h"

void Pictures::initModelView() {
    model = new QFileSystemModel(this);
    model->setFilter(QDir::QDir::AllEntries);
    model->setRootPath("");
    ui->listView->setModel(model);
}

void Pictures::initTable() {
    table = new QDialog();
    table->setWindowTitle("Информация о файлах");
    table->setWindowIcon(QPixmap(":/img/folder.png"));
    QGridLayout *tableLayout = new QGridLayout(table);
    table->setMinimumSize(700,700);
    info = new QTableWidget(table);
    tableLayout->addWidget(info);
    info->setColumnCount(5);
    info->setEditTriggers(QAbstractItemView::NoEditTriggers);
    info->setHorizontalHeaderItem(0, new QTableWidgetItem("Имя файла"));
    info->setHorizontalHeaderItem(1, new QTableWidgetItem("Размер"));
    info->setHorizontalHeaderItem(2, new QTableWidgetItem("Расширение"));
    info->setHorizontalHeaderItem(3, new QTableWidgetItem("Глубина цвета"));
    info->setHorizontalHeaderItem(4, new QTableWidgetItem("Сжатие"));
    info->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
}
