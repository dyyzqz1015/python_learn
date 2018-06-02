#include "dome.h"
#include "ui_dome.h"

Dome::Dome(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Dome)
{
    ui->setupUi(this);
}

Dome::~Dome()
{
    delete ui;
}
