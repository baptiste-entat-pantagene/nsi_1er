#include "Vehicule.h"

using namespace std;


AbstractVehicule::AbstractVehicule(string model, int prix, int vitesse) : m_model(model), m_prix(prix), m_vitesse(vitesse), m_nbRoues(0)
{
}

AbstractVehicule::~AbstractVehicule()
{
}

void AbstractVehicule::set_name(string model)
{
	m_model = model;
}

void AbstractVehicule::set_prix(int prix)
{
	m_prix = prix;
}

void AbstractVehicule::set_vitesse(int vitesse)
{
	m_vitesse = vitesse;
}

string AbstractVehicule::get_name()
{
	return m_model;
}

int AbstractVehicule::get_prix()
{
	return m_prix;
}

int AbstractVehicule::get_vitesse()
{
	return m_vitesse;
}

int AbstractVehicule::get_nbRoues()
{
	return m_nbRoues;
}



//Voiture
Voiture::Voiture(string model, int prix, int vitesse, int nbPortes) : AbstractVehicule(model, prix, vitesse), m_nbPortes(nbPortes)
{
	m_nbRoues = 4;
}

Voiture::~Voiture()
{
}

int Voiture::get_nbPortes()
{
	return m_nbPortes;
}



//Moto
Moto::Moto(string model, int prix, int vitesse) : AbstractVehicule(model, prix, vitesse)
{
	m_nbRoues = 2;
}

Moto::~Moto()
{
}



//widget_infoVVehicule
VehiculeWidget::VehiculeWidget()
{
    layout_main = new QGridLayout(this);
    QLabel* checkWork = new QLabel(QString("info 1\ninfo 2\n.."));
    layout_main->addWidget(checkWork, 0, 0);
}
VehiculeWidget::~VehiculeWidget()
{
}
