# -*- coding: utf-8 -*-
"""
@author: HIba Irfan
"""
import math
print("================= Welcome to the Root Finder ==============")
print("")
print("=========== Methods ==============")


itr = 0
tol_type = None
def f(x):
    return 3*(x+1)*(x-1/2)*(x-1)
def d(x):
    return (9*math.pow(x,2))-(3*x)-(3)
    
def bisection(a,b,choice,itr,tol,tol_type):
    print('Bisection Method :: ')
    m=0
    if(f(a)*f(b)<0):
        if choice == 1:
            for i in range(itr):
                m = (a+b)/2
                if (f(m) == 0 or abs(f(m))<tol):
                    return m
                
                if(f(m)*f(a)<0):
                    b = m
                elif(f(m)*f(b)<0):
                    a = m
                else:
                    print('') 
                print("iteration = %d The m value is :: %0.6f" % (i+1,m))
            return 'None'
            
        else:
            while(abs(f(m)) > tol):
                if tol_type == 1:
                    if abs(f(b) - f(a)) <= tol:
                        return m
                    
                elif tol_type == 2:
                    if abs(b - a) / 2 < tol:
                        return m
                m = (a+b)/2
                if(f(a)*f(m)<0):
                    b = m
                elif(f(b)*f(m)<0):
                    a = m
                else:
                    print('')
            return m
                      
    else:
        print('No root between this interval')

   
def regualr_falsi(a,b,choice,itr,tol,tol_type):
    print('Regular Falsi Method :: ')
    x=0
    if(f(a)*f(b)<0):
        if choice == 1:
            for i in range(itr):
                x = (a * f(b) - b * f(a))/ (f(b) - f(a))
                if (f(x) == 0 or abs(f(x))<tol):
                    return x
                
                if(f(x)*f(a)<0):
                    b = x
                elif(f(x)*f(b)<0):
                    a = x
                else:
                    print('no root found') 
                print("iteration = %d The value is :: %0.6f" % (i+1,x))
            return 'None'

        else:
            while(abs(f(x)) > tol):
                x = (a * f(b) - b * f(a))/ (f(b) - f(a))

                if(f(x)*f(a)<0):
                    b = x
                elif(f(x)*f(b)<0):
                    a = x
                else:
                    print('no root found') 
                    
                if tol_type == 1:
                    if abs(f(x)) < tol:
                        return x
                   
                elif tol_type == 2:
                    if abs(b-a) < tol:
                        return x
            return x
    else:
        print('No root between this interval')
    
    
def secant(a,b,choice,itr,tol,tol_type):
    print('Secant Method :: ')
    x=0
    if(f(a)*f(b)<0):
        if choice == 1:
            for i in range(itr):

                x = b - f(b) * (b - a) / (f(b) - f(a))
                print("iteration = %d The value is :: %0.6f" % (i+1,x))
                if (f(x) == 0 or abs(f(x))<tol):
                    return x
                a=b
                b=x
                 
            
            return 'None'
        else:
            while(abs(f(x)) > tol):
                if f(a) == f(b):
                    break
                
                if tol_type == 1:
                    if abs(f(x)) <= tol:
                        return x
                elif tol_type == 2:
                    if abs(f(x) - f(a)) < tol:
                        return x
                    
                x = (a * f(b) - b * f(a))/ (f(b) - f(a))
                a=b
                b=x
            return 'None'
    else:
        print('No root between this interval')
    
def newton_raphson(x0,choice,itr,tol,tol_type):
    print('Newton Raphson Method :: ')
    x = x0
    if choice == 1:
        for i in range(itr):
            if d(x0) == 0.0:
                break
            fx = f(x)
            dx = d(x)
            x = x0 - fx/dx
            fx = f(x)
            x0 = x
            if abs(fx) < tol:
                return x
            
            if abs(dx) < tol:
                print('Error')
                break
            print("iteration = %d The value is :: %0.6f" % (i+1,x))  
        return 'None'
    else:
        while(abs(f(x)) > tol):
            fx = f(x)
            dx = d(x)
            x = x0 - f(x0)/d(x0)
            x0 = x
            
            
            if abs(d(x)) < tol:
                   print('Error')
                   break

            if tol_type == 1:
                if abs(f(x)) < tol:
                    return x
                
            elif tol_type == 2:
                if abs(x-x0) <= tol:
                    return x
        return 'None'
   
    
    
    
    
    
    
print("1. Bisection Method")
print("2. Regular Falsi ")
print("3. Secant Method")
print("4. Newton Raphson Method")
choice_func = int(input('Enter which method you want to choice:: '))

choice= int(input('Enter 1 to find by iteration otherwise enter 2 to find by tolerance level ::'))
if choice == 1:
    itr = int(input('Enter number of iteration :: '))
    tol = float(input('Enter number of tolerance :: '))
else:
    tol = float(input('Enter number of tolerance :: '))
    print('1.function value on root')
    print('2. Root Value ')
    tol_type = int(input('Enter Type of tolerance ::  '))
    
    


if(choice_func==4):
    a = float(input("Enter the initial guess: "))
else:
    a = float(input("Enter the first initial guess: "))
    b = float(input("Enter the second initial guess: "))

if(choice_func == 1):
    print()
    root = bisection(a,b,choice,itr,tol,tol_type)
    print("Required Root is :: " ,root)
elif(choice_func == 2):
    root = regualr_falsi(a,b,choice,itr,tol,tol_type)
    print("Required Root is :: " ,root)
elif(choice_func== 3):
    root = secant(a,b,choice,itr,tol,tol_type)
    print("Required Root is :: " ,root)
elif(choice_func == 4):
    root = newton_raphson(a,choice,itr,tol,tol_type)
    print("Required Root is :: " ,root)
else:
    print('No method')
    