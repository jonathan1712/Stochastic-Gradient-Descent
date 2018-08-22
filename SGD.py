import numpy as np
import scipy.misc as sc
import random
import matplotlib.pyplot as plt

def funcion_a(x):
    return x**2 + 2

def funcion_b(x):
    #return np.cos(x)
    return x**3

def grafica_funcion(funcion, puntos):
    _x = np.linspace(-10, 10, puntos, endpoint=True)
    for x in _x:
        plt.plot(x,funcion(x),".",c="blue")

def SGC(alpha,theta0,iteraciones,funcion):
    start_iter = 0
    theta= theta0
    plt.plot(theta,funcion(theta),"o",c="green")
    for iter in range(start_iter + 1, iteraciones, + 1):
        grad = sc.derivative(funcion,theta)
        theta = theta - (alpha * grad)
        plt.plot(theta,funcion(theta),".",c="yellow")

    plt.plot(theta,funcion(theta),"o",c="red")
    plt.show()    
    return theta    

def main():
    ### polinimo 1 - funcion = x**2 + 2
    #grafica_funcion(funcion_a, 100)
    #xi = random.randint(-10, 10)
    #SGC(0.1,xi,100,funcion_a)

    ### polinomio 2 - funcion = cos(x)
    
    grafica_funcion(funcion_b, 100)
    xi = random.randint(-10, 10)
    SGC(0.0001,xi,100,funcion_b)
    
    

main()


