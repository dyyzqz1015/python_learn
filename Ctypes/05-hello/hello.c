#include <ansi_c.h>
//==============================================================================
//
// Title:		hello.c
// Purpose:		A short description of the implementation.
//
// Created on:	2018/9/23 at 22:40:05 by .
// Copyright:	. All Rights Reserved.
//
//==============================================================================

//==============================================================================
// Include files

//#include "hello.h"

//==============================================================================
// Constants

//==============================================================================
// Types

//==============================================================================
// Static global variables

//==============================================================================
// Static functions

//==============================================================================
// Global variables

//==============================================================================
// Global functions

/// HIFN  What does your function do?
/// HIPAR x/What inputs does your function expect?
/// HIRET What does your function return?
char const* greet() 
{
	return "hello, world"; 
}

int sum(int a,int b)
{
	return a+b;
}


int add_one(int i)
{
    return i+1;
}


void print_array(double* array, int N)
{
    for (int i=0; i<N; i++) 
        array[i]=i;
}

int main(){

	printf("Hello,world!");

	
	getchar();
	return 0;
}
