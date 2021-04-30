#pragma once
#include <string>

#include <QLabel>
#include <QObject>
#include <QWidget>
#include <QGridLayout>

using namespace std;

class AbstractVehicule
{
public:
	AbstractVehicule(string model = "", int prix = 0, int vitesse = 0);
	virtual ~AbstractVehicule();


	//set section
	void set_name(string model);
	void set_prix(int prix);
	void set_vitesse(int vitesse);


	//get section
	string get_name();
	int get_prix();
	int get_vitesse();
	int get_nbRoues();


protected:
	string m_model;
	int m_prix;
	int m_vitesse;
	int m_nbRoues;
};

class Voiture : public AbstractVehicule
{
public:
	Voiture(string model = "", int prix = 0, int vitesse = 0, int nbPortes = 5);
	~Voiture();


	int get_nbPortes();

protected:
	int m_nbPortes;


};

class Moto : public AbstractVehicule
{
public:
	Moto(string model = "", int prix = 0, int vitesse = 0);
	~Moto();



};


class VehiculeWidget : public QWidget
{
    Q_OBJECT
public:
    VehiculeWidget();
    virtual ~VehiculeWidget();

private:
    QGridLayout* layout_main;
};
