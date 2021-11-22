import numpy as np

def Ticket_price(row,column,r) :
    if row*column <= 60 :
        TP=10
    else :
        if r < (row/2) :
            TP=10
        else :
            TP=8
    return TP
        
def Total_Income(m):
    r,c=np.shape(m)
    if r <= 60 :
        TI = r*c*10
    else :
        TI = ((r//2)*10)*c + ((r-(r//2))*8)*c
    return TI

def show_stats(m):
     B = np.array([])
     r,c = np.shape(m)
     for i in range (r):
        for j in range (c):
           if m[i][j] == 'B' :
               B = np.append(B,i)
               
     P = np.array([])
     for i in B:
         u = Ticket_price(r,c,i)
         P = np.append(P,u)
      
     print('Number of Purchased tickets :', np.array(B)[0])
     print('Percentage :',(np.array(B)[0]/(r*c))*100,'%')
     print('Total Income : $',Total_Income(m))
     print('Current Income :$',Total_Income(m))
     print("*******************")        
   
        
      
            
   
        
        
        