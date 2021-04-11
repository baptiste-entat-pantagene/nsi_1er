#include "widget.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    //app.setStyleSheet("* { color: red }");
    QString globalStyleSheet(" QPushButton { background-color: red; border: 5px solid green; }");
    app.setStyleSheet(globalStyleSheet);

    Widget window;
    window.setWindowTitle(QString("Calculator"));
    window.show();
    return app.exec();
}
