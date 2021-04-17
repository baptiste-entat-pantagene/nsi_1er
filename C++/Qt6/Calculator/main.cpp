#include "widget.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);
    app.setStyleSheet(" QPushButton { background-color: red; border: 5px solid green; border-radius: 6px; }"
                        "QLabel { background-color: green; border:5px solid red; border-radius: 7px; }");
    Widget window;
    window.setWindowTitle(QString("Calculator"));
    window.show();
    return app.exec();
}
