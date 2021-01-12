#include "plusMoins.h"
using namespace std;

void mainPlusMoins(void)
{
	clear();
	cout << "jeux de plus ou moins" << endl;
	int buff = 0, nbMystere = 12;

	cout << "tape un nombre entre 0 et 100" << endl;
	while (true)
	{
		buff = input();
		if (buff > nbMystere)
		{
			cout << "moins";
		}
		else if (buff < nbMystere)
		{
			cout << "plus";
		}
		else if (buff == nbMystere)
		{
			cout << "gagné !";
			break;
		}
		else
		{
			cout << "error";
		}
	}
}
