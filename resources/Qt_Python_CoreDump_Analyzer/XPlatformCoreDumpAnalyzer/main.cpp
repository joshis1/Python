#include "coredumputilframe.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    coreDumpUtilFrame w;
    w.show();

    return a.exec();
}
