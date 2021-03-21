#include "widget.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    Widget window;

    window.setWindowTitle(QString("Hello Qt !"));
    window.resize(500, 500);

    window.show();
    return app.exec();
}
