#include "fonction.h"


string repeter_lettres_n_fois(string text, int multi)
{
	string buff;
	for (int i = 0; i < text.length(); i++)
	{
		for (int ii = 0; ii < multi; ii++)
		{
			buff += text[i];
		}
	}
	return buff;
}

string repeter_lettres_liste(string text, int tab[])
{
	string buff;
	for (int i = 0; i < text.length(); i++)
	{
		for (int ii = 0; ii < tab[i]; ii++)
		{
			buff += text[i];
		}
	}
	return buff;
}

string triangle(int taille)
{
	string buff;
	for (int i = 1; i < taille + 1; i++)
	{
		for (int ii = 0; ii < i; ii++)
		{
			buff += "*";
		}
		buff += "\n";
	}

	return buff;
}

string triangleReverse(int taille)
{
	string buff;
	for (int i = taille; i >= 0; i--)
	{
		for (int ii = 0; ii < i; ii++)
		{
			buff += "*";
		}
		buff += "\n";
	}

	return buff;
}

std::string triangleMiroire(int taille)
{
	string buff;
	for (int i = taille - 1; i >= 0; i--)
	{
		for (int ii = 0; ii < taille; ii++)
		{
			if (i <= ii)
			{
				buff += "*";
			}
			else {
				buff += " ";
			}

		}
		buff += "\n";
	}
	return buff;
}

string carre(int taille)
{
	string buff;
	for (int i = 0; i < taille; i++)
	{
		for (int ii = 0; ii < taille; ii++)
		{
			buff += "*";
		}
		buff += "\n";
	}
	return buff;
}

string diagonal(int taille)
{
	string buff;
	for (int i = taille - 1; i >= 0; i--)
	{
		for (int ii = 0; ii < taille; ii++)
		{
			if (i == ii)
			{
				buff += "/";
			}
			else {
				buff += " ";
			}

		}
		buff += "\n";
	}
	return buff;
}

string diagonalReverse(int taille)
{
	string buff;
	for (int i = 0; i < taille; i++)
	{
		for (int ii = 0; ii < taille; ii++)
		{
			if (i == ii)
			{
				buff += "\\";
			}
			else {
				buff += " ";
			}

		}
		buff += "\n";
	}
	return buff;
}
