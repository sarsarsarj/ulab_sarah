#file:subplot_time.py
import numpy as np
import matplotlib.pyplot as plt

def horz(h,k,x):
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.plot(x,h)
    plt.title('cos(x)')
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    
    plt.subplot(1,2,2)
    plt.plot(x,k)
    plt.title('sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.tight_layout()
    plt.show()
    
def vert(h,k,x):
    plt.figure(figsize=(12,5))
    plt.subplot(2,1,1)
    plt.plot(x,h)
    plt.title('cos(x)')
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    
    plt.subplot(2,1,2)
    plt.plot(x,k)
    plt.title('sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.tight_layout()
    plt.show()


