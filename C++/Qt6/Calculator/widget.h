#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <QGridLayout>
#include <QPushButton>
#include <QLabel>

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();
public slots:
    void num0Presed();
    void num1Presed();
    void num2Presed();
    void num3Presed();
    void num4Presed();
    void num5Presed();
    void num6Presed();
    void num7Presed();
    void num8Presed();
    void num9Presed();

signals:


private:
    QGridLayout *m_layout;
    //QGridLayout *m_layoutButton;
};
#endif // WIDGET_H
