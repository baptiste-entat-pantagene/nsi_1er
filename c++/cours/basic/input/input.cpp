// input.cpp : définit le point d'entrée de l'application.
//

#include "input.h"

using namespace std;

int main()
{
	string buffer;
	int age;

	cout << "tape ton age\n";

	cin >> buffer;
	try
	{
		age = stoi(buffer);
	}
	catch (const std::exception&)
	{
		cout << "erreur : 55";
		return -1;
	}
	cout << "vous avez taper : " << age << "ans\n";
	return 0;
}