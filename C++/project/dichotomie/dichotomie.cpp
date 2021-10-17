// dichotomie.cpp : définit le point d'entrée de l'application.
//

#include "dichotomie.h"

using namespace std;

template <typename TType>
TType dichoto(vector<TType> tab, TType shearch);

int main()
{

    
    vector<int> tableau{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };





    for (auto& i : tableau)
    {
        cout << i << endl;
    }

    for (size_t i = 0; i < tableau.size(); i++)
    {
        cout << tableau.at(i);
    }

    cout << endl;
    cout << endl;
    cout << dichoto(tableau, 5);



	return 0;
}

template <typename TType>
TType dichoto(vector<TType> tab, TType shearch)
{

    size_t beging(0);
    size_t end = tab.size() - 1;
    size_t middle = (beging + end) / 2;

    while (beging <= end && tab.at(middle) == shearch)
    {
        
        if (tab.at(middle) > shearch)
        {
            end = middle--;
        }
        else
        {
            beging = middle++;
        }

        
        middle = (beging + end) / 2;
    }

    return middle;
}

