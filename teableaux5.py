# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 19:13:54 2022

@author: Emile
"""

import numpy as np

A = np.array([[4,-5],[np.sqrt(3),(np.pi)/4]])
print(A)

B = np.array([[2,complex(3,1)],[(-72)/3,0.2]])
print(B)

def somme(A,B):
    C = A + B
    print("\n La somme de A et B est: \n", C)
    
def produit(A,B):
    C = np.dot(A,B)
    print("\n Le produit de A et B est: \n", C)
    
def carré(A):
    C = np.dot(A,A)
    print("\n Le carré de A est: \n", C)
    
def transposée(A):
    C = A.T
    print("\n La transposée de A est: \n", C)

def inverse(B):
    C = np.linalg.inv(B)
    print("\n L'inverse de B est: \n", C)
    
def operation1(A,B):
    C = np.dot(A.T,B.T)
    print("\n L'opération A^t*B^t donne: \n", C)
    
def operation2(A,B):
    C = (np.dot(A,A) + np.dot(B,B) - np.dot(A,B))
    print("\n L'opération A^2 + B^2 - AB donne: \n", C)
    

    
somme(A,B)
produit(A,B)
carré(A)
transposée(A)
inverse(B)
operation1(A,B)
operation2(A,B)
