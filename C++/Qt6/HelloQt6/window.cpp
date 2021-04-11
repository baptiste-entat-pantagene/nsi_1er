#include "window.h"

#include <QPushButton>
#include <QLabel>

Window::Window(QWidget *parent)
    : QWidget(parent)
{
    m_mainLayout = new QGridLayout(this);
    m_button = new QPushButton("click ME");
    m_mainLayout->addWidget(m_button, 0, 0);
    connect(m_button, &QPushButton::clicked, this, &Window::handleButton);
    geoButtonR = 1;
    geoButtonC = 1;

}

Window::~Window()
{
}

void Window::handleButton()
{
  m_button->setText("nice");

  QLabel *displayHello = new QLabel("salut bg");
  m_mainLayout ->addWidget(displayHello, geoButtonR, geoButtonC);
  if (geoButtonR >= 4)
  {
      geoButtonR = 1;
      geoButtonC += 1;
  }
  geoButtonR += 1;


}
