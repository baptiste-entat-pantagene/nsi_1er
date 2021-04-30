#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>

#include <QGridLayout>
#include <QBoxLayout>

#include <QLabel>

#include <QString>
#include <vector>
#include <QVector>

#include "Vehicule.h"

class Widget : public QWidget
{
    Q_OBJECT

public:
    Widget(QWidget *parent = nullptr);
    ~Widget();


public slots:
    void update_layout_vehicule();

private:
    QGridLayout* layout_main;

    QBoxLayout* layout_vehicule;
    vector<VehiculeWidget*>* vehicule_vector_info;

    QBoxLayout* layout_aboutIt;
};
#endif // WIDGET_H
