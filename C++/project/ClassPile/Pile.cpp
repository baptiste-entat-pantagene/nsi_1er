/* Inclut la déclaration de la classe : */
#include <iostream>
#include "Pile.h"

/* Définit les méthodes de la classe : */

Pile::Pile(void)
{
    m_taille = 0;
    m_pile[2] = 0;
    std::cout << "error" << std::endl;
}

Pile::Pile(int taille)
{
    m_taille = taille;
    m_pile[taille +1] = 0;
    clear();
    
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

int Pile::get_last(void)
{
    return m_pile[m_pile[0]];
}

int Pile::get_lastAndPop(void)
{
    int buff;
    buff = get_last();
    pop();
    return buff;
}

void Pile::resize(int newSize)
{
    m_taille = newSize + 1;
    
}

void Pile::push(int value)
{
    if (m_pile[0] == m_taille)
    {
        std::cout << "  !-> debordement de pile positif <!" << std::endl;
    }
    else
    {
        m_pile[m_pile[0] + 1] = value;
        m_pile[0] += 1;
    }
}

void Pile::pop(void)
{
    m_pile[0] -= 1;
}

void Pile::info(void)
{
    std::cout << "blocs utilise-> " << get_actualBlocs() << ", sur -> " << get_taille() << std::endl;
}
