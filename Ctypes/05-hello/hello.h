//==============================================================================
//
// Title:		hello.h
// Purpose:		A short description of the interface.
//
// Created on:	2018/9/23 at 22:40:05 by .
// Copyright:	. All Rights Reserved.
//
//==============================================================================

#ifndef __hello_H__
#define __hello_H__

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

__declspec(dllexport) char const* greet() ;
__declspec(dllexport) int sum(int a,int b);
__declspec(dllexport) int add_one(int i);
__declspec(dllexport) void print_array(double* array, int N) ;
#ifdef __cplusplus
    }
#endif

#endif  /* ndef __hello_H__ */
