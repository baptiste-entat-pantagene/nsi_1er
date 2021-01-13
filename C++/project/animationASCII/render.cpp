#include "Render.h"
using namespace std;

void Render::car(void)
{
	string car[4] = { "  ______", " /|_||_`.__", "(   _    _ _\\", "=`-(_)--(_)-'" };
	for (int i = 0; i < 4; i++)
	{
		cout << car[i] << endl;
	}

}


