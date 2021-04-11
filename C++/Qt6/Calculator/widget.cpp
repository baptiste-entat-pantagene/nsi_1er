#include "widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    m_layout = new QGridLayout(this);


    QPushButton *m_newButton1 = new QPushButton("1");
    connect(m_newButton1, &QPushButton::pressed, this, &Widget::num1Presed);
    m_layout->addWidget(m_newButton1, 2, 0);

    QPushButton *m_newButton2 = new QPushButton("2");
    connect(m_newButton2, &QPushButton::pressed, this, &Widget::num2Presed);
    m_layout->addWidget(m_newButton2, 2, 1);

    QPushButton *m_newButton3 = new QPushButton("3");
    connect(m_newButton3, &QPushButton::pressed, this, &Widget::num3Presed);
    m_layout->addWidget(m_newButton3, 2, 2);

    QPushButton *m_newButton4 = new QPushButton("4");
    connect(m_newButton4, &QPushButton::pressed, this, &Widget::num4Presed);
    m_layout->addWidget(m_newButton4, 1, 0);

    QPushButton *m_newButton5 = new QPushButton("5");
    connect(m_newButton5, &QPushButton::pressed, this, &Widget::num5Presed);
    m_layout->addWidget(m_newButton5, 1, 1);

    QPushButton *m_newButton6 = new QPushButton("6");
    connect(m_newButton6, &QPushButton::pressed, this, &Widget::num6Presed);
    m_layout->addWidget(m_newButton6, 1, 2);

    QPushButton *m_newButton7 = new QPushButton("7");
    connect(m_newButton7, &QPushButton::pressed, this, &Widget::num7Presed);
    m_layout->addWidget(m_newButton7, 2, 0);

    QPushButton *m_newButton8 = new QPushButton("8");
    connect(m_newButton8, &QPushButton::pressed, this, &Widget::num8Presed);
    m_layout->addWidget(m_newButton8, 2, 1);

    QPushButton *m_newButton9 = new QPushButton("9");
    connect(m_newButton9, &QPushButton::pressed, this, &Widget::num9Presed);
    m_layout->addWidget(m_newButton9, 2, 2);

    QPushButton *m_newButton0 = new QPushButton("0");
    connect(m_newButton0, &QPushButton::pressed, this, &Widget::num1Presed);
    m_layout->addWidget(m_newButton0, 3, 0, 1, 3);

    QLabel *saisieUtilisateur = new QLabel("void");
    m_layout->addWidget(saisieUtilisateur, 0, 4);

}

Widget::~Widget()
{
}

void Widget::num0Presed()
{

}
void Widget::num1Presed()
{
    qDebug("void Widget::num1Presed() is here !");
    QLabel *m_pressed = new QLabel("bravo kids");
    m_layout->addWidget(m_pressed, 5, 5);
}
void Widget::num2Presed()
{

}

void Widget::num3Presed()
{

}
void Widget::num4Presed()
{

}
void Widget::num5Presed()
{

}
void Widget::num6Presed()
{

}
void Widget::num7Presed()
{

}
void Widget::num8Presed()
{

}
void Widget::num9Presed()
{

}

