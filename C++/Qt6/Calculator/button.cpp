#include "button.h"

Button::Button(qint8 keyId, QPushButton *parent) : QPushButton(parent), m_keyId(keyId)
{

    connect(this, &QPushButton::pressed, this, &Button::slotEventPressed);

}

Button::~Button()
{

}

void Button::slotEventPressed()
{
    emit signalEventPressed();
}

qint8 Button::getKeyId() const
{
    return m_keyId;
}

void signalEventPressed()
{
    qDebug("signal retransmite (in Button)");
}
