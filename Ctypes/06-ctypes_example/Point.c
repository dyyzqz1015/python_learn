#include <ansi_c.h>
#include "Point.h"
//==============================================================================
//
// Title:		Point.c
// Purpose:		A short description of the implementation.
//
// Created on:	2018/9/24 at 7:51:10 by .
// Copyright:	. All Rights Reserved.
//
//==============================================================================

//==============================================================================
// Include files

//#include "Point.h"

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
/* Point.c */
/* display a Point value */
void show_point(Point point) {
    printf("Point in C      is (%d, %d)\n", point.x, point.y);
}

/* Increment a Point which was passed by value */
void move_point(Point point) {
    show_point(point);
    point.x++;
    point.y++;
    show_point(point);
}

/* Increment a Point which was passed by reference */
void move_point_by_ref(Point *point) {
    show_point(*point);
    point->x++;
    point->y++;
    show_point(*point);
}

/* Return by value */


Point get_point(int x, int y) {
    Point point = { x, y };
    printf("Returning Point    (%d, %d)\n", point.x, point.y);
    return point;
}

Point_float get_point_float(float x, float y) {
    Point_float point = { x, y };
    printf("Returning Point    (%f, %f)\n", point.x, point.y);
    return point;
}



Point get_default_point(void) {
    static int x_counter = 0;
    static int y_counter = 100;
    x_counter++;
    y_counter--;
    return get_point(x_counter, y_counter);
}	

float add_float(float a,float b){
	return a+b;
}

int add_int(int a,int b){
	return a+b;
}

int add_float_ref(float *a,float *b,float *c){
	*c=*a+*b;
	return 0;
}

int add_int_array(int *a,int *b,int *c,int n){
	int i;
	for(i=0;i<n;i++){
		c[i]=a[i]+b[i];
			 
	}
	return 0;	 
	
}


float area(Rectangle rect){
	return rect.height*rect.width ;
}

int getAnEnumValue(MyEnum anEnum){
	return (int)anEnum;
} 


