#include <iostream>
#include <string>
struct CmdInteract
{
public:
	CmdInteract(void);

	void choixLv1(std::string lstChoix[]);
	void createPile(void);


private:
	int IntUserInput;
	std::string lstChoixLv1[10];
};