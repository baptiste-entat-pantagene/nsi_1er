// revision_ BoucleFor-ASCIIArt-Listes.cpp : définit le point d'entrée de l'application.
//

#include "revision_ BoucleFor-ASCIIArt-Listes.h"
using namespace std;

string repeter_lettres_n_fois(string text, int multi = 1);
string repeter_lettres_liste(string text, int tab[]);
string triangle(int taille);

int main()
{
	cout << "start" << endl;

	/*
	int tab[] = { 1, 1, 8, 4, 2 };
	cout << repeter_lettres_liste("salut", tab);
	*/

	cout << triangle(5);

	return 0;
}


string repeter_lettres_n_fois(string text, int multi)
{
	string buff;
	for (int i = 0; i < text.length(); i++)
	{
		for (int ii = 0; ii < multi; ii++)
		{
			buff += text[i];
		}
	}
	return buff;
}

string repeter_lettres_liste(string text, int tab[])
{
	string buff;
	for (int i = 0; i < text.length(); i++)
	{
		for (int ii = 0; ii < tab[i]; ii++)
		{
			buff += text[i];
		}
	}
	return buff;
}

string triangle(int taille)
{
	string buff;
	for (int i = 1; i < taille +1; i++)
	{
		for (int ii = 0; ii < i; ii++)
		{
			buff += "*";
		}
		buff += "\n";
	}

	return buff;
}