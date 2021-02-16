#include "mainwidget.h"

#include <QApplication>
#include <QCommandLineParser>
#include <QCommandLineOption>
#include <QCursor>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    QCoreApplication::setApplicationName("Hello Qt6");

    MainWidget mainWin;
    mainWin.show();

    return app.exec();
}
