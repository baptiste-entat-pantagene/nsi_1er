// test.cpp : Ce fichier contient la fonction 'main'. L'exécution du programme commence et se termine à cet endroit.
//

#include <iostream>
#include <string>
using namespace std;

int input(string msg = "");

int main()
{
    int buff = 0;

    string msg[] = { "tu as moins de 18 ans", "tu as juste 18 ans", "tu as plus de 18 ans" };
    string* ptn = NULL;

    
    buff = input("tape ton age\n");
    if (buff < 18) {
        ptn = &msg[0];
    }
    else if (buff == 18)
    {
        ptn = &msg[1];
    }
    else
    {
        ptn = &msg[2];
    }

    cout << *ptn << endl;
}

int input(string msg) {
    string buffStr = "";
    int buffInt = 0;

    while (true)
    {
        cout << msg;
        cin >> buffStr;
        try
        {
            buffInt = std::stoi(buffStr);
            break;
        }
        catch (const std::exception&)
        {
            cout << "use only int type\n";
        }
    }
    return buffInt;
}
