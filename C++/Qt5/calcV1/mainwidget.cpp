#include "mainwidget.h"
#include "./ui_mainwidget.h"
#include "button.h"

MainWidget::MainWidget(QWidget *parent)
    : QWidget(parent)
    , ui(new Ui::MainWidget)
{
    ui->setupUi(this);

}

MainWidget::~MainWidget()
{
    delete ui;
}
