// gestionVehicules.cpp : définit le point d'entrée de l'application.
//

#include "gestionVehicules.h"

using namespace std;


void presentationVehicule(AbstractVehicule* v) //take ptr
{
	cout << "model: \"" << v->get_name() << "\" ,prix: " << v->get_prix() << "euro ,vitesse: " << v->get_vitesse() << "km/h ,nb roues: " << v->get_nbRoues();
	Voiture* castedVoiture = dynamic_cast<Voiture*>(v);
	if (castedVoiture != nullptr)
	{
		cout << " ,nb portes: " << castedVoiture->get_nbPortes();
		cout << "  --> c'est une voiture";
	}
	Moto* castedMoto = dynamic_cast<Moto*>(v);
	if (castedMoto != nullptr)
	{
		cout << "  --> c'est une moto";
	}
	cout << endl;
}

int main()
{
	//exemple 1
	Voiture voitureTest("Tesla Model S", 89990, 250);
	voitureTest.set_vitesse(322);
	presentationVehicule(&voitureTest); //passe par la &
	


	//exemple 2
	vector<AbstractVehicule*> listVehicules;
	listVehicules.push_back(new Voiture("Zoe", 20500, 250)); //add vehicule to vect
	listVehicules.push_back(new Moto("moto", 10200, 245));

	presentationVehicule(listVehicules[0]); //print info about
	presentationVehicule(listVehicules[1]);

	for (int i(0); i < listVehicules.size(); ++i) //clean
	{
		delete listVehicules[i];  //On libère la i-ème case mémoire allouée
		listVehicules[i] = nullptr;  //On met le pointeur à 0 pour éviter les soucis
		listVehicules.pop_back();
	}
	
	//exemple 3 (plan)
	/*
	vector<AbstractVehicule*> garageColection;
	string userInput("");
	cout << "1 -> voiture\n2 -> moto\n";
	cin >> userInput;
	if (userInput == "1")
	{
		cout << "model ?\n";
		string model("");
		cin >> model;
		garageColection.push_back(new Voiture(model));

	}
	else if (userInput == "2")
	{
		cout << "model ?\n";
		string model("");
		cin >> model;
		garageColection.push_back(new Moto(model));
	}
	else
	{
		cout << "bad input";
	}

	for (int i(0); i < garageColection.size(); ++i) //print info
	{
		presentationVehicule(garageColection[i]);
	}

	for (int i(0); i < garageColection.size(); ++i) //clean
	{
		delete garageColection[i];  //On libère la i-ème case mémoire allouée
		garageColection[i] = nullptr;  //On met le pointeur à 0 pour éviter les soucis
		garageColection.pop_back();
	}
	*/
	
	return 0;
}
