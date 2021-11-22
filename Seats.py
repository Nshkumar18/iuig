import numpy as np

def Theatre(r,c):
    m = []
    for i in range(r):
        temp=[]
        for j in range(c):
            temp.append('s')
        m.append(temp)
    return np.array(m)
 
def show_seats(m):
    print('layout:/n')    
    r,c=np.shape(m)
    for j in range(c+1):
        print(j,end=' ')
    print('/n')
    for i in range(r):
        print(i+1,*m[i])
    print('/n Your Screen is Here')
    Print('*****************')