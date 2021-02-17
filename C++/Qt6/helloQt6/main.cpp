#include "widget.h"

#include <QApplication>
#include <QtWidgets>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    Widget window;
    window.show();
    window.setWindowTitle(QString("App HelloQt6"));
    return app.exec();
}
