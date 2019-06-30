#include<stdio.h>
#include"struct_array.h"

int sum(struct Point a){

    return a.freq+a.power+a.x[0]+a.x[1];   
}

int main() {

    struct Point a;
    a.freq=1;
    a.power=2;
    a.x[0]=1;
    a.x[1]=2;

    printf("sum:%d",sum(a));
    return 0;
}