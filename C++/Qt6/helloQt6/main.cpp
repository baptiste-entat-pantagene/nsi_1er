#include "window.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    Window mainWindow;

    mainWindow.setWindowTitle(QString("helloQt6"));
    mainWindow.showMaximized();

    return app.exec();
}
