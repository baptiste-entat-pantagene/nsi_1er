#ifndef BUTTON_H
#define BUTTON_H

#include <QPushButton>

class Button : public QPushButton
{
public:
    Button();

private:
    QPushButton *m_button;
};

#endif // BUTTON_H
