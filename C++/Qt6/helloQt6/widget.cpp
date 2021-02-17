#include "widget.h"
#include <QtWidgets>

Widget::Widget(QWidget *parent): QWidget(parent)
{
    QPushButton *button = new QPushButton("click me !", this);
    QLabel *label1 = new QLabel("bravo kids !", this);
    label1->move(50, 50);

    QFormLayout *layout = new QFormLayout(this);
    layout->addRow(button, label1);







}

Widget::~Widget()
{
}

void Widget::on_pushButton_clicked()
{

}
