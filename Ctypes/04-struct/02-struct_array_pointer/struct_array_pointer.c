struct particle
{
    double x;
    double y;
 };

__declspec(dllexport) struct particle* getParticles()
{
    static struct particle p[3] = {1.1,2.2,3.3,4.4,5.5,6.6};
    return p;
}