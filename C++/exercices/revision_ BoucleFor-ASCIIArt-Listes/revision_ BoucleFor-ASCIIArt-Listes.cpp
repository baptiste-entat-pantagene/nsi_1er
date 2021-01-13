// revision_ BoucleFor-ASCIIArt-Listes.cpp : définit le point d'entrée de l'application.
//

#include "revision_ BoucleFor-ASCIIArt-Listes.h"
using namespace std;


int inputInt(void);


int main()
{

	//fonction pour répéter les lettres de mots non implémenter dans le sélecteur de dessin,
	//mis sous commentaire mais bien fonctionnelle...
	/*
	cout << repeter_lettres_n_fois("salut", 2);
	int tab[] = { 1, 1, 8, 4, 2 };
	cout << repeter_lettres_liste("salut", tab);
	*/

	string lstFx[6] = { "carre" ,"triangle", "triangleReverse", "triangleMiroire", "diagonale", "diagonalReverse" };
	
	int dessinX = 0, tailleDessinX = 0;
	while (true)
	{
		cout << "select mode :\n";
		for (int i = 1; i <= 6; i++) //lstFx -> liste des modes de dessins...
		{
			cout << i << " -> " << lstFx[i - 1] << endl;
		}
		dessinX = inputInt();
		if (dessinX < 1 || dessinX > 6)
		{
			system("cls");
			cout << "veilliez recommencer\n";
			continue;
		}
		system("cls");
		cout << "select mode :\n";
		cout << "taille du dessin ?\n";
		tailleDessinX = inputInt();
		break;
	}

	system("cls");

	
	switch (dessinX)
	{
	case 1:
		cout << carre(tailleDessinX);
		break;
	case 2:
		cout << triangle(tailleDessinX);
		break;
	case 3:
		cout << triangleReverse(tailleDessinX);
		break;
	case 4:
		cout << triangleMiroire(tailleDessinX);
		break;
	case 5:
		cout << diagonal(tailleDessinX);
		break;
	case 6:
		cout << diagonalReverse(tailleDessinX);
		break;
	default:
		cout << "fuck !";
		break;
	}

	return 0;
}

int inputInt(void)
{
	char buff[10];
	int secured = 0;
	while (true)
	{
		cin >> buff;
		try
		{
			secured = stoi(buff);
			break;
		}
		catch (const std::exception&)
		{
			cout << "!-> please retry\n";
			continue;
		}
	}
	return secured;
}