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
		cout << "error de toi/n/n";
		return -1;
	}
	cout << "vous avez taper : " << age << "ans\nworkNice\n";
	return 0;
}
