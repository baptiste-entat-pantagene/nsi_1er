#ifndef WINDOW_H
#define WINDOW_H

#include <QWidget>
#include <QGridLayout>
#include <QPushButton>

class Window : public QWidget
{
    Q_OBJECT

public:
    Window(QWidget *parent = nullptr);
    ~Window();

private slots:
  void handleButton();

private:
  QGridLayout *m_mainLayout;
  QPushButton *m_button;
  int geoButtonR;
  int geoButtonC;


};
#endif // WINDOW_H
