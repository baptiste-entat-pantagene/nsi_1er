#include "widget.h"
#include "button.h"
#include <QPushButton>
#include <QLabel>
#include <QtWidgets>

Widget::Widget(QWidget *parent): QWidget(parent)
{
    QPushButton *button = new QPushButton("click me !", this);
    //QLabel *label1 = new QLabel("bravo kids !", this);
    //label1->hide();







}

Widget::~Widget()
{
}

void Widget::on_pushButton_clicked()
{
    QLabel *label1 = new QLabel("bravo kids !", this);
}
