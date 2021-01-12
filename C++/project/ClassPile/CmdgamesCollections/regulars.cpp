#include "regulars.h"


int input(void)
{
	char buff[10];
	int buffInt = 0;
	while (true)
	{
		std::cin >> buff;
		try
		{
			buffInt = std::stoi(buff);
			break;
		}
		catch (const std::exception&)
		{
			continue;
		}
	}
	
	return buffInt;
}

void clear(void)
{
	system("cls");
}

/*
std::string input(void)
{

}
*/

int perso::ramdom(void)
{
	std::cout << "salut";
	return 0;
}
