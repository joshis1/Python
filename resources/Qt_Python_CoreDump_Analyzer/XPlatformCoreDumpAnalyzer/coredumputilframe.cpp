#include "coredumputilframe.h"
#include "ui_coredumputilframe.h"

coreDumpUtilFrame::coreDumpUtilFrame(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::coreDumpUtilFrame)
{
    ui->setupUi(this);
}

coreDumpUtilFrame::~coreDumpUtilFrame()
{
    delete ui;
}
