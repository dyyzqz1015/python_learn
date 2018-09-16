struct DATA;

typedef struct DATA{
    int n;
    double *ina;
    double *outa;
} DATA;

__declspec(dllexport) void square_array(DATA* data);