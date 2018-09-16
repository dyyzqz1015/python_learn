#include "square_array_struct.h"

void square_array(DATA* data)
{
    int i;
    for (i=0; i<data->n; i++){
        data->outa[i] = data->ina[i]*data->ina[i];
        }
}