class Cus_Details :
    
    def __init__(self,Name,Gender,Age,Phn,Seat):
        self.Name=Name
        self.Gender=Gender
        self.Age=Age
        self.Phn=Phn
        self.Seat=Seat
        
    def Print_Details(self):
        print('Name: ',self.Name)
        print('Gender :',self.Gender)
        print('Age ;',self.Age)
        print('Phn :',self.Phn)
        print('Seat : ',self.Seat)
        print('******END******')
        