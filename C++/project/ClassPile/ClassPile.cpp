// ClassPile.cpp : définit le point d'entrée de l'application.
//

#include "ClassPile.h"

using namespace std;

int main()
{
	cout << "    --> start <--" << endl;

	Pile pile;
	pile.clear();
	pile.push(5);
	pile.push(6);

	
	cout << "blocs utilise->" << pile.get_actualBlocs() << ", sur ->" << pile.get_taille() << endl;

	return 0;
}
