// array.cpp : définit le point d'entrée de l'application.
//

#include "array.h"

using namespace std;

int main()
{
    array<int, 5> const tableau_entiers{ 1, 4, 2, 4, 7 };

    cout << "Je vais afficher mon tableau de " << tableau_entiers.size() << " entier.\n";
    for (auto const element : tableau_entiers)
    {
        cout << element << endl;
    }
}
