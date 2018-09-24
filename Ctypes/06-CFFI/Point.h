//==============================================================================
//
// Title:		Point.h
// Purpose:		A short description of the interface.
//
// Created on:	2018/9/24 at 7:51:10 by .
// Copyright:	. All Rights Reserved.
//
//==============================================================================

#ifndef __Point_H__
#define __Point_H__

#ifdef __cplusplus
    extern "C" {
#endif

//==============================================================================
// Include files

#include "cvidef.h"

//==============================================================================
// Constants

//==============================================================================
// Types

//==============================================================================
// External variables

//==============================================================================
// Global functions

/* Point.h */
/* Simple structure for ctypes example */
typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    float x;
   	float y;
} Point_float;




__declspec(dllexport) void show_point(Point point);
__declspec(dllexport) void move_point(Point point);
__declspec(dllexport) void move_point_by_ref(Point *point);
__declspec(dllexport) Point get_point(int x, int y);
__declspec(dllexport) Point_float get_point_float(float x, float y);
__declspec(dllexport) Point get_default_point(void);

__declspec(dllexport) float add_float(float a,float b);
__declspec(dllexport) int add_int(int a,int b);
__declspec(dllexport) int add_float_ref(float *a,float *b,float *c);
__declspec(dllexport) int add_int_array(int *a,int *b,int *c,int n) ;


typedef struct _rect{
	float height,width;
	
}Rectangle;
__declspec(dllexport) float area(Rectangle rect);

//////////// enum //////////////
typedef enum{
	ZERO,
	ONE,
	TWO
}MyEnum;

__declspec(dllexport) int getAnEnumValue(MyEnum anEnum);


#ifdef __cplusplus
    }
#endif

#endif  /* ndef __Point_H__ */
