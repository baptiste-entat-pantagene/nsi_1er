#include "widget.h"
#include "QLabel"
#include "QPushButton"


Widget::Widget(QWidget *parent)
    : QWidget(parent)
{


   QPushButton *restart = new QPushButton(this);
   restart->setText(QString("restart"));


}

Widget::~Widget()
{
}
