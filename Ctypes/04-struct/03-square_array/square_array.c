#include <stdio.h>

__declspec(dllexport) void square_array(int n, double* ina, double* outa)
{
    int i;
    for (i=0; i<n; i++){
        outa[i] = ina[i]*ina[i];
    }
}