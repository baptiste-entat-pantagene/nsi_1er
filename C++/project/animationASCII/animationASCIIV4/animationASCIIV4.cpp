// animationASCIIV4.cpp : définit le point d'entrée de l'application.
//

#include "animationASCIIV4.h"

using namespace std;
void frameToScene(string frame[50][10], string scene[], int sceneNB);
void addObjToFrame(string frame[50][10], string obj[2][5]);


int main()
{

	string scene[1];
	string frame[50][10];

	string objRoad[2][5] = { {"_", " ", "-", " ", "_"},{"_", " ", " ", " ", "_"} };

	addObjToFrame(frame, objRoad);
	frameToScene(frame, scene, 0);

	
	cout << scene[0];

	do
	{

	} while (true);

	return 0;
}

void frameToScene(string frame[50][10], string scene[], int sceneNB)
{
	string buff;
	for (int col = 0; col < 50; col++)
	{
		for (int lign = 0; lign < 10; lign++)
		{
			buff += frame[lign][col];
		}
		buff += "\n";
	}
	scene[sceneNB] = buff;
}

void addObjToFrame(string frame[50][10], string obj[2][5])
{
	for (int col = 0; col < 2; col++)
	{
		for (int lign = 0; lign < 5; lign++)
		{
			frame[lign][col] = obj[lign][col];
		}
	}
}
