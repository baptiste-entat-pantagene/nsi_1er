// animationASCIIV3.cpp : définit le point d'entrée de l'application.
//

#include "animationASCIIV3.h"

using namespace std;
void addRoad(string actualFrame[50][5]);
void addCar(string actualFrame[50][5]);
void frameToframeExpress(string actualFrame[50][5], string m_frameExpress[5]);

int main()
{
	string frame[50][5];
	string frameExpress[5];
	
	string multiFrameExpress[3];

	for (int i = 0; i < 3; i++)
	{
		addRoad(frame);
		addCar(frame);
		frameToframeExpress(frame, frameExpress);

		for (int ii = 0; ii < 5; ii++)
		{
			multiFrameExpress[i] += frameExpress[ii] + "\n";
			cout << multiFrameExpress[i] << endl;
		}

	}
	
	do
	{
		for (int i = 0; i < 3; i++)
		{
			cout << multiFrameExpress[i] << endl;
		}

	} while (false);
	

	return 0;
}

void addRoad(string actualFrame[50][5])
{
	string road[2][5] = { {"_", " ", "-", " ", "_"},{"_", " ", " ", " ", "_"} };
	int indexRoad = 0;

	for (int i = 0; i < 50; i++)
	{
		if (indexRoad == 0)
		{
				indexRoad = 1;
		}
		else
		{
				indexRoad = 0;
		}
		for (int ii = 0; ii < 5; ii++)
		{
			actualFrame[i][ii] = road[indexRoad][ii];
		}
		
	}
}

void addCar(string actualFrame[50][5])
{
	string car[2][8] = { {"~", "'", "O", "-", "-", "-", "O", "'"}, {"~", "~", ",", "-", "-", ".", " ", " "} };


	int indexCar = 0;

	for (int i = 0; i < 2; i++)
	{
		if (indexCar == 0)
		{
			indexCar = 1;
		}
		else
		{
			indexCar = 0;
		}
		for (int ii = 0; ii < 8; ii++)
		{
			actualFrame[ii][i+3] = car[indexCar][ii];
		}

	}
}

void frameToframeExpress(string actualFrame[50][5], string m_frameExpress[5])
{
	for (int i = 0; i < 5; i++)
	{
		for (int ii = 0; ii < 50; ii++)
		{
			m_frameExpress[i] += actualFrame[ii][i];
		}

	}
}