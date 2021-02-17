#include "button.h"

Button::Button()
{
    QPushButton *m_button = new QPushButton("click me !", this);
    m_button->show();
}
