// GestionMémoireInsuffisante.cpp : définit le point d'entrée de l'application.
//

#include "GestionMémoireInsuffisante.h"

using namespace std;
constexpr auto BIG_NUMBER = 100000000;

int main()
{
    int* pI = new int[BIG_NUMBER];
    if (pI == 0x0) {
        cout << "Insufficient memory" << endl;
        return -1;
    }
    cout << "\nnice";
    
    delete[] pI;
    
}