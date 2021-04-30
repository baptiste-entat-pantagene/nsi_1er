#include "widget.h"


class SimpleItem : public QGraphicsItem
{
public:
    QRectF boundingRect() const override
    {
        qreal penWidth = 1;
        return QRectF(-10 - penWidth / 2, -10 - penWidth / 2,
                      20 + penWidth, 20 + penWidth);
    }

    void paint(QPainter *painter, const QStyleOptionGraphicsItem *option,
               QWidget *widget) override
    {
        painter->drawRoundedRect(-10, -10, 20, 20, 5, 5);
    }
};


Widget::Widget(QWidget *parent)
    : QWidget(parent)
{

    auto* itemTest = new SimpleItem;

    auto* scene = new QGraphicsScene;
    scene->addItem(itemTest);
    itemTest->paint();

    auto* view = new QGraphicsView(this);
    view->setScene(scene);
    view->resize(this->width(), this->height());
}

Widget::~Widget()
{
}

