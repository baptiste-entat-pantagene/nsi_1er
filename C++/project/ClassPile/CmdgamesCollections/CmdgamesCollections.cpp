// CmdgamesCollections.cpp : définit le point d'entrée de l'application.
//

#include "CmdgamesCollections.h"

using namespace std;

int main()
{

	cout << "1 --> plus ou moins" << endl;
	int buff = 0;

	buff = input();
	switch (buff)
	{
	case 1:
		mainPlusMoins();
		break;
	default:
		break;
	}
	
	
	return 0;
}
