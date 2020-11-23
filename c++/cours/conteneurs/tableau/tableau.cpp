// tableau.cpp : définit le point d'entrée de l'application.
//

#include "tableau.h"

using namespace std;

int main()
{
    vector<int> const tableau_entiers{ 1, 2, 3 };

    cout << "Je vais afficher mon tableau en entier.\n";
    for (auto const element : tableau_entiers)
    {
        cout << element << endl;
    }
}
