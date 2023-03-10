#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:21:21 2023

@author: tristan
"""

import numpy as np

"""1"""
def F1(x):
    return np.abs(x-100)

def F2(x):
    a=0
    if x>=50 :
        a=np.sqrt(x-50)
    else :
        a=np.sqrt(-(x-50))
    return a

def F3(x):
    if 4*x>x+5:
        return x+5
    else:
        return 4*x
    
    

def F4(x):
    return -x**3



def dichoto(f,a,b,eps):
    
    while b - a > eps :
       c = (a + b) / 2
       if f(c) == 0:
           return c
       elif f(a)*f(c) < 0:
            b = c
           
       else:
            a = c
            

    return (a + b) / 2

eps = 1e-6
print(dichoto(F1, -1000, 1000, eps)) # 100.0
print(dichoto(F2, -1000, 1000, eps)) # 50.0
print(dichoto(F3, -1000, 1000, eps)) # -1.25
print(dichoto(F4, -1000, 1000, eps)) # 0.0

"""methode du nombre d'or"""

#Q4
"""Xg=bk-v = bk-w/α = bk-(bk-ak)/α""" 
"""Xd=ak+v = ak + (bk-ak)/α"""

#Q5
""" Dans le cas 1 et 2 l'intervalle est réduit d'un tiers à chaque foix 
dans le cas 3 l'intervalle et reduit de moitié"""

#Q6
"""à chaque iteration il y a 2 évaluation de la fonction f"""


#Q7
""" Xd-Xg = ak - bk +2(bk-ak)/α"""
"""l'intervalle entre Xd et Xg et donc minimale lorsque on se retrouve au milieu de xg xd"""


#Q8
""" on trouve α= nb d'or"""

def golden(f, a, b, eps):
    """
    Recherche d'un zéro de la fonction `f` sur l'intervalle `[a,b]`
    avec une précision de `eps` en utilisant la méthode du nombre d'or.
    """
    
    phi = (1 + np.sqrt(5)) / 2

  
    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    while abs(b - a) > eps:
        f1, f2 = f(x1), f(x2)

        if f1 < f2:
            b = x2
            x2 = x1
            x1 = b - (b - a) / phi
        else:
            a = x1
            x1 = x2
            x2 = a + (b - a) / phi

    return (a + b) / 2


print(golden(F1, -1000, 1000, eps)) # 100.0
print(golden(F2, -1000, 1000, eps)) # 50.0
print(golden(F3, -1000, 1000, eps)) # -1.25
print(golden(F4, -1000, 1000, eps)) # 0.0







