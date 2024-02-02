# -*- coding: utf-8 -*-
"""
@author: Hiba Irfan
"""
import numpy as np

def guass_elimination(A,B,equations):
    values = np.zeros(equations)
    aug = np.concatenate((A, np.expand_dims(B, axis=1)), axis=1)
    print('Apply Guass Elimination')
    for i in range(equations): # row
        for j in range(i+1,equations): # col
            key =  aug[j,i] / aug[i,i]
            aug[j][:] = aug[j][:] - key* aug[i][:]
    print("After Guass Elimination Method")
    for i in range(equations):
        augmented_str = "  ".join([f"{aug[i][j]}" for j in range(equations)])
        print(f"{augmented_str}  |  {aug[i,j+1]}")
    print()
    for i in range(equations - 1, -1, -1):
        values[i] = (aug[i, -1] - np.dot(aug[i, :-1], values)) / aug[i, i]

    for i in range(len(values)):
        print(f'x{i+1} :: ',values[i])
    
def guass_jordan(A,B,equations):
    print('Apply Guass Jordan')
    values = np.zeros(equations)
    aug = np.concatenate((A, np.expand_dims(B, axis=1)), axis=1)
    for i in range(equations): # row
        for j in range(i+1,equations): # col
            key =  aug[j,i] / aug[i,i]
            aug[j][:] = aug[j][:] - key* aug[i][:]
    for i in range(equations - 1, -1, -1): # row
        for j in range(i - 1, -1, -1): # col
            key =  aug[j,i] / aug[i,i]
            aug[j][:] = aug[j][:] - key* aug[i][:]
            
   
    for i in range(equations):
        values[i] = (aug[i, equations]  / aug[i, i])

    print()
    print("After Guass Jordan Method")
    for i in range(equations):
        augmented_str = "  ".join([f"{aug[i][j]}" for j in range(equations)])
        print(f"{augmented_str}  |  {aug[i,j+1]}")
    print()
    for i in range(len(values)):
        print(f'x{i+1} :: ',values[i])
    
def jacobi(A,B,equations):
    print('Apply Jacobi Method')
    for i in range(equations):
        sum = 0
        for j in range(equations):
            if i != j:
                sum = sum + A[i][j]
        if(A[i][i] > sum):
            print('')
        else:
            print('Error in equation')
            return 0
            break
    values = np.zeros(equations)
    cond = True
    while(cond):
        prev_x = values.copy()
        for i in range(equations):
            val = 0
            for j in range(equations):
                if i != j:
                    val += A[i][j] * prev_x[j]
            values[i] = (B[i] - val) / A[i][i]
        for i in range(len(values)):
            if(values[i] == prev_x[i]):
                cond = False
        
    print()    
    for i in range(len(values)):
        print(f'x{i+1} :: ',values[i])
    
def seidel(A,B,equations):
    print('Aplly Seidel Method')
    for i in range(equations):
        sum = 0
        for j in range(equations):
            if i != j:
                sum = sum + A[i][j]
        if(A[i][i] > sum):
            print('')
        else:
            print('Error in equation')
            return 0
            break
    values = np.zeros(equations)
    cond = True
    while(cond):
        prev_x = values.copy()
        next_x = values.copy()
        for i in range(equations):
            val = 0
            for j in range(equations):
                if i != j:
                    val += A[i][j] * next_x[j]
            values[i] = (B[i] - val) / A[i][i]
            next_x[i] = values[i]
        for i in range(len(values)):
            if(values[i] == prev_x[i]):
                cond = False
        
    print()        
    for i in range(len(values)):
        print(f'x{i+1} :: ',values[i])
    
print('Choose Method')
print('1) Guass Elimination')
print('2) Guass Jordan')
print('3) Jacobi method')
print('4) Seidel method')

choose_methd = int(input('Select :: '))

print('Enter Equation values:: ')

A = []
B = []

equations = int(input("Enter the number of equations: "))
variables = equations
for i in range(1,equations+1):
    row = []
    print('Equation number ',i)
    for j in range(1,equations+1):
        val =int(input(f'Enter value of x{j} :: '))
        row.append(val)
        if j==equations:
            val =int(input('Enter value of Equation :: '))
            B.append(val)
    A.append(row)
    
print("\nEquations:")
for i in range(equations):
    equation_str = " + ".join([f"({A[i][j]})x{j+1}" for j in range(equations)])
    print(f"{equation_str} = {B[i]}")
    
print("\nAugmented Matrix:")
for i in range(equations):
    augmented_str = "  ".join([f"{A[i][j]}" for j in range(equations)])
    print(f"{augmented_str}    |   {B[i]}")
print()
if choose_methd == 1:
    guass_elimination(A,B,equations)
elif choose_methd == 2:
    guass_jordan(A,B,equations)
elif choose_methd == 3:
    jacobi(A,B,equations)
elif choose_methd == 4:
    seidel(A,B,equations)
else:
    print('Method not found')