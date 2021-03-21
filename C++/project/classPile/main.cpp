// classPile.cpp : définit le point d'entrée de l'application.
//

#include "main.h"
#include "Pile.h"

using namespace std;

int main()
{
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
	
	system("PAUSE");
	return 0;
}
