// animationASCIIV2.cpp : définit le point d'entrée de l'application.
//

#include "animationASCIIV2.h"

using namespace std;

int main()
{
	string frame[10];
	//frame[] = "";

	for (int indexFrame = 0; indexFrame < 10; indexFrame++)
	{
		int poscar = 0;
		int ligneRoute = 0;
		for (int ling = 0; ling < 5; ling++) //col of the road
		{

			for (int col = 0; col < 100; col++) //len of the road
			{
				
				//make the road
				switch (ling)
				{
				case 0:
					frame[indexFrame] += "_";
					break;
				case 1:
					frame[indexFrame] += "";
					break;
				case 2:
					if (ligneRoute == 1)
					{
						frame[indexFrame] += "-";
						ligneRoute = 0;
					}
					else
					{
						frame[indexFrame] += " ";
						ligneRoute = 1;
					}
					break;
				case 3:
					frame[indexFrame] += "";
					break;
				case 4:
					frame[indexFrame] += "_";
					break;
				default:
					break;
				}
				

			}
			frame[indexFrame] += "\n";
		}
	}

	//std::cout << frame[0];
	do
	{
		for (int i = 0; i < 10; i++)
		{
			std::cout << frame[i];
		}
		
	} while (false);


	return 0;
}

//frame[indexFrame] = "________________________________________________\n\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n\n________________________________________________";