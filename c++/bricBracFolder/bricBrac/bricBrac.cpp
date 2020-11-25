// bricBrac.cpp : définit le point d'entrée de l'application.
//

#include "bricBrac.h"

using namespace std;

int main()
{
    ofstream flux("text.txt");  // on ouvre le flux en lecture

    if (flux)  // si l'ouverture a réussi
    {
        flux << "salut";
        flux.close();  // on ferme le flux
    }
    else  // sinon
        cerr << "Impossible d'ouvrir le fichier !" << endl;


	return 0;
}
