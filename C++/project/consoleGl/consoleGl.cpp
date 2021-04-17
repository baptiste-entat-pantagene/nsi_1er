// consoleGl.cpp : définit le point d'entrée de l'application.
//

#include "consoleGl.h"

using namespace std;

int main()
{

	int* screen[][3] = { {0}, {0}, {0} };

	for (int i = 0; i <= 2; i++)
	{
		for (int y = 0; y < 2; y++)
		{
			cout << screen[i][y];
		}
		cout << "\n";
	}


	return 0;
}
