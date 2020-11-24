// fonction1.cpp : définit le point d'entrée de l'application.
//

#include "fonction1.h"

using namespace std;

int add(int a, int b) {
	return a + b;
}

int main()
{
	int a, b, c;
	a = 5;
	b = 8;
	c = add(a, b);
	cout << "a + b = " << c << endl;
	return 0;
}