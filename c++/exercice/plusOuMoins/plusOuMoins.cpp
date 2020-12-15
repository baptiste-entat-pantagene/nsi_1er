// plusOuMoins.cpp : Ce fichier contient la fonction 'main'. L'exécution du programme commence et se termine à cet endroit.
//
#include <iostream>
/* rand example: guess the number */
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */

using namespace std;


int main()
{
    int randNum, iGuess;

    /* initialize random seed: */
    srand(time(NULL));
    /* generate secret number between 1 and 10: */
    randNum = rand() % 100 + 1;

    do {
        cout << "Guess the number (1 to 100): \n";
        cin >> iGuess;
        if (randNum < iGuess) cout << "The secret number is lower\n";
        else if (randNum > iGuess) cout << "The secret number is higher\n";
    } while (randNum != iGuess);

    cout << "Congratulations!";
    return 0;
}