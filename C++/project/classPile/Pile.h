#pragma once

class Pile
{
public:
	Pile(int size);
	~Pile();

	int getSize();
	int getActualLevel();

	int getTop();
	void setTop(int data);

	void dellTop();
	int getTopDell();


private:
	int m_size;
	int* m_dataArray;
	int m_actualLevel;
};