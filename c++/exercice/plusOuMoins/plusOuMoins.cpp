// plusOuMoins.cpp : Ce fichier contient la fonction 'main'. L'exécution du programme commence et se termine à cet endroit.
//
#include <iostream>
#include <random>
#include <ctime>
using namespace std;


int main()
{
    auto const seed = 5; // génération de la graine
    std::default_random_engine engin{ seed }; // générateur aléatoire
    std::normal_distribution<float> normal(0, 1); // générateur de distribution
    std::cout << normal(engin) << std::endl; // génération
}
