#ifndef WIDGET_H
#define WIDGET_H

#include <QDebug> //debug
#include <QWidget>
#include <QGridLayout>
#include <QPushButton>
#include <QLabel>
#include <QString>
#include <qfloat16>
#include <QQueue>
#include "button.h"

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();

    void calcResult();

public slots:
    void numNPresed();

signals:


private:
    QGridLayout *m_layout;
    QGridLayout *m_layoutButton;
    QGridLayout *m_layoutView;

    QLabel *viewer;
    QString *viewerString;
};
#endif // WIDGET_H
