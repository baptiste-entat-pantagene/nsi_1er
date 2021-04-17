#ifndef BUTTON_H
#define BUTTON_H

#include <QPushButton>

class Button : public QPushButton
{
    Q_OBJECT

public:
    Button(qint8 keyId, QPushButton *parent = nullptr);
    ~Button();


    qint8 getKeyId() const;

public slots:
    void slotEventPressed();

signals:
    void signalEventPressed();


private:
    qint8 m_keyId;
};

#endif // BUTTON_H
