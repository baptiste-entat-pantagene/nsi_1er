// main.cpp : définit le point d'entrée de l'application.
//

#include "main.h"

void getInput(int& inputVar);
void cmdInteract_choixLv1();

using namespace std;

int main()
{
	cout << "    --> start <--" << endl;
	int UserInput = 0;
	CmdInteract cmd;
	
	
	while (true)
	{
		cmdInteract_choixLv1();
	}

	cout << std::strlen("salut");

	


	/*
	pile.info();
	cout << "input test\n";
	int test = 0;
	getInput(test);
	cout << test << endl;
	*/
	return 0;
}


void getInput(int& inputVar)
{

	cin >> inputVar;

	while (!cin)
	{
		cin.clear();           // Restore input stream to working state
		cin.ignore(100, '\n'); // Get rid of any garbage that user might have entered
		cout << "Invalid selection! Try again: " << endl;
		cin >> inputVar; // After cin is restored and any garbage in the stream has been cleared, store user input in number again
	}
}

void cmdInteract_choixLv1()
{
	string lstLv1[2] = { "aaa", "bbb" };
	for (int i = 0; i < 2; i++)
	{
		//lstLv1[0]
		string buff = "ooo";
		std::count << buff << std::endl;
	}

}