// Morpion.cpp : définit le point d'entrée de l'application.
//

#include "Morpion.h"

using namespace std;

void afficher(string tableau[3][3]);

void NewAction(std::string  caseTab[3][3], string charact);

string etatGame(std::string  caseTab[3][3]);

int main()
{
	cout << "Morpion game\n" << endl;
	string caseTab[3][3]{ 
		{"*", "*", "*"},
		{"*", "*", "*"},
		{"*", "*", "*"}
	};
	

	string joueur[2] = { "Bap", "J2" };
	string prochainJoueur = joueur[0];
	string charact = "X";
	string msg = "";
	
	while (true)
	{
		afficher(caseTab);
		cout << "au tour de -> " << prochainJoueur << endl;
		
		
		NewAction(caseTab, charact);

		msg = etatGame(caseTab);
		if (msg != "")
		{
			cout << msg << endl;
			break;
		}



		if (prochainJoueur == joueur[0])
		{
			prochainJoueur = joueur[1];
			charact = "O";
		}
		else
		{
			prochainJoueur = joueur[0];
			charact = "X";
		}

		system("cls");
	}
	

	return 0;
}

string etatGame(std::string  caseTab[3][3])
{

	//test gagnat
	for (int lign = 0; lign < 3; lign++)
	{
		if (caseTab[lign][0] == caseTab[lign][1] && caseTab[lign][1] == caseTab[lign][2] && caseTab[lign][0] != "*")
		{
			return "une ligne gagnante";
		}
	}
	for (int col = 0; col < 3; col++)
	{
		if (caseTab[0][col] == caseTab[1][col] && caseTab[1][col] == caseTab[2][col] && caseTab[0][col] != "*")
		{
			return "une collone gagnante";
		}
	}
	if (caseTab[0][0] == caseTab[1][1] && caseTab[1][1] == caseTab[2][2] && caseTab[0][0] != "*")
	{
		return "une diagonal gagnante";
	}
	if (caseTab[0][2] == caseTab[1][1] && caseTab[1][1] == caseTab[2][0] && caseTab[0][2] != "*")
	{
		return "une diagonal gagnante";
	}

	//plateau plein
	int full = 0;
	for (int lign = 0; lign < 3; lign++)
	{
		for (int col = 0; col < 3; col++)
		{
			if (caseTab[lign][col] == "*")
			{
				full += 1;
			}
		}
	}
	if (full == 0)
	{
		return "fin de partie mais pas de gagnant";
	}
	return "";

}

void NewAction(std::string  caseTab[3][3], string charact)
{
	string tabLettre[3] = {"A", "B", "C"};
	string tabNum[3] = { "0", "1", "2" };
	string buffCin = "";
	int error = -1;

	while (true)
	{
		cin >> buffCin;
		for (int lettre = 0; lettre < 3; lettre++)
		{
			for (int num = 0; num < 3; num++)
			{
				if (buffCin == tabLettre[lettre] + tabNum[num])
				{
					if (caseTab[lettre][num] != "*")
					{
						cout << "non non non";
						error = 1;
						break;
					}
					caseTab[lettre][num] = charact;
					error = 0;
				}
			}
		}

		if (error == 0)
		{
			break;
		}
		else if (error == 1)
		{
			cout << "emplacement deja pris, recomencer\n";
		}
		else
		{
			cout << "emplacement inconnu tape par exemple: 'A0'\n";
		}
	}
}

void afficher(string tableau[3][3])
{

	cout << "    -------\n";
	for (int lign = 0; lign < 3; lign++)
	{
		switch (lign)
		{
		case 0:
			cout << "A-> ";
			break;
		case 1:
			cout << "B-> ";
			break;
		case 2:
			cout << "C-> ";
			break;
		default:
			break;
		}
		
		for (int col = 0; col < 3; col++)
		{
			cout << "|" << tableau[lign][col];
		}
		cout << "|\n    -------\n";
		
		
	}
	cout << "    ^  ^  ^" << endl;
	cout << "    |  |  |" << endl;
	cout << "    0  1  2" << endl;
}