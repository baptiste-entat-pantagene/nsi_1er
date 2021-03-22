#include "window.h"
#include <QPushButton>
#include <QLabel>

Window::Window(QWidget *parent)
    : QWidget(parent)
{
    m_button = new QPushButton("click ME", this);
    connect(m_button, &QPushButton::clicked, this, &Window::handleButton);
}

Window::~Window()
{
}

void Window::handleButton()
{
  m_button->setText("nice");
  m_button->resize(100,100);

  QLabel *displayHello = new QLabel("salut bb", this);
  displayHello->setGeometry(100, 100, 100, 100);
  displayHello->show();

}
