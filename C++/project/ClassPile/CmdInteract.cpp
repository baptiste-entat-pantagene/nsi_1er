#include "CmdInteract.h"

CmdInteract::CmdInteract(void)
{
	lstChoixLv1[2] = { "1-> creer une pile", "2-> ajouter une valeur" };
}

void CmdInteract::choixLv1(std::string lstChoix[])
{
	for (int i = 0; i < 2; i++)
	{
		//std::count << lstChoix[i] << std::endl;
	}
	
}

void CmdInteract::createPile(void)
{

}