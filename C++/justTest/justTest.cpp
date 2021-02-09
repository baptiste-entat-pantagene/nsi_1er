// justTest.cpp : définit le point d'entrée de l'application.
//

#include "justTest.h"

using namespace std;

int main()
{
	int myVar = 5;
	int* pointeToIntVar = &myVar;
	
	cout << &myVar << endl;
	cout << pointeToIntVar << endl;
	cout << *pointeToIntVar << endl;
	return 0;
}
