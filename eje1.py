#! /usr/bin/python
#!encodin: UTF-8

import sys
PI=3.14159265358979323846264338327950288
n = int (sys.argv[1])
v = int (sys.argv[2])

def g(n):
  if (n!=0):
    suma=0
    for i in range(1,n+1):
      a=float(i-1)/n
      b=float(i)/n
      xi=float(i-0.5)/n
      fxi=4.0/(1.0 + xi*xi)
      suma+=fxi
    pi=float (suma)/n
    return pi
    
for j in range (1, v+1):
   pi = g(j*n)
   print pi
