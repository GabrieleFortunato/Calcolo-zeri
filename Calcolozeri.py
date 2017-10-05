
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2-9
    
def der(x):
    return 2*x

def stampafunzione():
    print("")
    print("")
    print("FUNZIONE: (y=x^2-9)")

    
def puntomedio(a,b):
    return (a+b)/2.0

def stampaintervallo(a,b):
    print ("")
    print ("Intervallo considerato: [",a,",",b,"]")     
    
def teoremadeglizeri(a,b):  
    print("")
    print ("")
    print("===================================")
    print("APPLICAZIONE DEL TEOREMA DI BOLZANO")
    print("===================================")
    print("")
    stampaintervallo(a,b)
    if (f(a)*f(b)<0):
        print ("La funzione ammette uno zero")
        print ("nell'intervallo considerato")   
    else:
        print ("La funzione non ammette zeri")
        print ("nell'intervallo considerato")
    
def metodotangenti(a,b,tol):
    print("")
    print("")
    print("======================================")
    print("APPLICAZIONE DEL METODO DELLE TANGENTI")
    print("======================================")
    print("")
    stampaintervallo(a,b)
    print ("")
    print ("Partendo da x =",a)
    x=a
    i=0
    y=f(x)
    while(abs(y)>tol): 
        x=x-(f(x)/(der(x))*1.)
        y=f(x)
        i = i+1
    print ("Numero iterate: ",i)
    print ("f(x) =",round(f(x)),"per x =",round(x))
    print("")
    print ("Partendo da x =",b)
    x=b
    i=0
    y=f(x)
    print
    while(abs(y)>tol):
        x=x-(f(x)/(der(x))*1.)
        y=f(x)
        i = i+1
    print ("Numero iterate:",i)
    print ("f(x) =",round(f(x)),"per x =",round(x))
    
        
def metodosecanti(a,b,tol):
    print("")
    print("")
    print("=====================================")
    print("APPLICAZIONE DEL METODO DELLE SECANTI")
    print("=====================================")
    print("")
    stampaintervallo(a,b)
    y = a-f(a)*(a-b)/(1.*(f(a)-f(b)))
    i = 0    
    while (abs(f(y))>tol):
        a=b
        b=y
        y = a-f(a)*(a-b)/(1.*(f(a)-f(b)))
        i = i+1      
    print ("Numero iterate: ",i)
    print ("f(x) =",round(f(y)),"per x =",round(y) )  
    
def bisezione(a,b,tol): 
    c=puntomedio(a,b);
    i = 1
    while (abs(f(c))>tol):
        if (f(c)>0):
            a=c
            c=puntomedio(a,b);
        else:
            b=c
            c=puntomedio(a,b);
        i = i+1
    print ("Numero iterate effettuate: ",i)
    print ("f(x) =",round(f(c)),"per x =",round(c))

def metodobisezione(a,b,tol):
    print("")
    print("")
    print("=======================================")
    print("APPLICAZIONE DEL METODO DELLE BISEZIONI")
    print("=======================================")
    print("")
    stampaintervallo(a,b)
    bisezione(a,b,tol)
    print("")
    
def grafico(a,b): 
    print("")
    print("")
    print("======================")
    print("GRAFICO DELLA FUNZIONE")
    print("======================")
    print("")
    x=np.linspace(a,b,100)
    plt.plot(x,f(x))
    plt.grid()
    plt.show()
   
a = -4
b =  2  
tol = 0.001
stampafunzione()
grafico(a,b)
teoremadeglizeri(a,b)
metodotangenti(a,b,tol)
metodosecanti(a,b,tol)
metodobisezione(a,b,tol)
