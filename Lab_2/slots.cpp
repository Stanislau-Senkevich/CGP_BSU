#include "pictures.h"

void Pictures::on_listView_doubleClicked(const QModelIndex &index)
{
    QListView* listView = (QListView*)sender();
    QFileInfo fileInfo = model->fileInfo(index);

    if(fileInfo.fileName() == "..")
    {
        dirUp(fileInfo, listView);
    }
    else if (fileInfo.fileName() == ".")
    {
        listView->setRootIndex(model->index(""));
    }
    else if(fileInfo.isDir())
    {
        listView->setRootIndex(index);
    }
    else
    {
        QString fileExt = model->fileName(index);
        QImageWriter imgWriter(model->filePath(index));
        QString res = "";
        QImage img (model->filePath(index));
        for(int i = fileExt.lastIndexOf('.'); i < fileExt.size(); i++)
        {
            res.append(fileExt[i]);
        }
        if (correctResolution(res))
        {
            getPictureInfo(index, img, imgWriter);
        }
    }
}

void Pictures::dialogClose()
{
    this->show();
}

void Pictures::on_multiChoice_clicked()
{
    QFileDialog *files = new QFileDialog;
    files->setWindowTitle("Open files");
    QList<QUrl> list = files->getOpenFileUrls();
    info->setRowCount(0);
    info->setRowCount(list.size());
    for (int i = 0; i < list.size(); i++)
    {
        QFile temp(list[i].toLocalFile());
        QString res;
        if (temp.fileName().lastIndexOf('.') == -1)
        {
            info->setRowCount(info->rowCount()-1);
            continue;
        }
        for (int i = temp.fileName().lastIndexOf('.'); i < temp.fileName().size(); i++)
        {
            res.append(temp.fileName()[i]);
        }
        if (!correctResolution(res))
        {
            info->setRowCount(info->rowCount()-1);
            continue;
        }
        addItem(i, res, list, temp);
    }
    if (info->rowCount() == 0)
    {
        return;
    }
    table->show();
    connect(table, SIGNAL(rejected()), this, SLOT(dialogClose()));
    this->hide();
}
