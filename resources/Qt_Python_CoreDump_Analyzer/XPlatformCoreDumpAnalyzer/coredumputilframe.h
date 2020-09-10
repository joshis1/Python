#ifndef COREDUMPUTILFRAME_H
#define COREDUMPUTILFRAME_H

#include <QMainWindow>

namespace Ui {
class coreDumpUtilFrame;
}

class coreDumpUtilFrame : public QMainWindow
{
    Q_OBJECT

public:
    explicit coreDumpUtilFrame(QWidget *parent = 0);
    ~coreDumpUtilFrame();

private:
    Ui::coreDumpUtilFrame *ui;
};

#endif // COREDUMPUTILFRAME_H
