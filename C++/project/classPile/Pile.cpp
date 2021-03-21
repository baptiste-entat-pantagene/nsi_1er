#include "Pile.h"

Pile::Pile(int size)
{
	m_size = size;
	m_dataArray = new int[size];
	m_actualLevel = 0;
}

Pile::~Pile()
{
	delete m_dataArray;
}

int Pile::getSize()
{
	return m_size;
}

int Pile::getActualLevel()
{
	return m_actualLevel;
}

int Pile::getTop()
{
	return m_dataArray[m_actualLevel-1];
}

void Pile::setTop(int data)
{
	m_dataArray[m_actualLevel] = data;
	m_actualLevel += 1;
	
}

void Pile::dellTop()
{
	m_actualLevel -= 1;
}

int Pile::getTopDell()
{
	m_actualLevel -= 1;
	return m_dataArray[m_actualLevel]; //-1 =!

}
