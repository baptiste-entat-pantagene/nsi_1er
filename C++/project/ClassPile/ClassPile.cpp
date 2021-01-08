// ClassPile.cpp : définit le point d'entrée de l'application.
//

#include "ClassPile.h"

using namespace std;

int main()
{
	cout << "    --> start <--" << endl;

	Pile pile(10);
	pile.clear();

	cout << "taille max de bloc dans la pile-> " << pile.get_taille() << endl;
	cout << "blocs utilise->" << pile.get_actualBlocs() << endl;

	return 0;
}
