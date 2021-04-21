// classPile.cpp : définit le point d'entrée de l'application.
//

#include "main.h"
#include "Pile.h"

using namespace std;

int main()
{
	cout << "version simple" << endl;
	Pile pile(5);

	cout << "max size -> " << pile.getSize() << endl;
	
	pile.setTop(1);
	pile.setTop(2);
	pile.setTop(3);

	cout << "getActualLevel -> " << pile.getActualLevel() << endl;

	int buff = pile.getActualLevel();
	for (size_t i = 0; i < buff; i++)
	{
		cout << "top -> " << pile.getTopDell() << endl;
	}
	
	//---> vs pointeur <---
	cout << endl << "version pointeur" << endl;
	Pile* pileP = new Pile(5);

	cout << "max size -> " << pileP->getSize() << endl;

	pileP->setTop(1);
	pileP->setTop(2);
	pileP->setTop(3);

	cout << "getActualLevel -> " << pileP->getActualLevel() << endl;

	int buff2 = pileP->getActualLevel();
	for (size_t i = 0; i < buff2; i++)
	{
		cout << "top -> " << pileP->getTopDell() << endl;
	}
	delete pileP;

	system("PAUSE");
	return 0;
}
