#ifndef DOME_H
#define DOME_H

#include <QWidget>

namespace Ui {
class Dome;
}

class Dome : public QWidget
{
    Q_OBJECT

public:
    explicit Dome(QWidget *parent = 0);
    ~Dome();

private:
    Ui::Dome *ui;
};

#endif // DOME_H
