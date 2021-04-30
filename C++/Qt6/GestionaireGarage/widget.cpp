#include "widget.h"

Widget::Widget(QWidget *parent) : QWidget(parent)
{
    layout_main = new QGridLayout(this);

    layout_vehicule = new QBoxLayout(QBoxLayout::TopToBottom);
    layout_main->addLayout(layout_vehicule, 0, 0);

    layout_aboutIt = new QBoxLayout(QBoxLayout::TopToBottom);
    layout_main->addLayout(layout_vehicule, 0, 1);


    vehicule_vector_info = new vector<VehiculeWidget*>;
    for (unsigned i=0;i<5 ;i++ ) {
        vehicule_vector_info->push_back(new VehiculeWidget);
        layout_vehicule->addWidget(vehicule_vector_info->at(i));
    }


    QLabel* test001 = new QLabel(QString("012154\n59741"));
    layout_aboutIt->addWidget(test001);


}

Widget::~Widget()
{
    //delete layout_main;

    //delete vehicule_vector_info[0];
    /*
    for (unsigned int i = 0; i < vehicule_vector_info.size(); i++) //clean
        {
            delete vehicule_vector_info[i];
            vehicule_vector_info[i] = nullptr;
            vehicule_vector_info.pop_back();
        }
        */
}


void Widget::update_layout_vehicule()
{
    //for (unsigned i=0, i < )
}

