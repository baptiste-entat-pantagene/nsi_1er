/* Inclut la déclaration de la classe : */
#include <iostream>
#include "Pile.h"

/* Définit les méthodes de la classe : */

Pile::Pile(void)
{
    m_taille = 0;
    m_pile[1] = 0;
}

Pile::Pile(int taille)
{
    m_taille = taille + 1;
    m_pile[taille] = 0;
}

void Pile::clear(void)
{
    m_pile[0] = 0;

    /*
    for (int i = 0; i < 5; i++)
    {
        std::cout << "debug i->" << i << std::endl;
        m_pile[i] = 0;
    }
    */
}

int Pile::get_taille(void)
{
    return m_taille;
}

int Pile::get_actualBlocs(void)
{
    return m_pile[0];
}

int Pile::push(int value)
{
    m_pile[m_pile[0]] = value;
    return 0;
}
