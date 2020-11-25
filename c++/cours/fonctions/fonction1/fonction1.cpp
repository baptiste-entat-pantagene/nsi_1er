// fonction1.cpp : définit le point d'entrée de l'application.
//

#include "fonction1.h"

using namespace std;



template<typename TypNam>
const TypNam& Add(const TypNam& A, const TypNam& B)
{
	return A + B;
}

int main()
{
	int a, b, c;
	a = 5;
	b = 8;
	c = Add(a, b);
	cout << "a + b = " << c << endl;
	return 0;
}