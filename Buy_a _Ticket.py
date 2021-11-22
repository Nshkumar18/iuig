def book_a_ticket(m,r,c):
    m[r-1][c-1] = 'B'
    print('Ticket Booked Successfully!')
    print('***************')
    return m