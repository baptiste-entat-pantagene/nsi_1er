// animationASCII.cpp : définit le point d'entrée de l'application.
//

#include "animationASCII.h"
using namespace std;



int main()
{
	string render[10][10];
	string car[4][3] = { {"  ______"}, {" /|_||_`.__"}, {"   _    _ _\\"}, {"=`-(_)--(_)-'"} };
	string tree[4][3] = { {"***"}, {"*|*"}, {" | "}, {" |" } };

	
	string buff;
	int IndexTree = 0;
	while (true)
	{
		clearRender(render);

		addToRender(render, tree, 0, IndexTree);
		addToRender(render, tree, 0, IndexTree + 5);
		addToRender(render, tree, 5, IndexTree);
		addToRender(render, car, 5, 5);

		extractRender(buff, render);
		std::cout << buff;
		cout.flush();
		
		if (IndexTree <= 0)
		{
			IndexTree = 10;
		}
		else
		{
			IndexTree -= 1;
		}
		std::this_thread::sleep_for(std::chrono::milliseconds(200));
		std::system("cls");
	}
	return 0;
}

void clearRender(std::string  render[10][10])
{
	for (int i = 0; i < 10; i++)
	{
		for (int ii = 0; ii < 10; ii++)
		{
			render[i][ii] = " ";
		}

	}
}

void addToRender(std::string  render[10][10], std::string  obj[4][3], int x, int y)
{
	for (int i = 0 ; i < 4; i++)
	{
		for (int ii = 0; ii < 3; ii++)
		{
			render[i+x][ii+y] = obj[i][ii];
		}

	}
}

void extractRender(std::string& buff, std::string  render[10][10])
{
	for (int i = 0; i < 10; i++)
	{
		for (int ii = 0; ii < 10; ii++)
		{
			buff += render[i][ii];
		}
		buff += "\n";
	}
}
