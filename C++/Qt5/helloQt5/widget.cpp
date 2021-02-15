#include "widget.h"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::Widget)
{
    ui->setupUi(this);
    ui->label->hide(); //cache le "salut"
}

Widget::~Widget()
{
    delete ui;
}


void Widget::on_pushButton_clicked()
{
    ui->pushButton->hide();
    ui->label->show();

}
