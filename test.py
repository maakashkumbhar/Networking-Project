from _thread import *

def sum(x,y):
    sum = x+y
    return sum
x=10
y=33
x2 = start_new_thread(sum,(x,y))
print(x2)
