#include "widget.h"

Widget::Widget(QWidget *parent)
    : QWidget(parent)
{
    m_layout = new QGridLayout(this);
    m_layoutButton = new QGridLayout();
    m_layoutView = new QGridLayout();

    m_layout->addLayout(m_layoutView, 1, 1);
    m_layout->addLayout(m_layoutButton, 2, 1, 3, 1);



    //button setup
    for (qint8 i=0;i<=9 ;i++ ) {
        Button *newbutton = new Button(i);
        newbutton->setText(QString::number(i));
        connect(newbutton, &Button::signalEventPressed, this, &Widget::numNPresed);
        switch (i) {
        case 0: {
            m_layoutButton->addWidget(newbutton, 3, 0, 1, 3);
            break;
        }
        case 1: {
            m_layoutButton->addWidget(newbutton, 2, 0);
            break;
        }
        case 2: {
            m_layoutButton->addWidget(newbutton, 2, 1);
            break;
        }
        case 3: {
            m_layoutButton->addWidget(newbutton, 2, 2);
            break;
        }
        case 4: {
            m_layoutButton->addWidget(newbutton, 1, 0);
            break;
        }
        case 5: {
            m_layoutButton->addWidget(newbutton, 1, 1);
            break;
        }
        case 6: {
            m_layoutButton->addWidget(newbutton, 1, 2);
            break;
        }
        case 7: {
            m_layoutButton->addWidget(newbutton, 0, 0);
            break;
        }
        case 8: {
            m_layoutButton->addWidget(newbutton, 0, 1);
            break;
        }
        case 9: {
            m_layoutButton->addWidget(newbutton, 0, 2);
            break;
        }
        default: {
            break;
        }
        }

        for (qint8 i=10;i<=12 ;i++ ) {
            Button *newbutton = new Button(i);
            connect(newbutton, &Button::signalEventPressed, this, &Widget::numNPresed);
            switch (i) {
            case 10: {
                newbutton->setText(QString("-"));
                m_layoutButton->addWidget(newbutton, 0, 3);
                break;
            }
            case 11: {
                newbutton->setText(QString("+"));
                m_layoutButton->addWidget(newbutton, 1, 3);
                break;
            }
            case 12: {
                newbutton->setText(QString("="));
                m_layoutButton->addWidget(newbutton, 2, 3);
                break;
            }
            default: {
                break;
            }
            }
        }


        //view setup
        viewer = new QLabel();
        viewerString = new QString("");
        viewer->setText("00,0");
        m_layoutView->addWidget(viewer, 0, 0);
    }


}

Widget::~Widget()
{
}

void Widget::calcResult()
{
    qDebug("calcResult");

    //-->slice ligne
    QQueue<QString> *splitResult = new QQueue<QString>;

    QString *curentChar = new QString();
    QString *construcLign = new QString();
    for (quint8 i = 0;i<viewerString->length() ;i++ ) {
        *curentChar = viewerString->at(i);
        //qDebug() << viewerString[0][i]; // same ?
        //qDebug() << viewerString->at(i); //same ?

        if (*curentChar == "-") {
            splitResult->enqueue(*construcLign);
            *construcLign = "";
            splitResult->enqueue("-");
        }
        else if (*curentChar == "+") {
            splitResult->enqueue(*construcLign);
            *construcLign = "";
            splitResult->enqueue("+");
        }
        else {
            *construcLign += *curentChar;
        }
    }
    splitResult->enqueue(*construcLign);


    delete curentChar;
    delete construcLign;

    //-->calcule
    float_t *result = new float_t();
    QString *curentCalc = new QString();
     *result = splitResult->dequeue().toFloat();
    qDebug()<<*result;
    while (!splitResult->isEmpty()) {
        if (splitResult->dequeue() == "-") {
            *result -= splitResult->dequeue().toFloat();
            qDebug()<<*result;
        }
        else if (splitResult->dequeue() == "+") {
            *result += splitResult->dequeue().toFloat();
            qDebug()<<*result;
        }

    }
    qDebug()<<"calc =";
    qDebug()<<*result;
    delete curentCalc;
    delete splitResult;


    viewer->setText(QString::number(*result));
    *viewerString = "";
    delete result;


}


void Widget::numNPresed()
{
    QObject *emetteur = sender(); // emetteur contient le QPushButton btn si on clique sur ce bouto
    Button *emetteurCasted = qobject_cast<Button*>(emetteur); // On caste le sender en ce que nous supposons qu'il soit
    if(emetteurCasted) //emetteurCasted vaut 0 si le cast à échoué
    {
        qint8 emetKey = emetteurCasted->getKeyId();
        qDebug() << emetKey;

        if (emetKey <=9) {
        *viewerString += QString::number(emetKey);
        }
        else {
            switch (emetKey) {
            case 10: {
                *viewerString += QString("-");
                break;
            }
            case 11: {
                *viewerString += QString("+");
                break;
            }
            case 12: {
                //en dessous
                break;
            }
            default: {
                break;
            }

            }
        }

        if (emetKey == 12) {
            Widget::calcResult(); //deleg result
        }
        else {
            viewer->setText(*viewerString);
        }


    }
}

