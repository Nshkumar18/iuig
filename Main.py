from show import *
print('Hello Guys ! Welcome to Book_My_Show.com')
rows = input('Please Enter  Desired Row in theatre :/n')
columns = input('Please Enter  Desired Row in theatre :/n')

def Showoptions():
    print('Select from Below Options')
    print('1.Show Seats/n2.Buy a Ticket/n3.Statistics/n4.Show Booked Tickets User Info/n0.Exist')
    n = input()
    return int(n)
n = Showoptions()
m = Seats.Theatre(int(rows), int(columns))
q = 0
Customers = []
while n != 0:
    q = 0
    if n == 1:
        print('1.Show the seats')
        Seats.show_seats(m)
    elif n == 2:
        print('2.Buy a Ticket')
        r = int(input('Enter your Desired Row of seat'))
        c = int(input('Enter your Desired Column of seat'))
        for j in Customers:
            if j.Seats == (r, c):
                print('Sorry,Seats has been Reserved')
                print('***********')
                n = Showoptions()
                q = 1
        if q == 1 :
            continue
        TP = stats.Ticket_price(int(row), int(column), r)
        print('your ticket price is ;', TP, '$')
        inp = input('Press y to proceed further/nPress n to return Main Menu/n')
        if inp == y:
            Name = input('Enter your Name :/n')
            Gender = input('Enter your Gender :/n')
            Age = int(input('Enter your Age :/n'))
            Phn = int(input('Enter your Phn :/n'))
            print('***Thanks for Details***')
            i = Info.Cus_Details(Name, Gender, Age, Phn, (r, c))
            Customers.append(i)
            m = Buy_a_Ticket.book_a_ticket(m,r,c)
        elif inp == n :
             pass
        else:
            print('Please enter Valid option/n Returning to Main Menu/n............./n')
    elif n ==3:
          print('3.Statistics')
          stats.show_stats(m)
    elif n == 4 :
         print('4.Show Booked Tickets User Info')
         for i in Customers:
             i.Print_Details()
    else :
         print('Sorry ! Please Select Valid Options')
         n=Showoptions()
         
print('Thanks for Choosing Book_My_Show.com,Dont hesitate to visit again us')         
        
            
            
            
            
