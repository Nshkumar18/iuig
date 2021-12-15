show databases;
USE person;
CREATE TABLE SalesPeople (
Snum int NOT NULL,
Sname VARCHAR(20) NOT NULL,
City VARCHAR(20),
comm int,
Primary key (Snum),
Unique(Sname));
INSERT INTO SalesPeople
values(1001, 'Peel', 'London',12);
INSERT INTO SalesPeople
values(1002,  'Serres', 'Sanjose',13);
INSERT INTO SalesPeople
values(1004 , 'Motika' , 'London' ,11);
INSERT INTO SalesPeople
values(1007, 'Rifkin',' Barcelona',15);
INSERT INTO SalesPeople
VALUES(1003,'Axelrod',' Newyork',10);
CREATE TABLE Customers (
Cnum int NOT NULL,
Cname VARCHAR(20), 
City VARCHAR(20) NOT NULL,
Snum int,
primary key (Cnum),
foreign key (Snum) references SalesPeople(Snum));
INSERT INTO Customers
values(2001,'Hoffman','London',1001);
INSERT INTO Customers
values(2002,'Giovanni','Rome',1003);
INSERT INTO Customers
values(2003 ,'Liu','Sanjose',1002);
INSERT INTO Customers
values(2004,'Grass','Berlin',1002);
INSERT INTO Customers
values(2006,'Clemens','London',1001);
INSERT INTO Customers
values(2008,'Cisneros','Sanjose',1007);
INSERT INTO Customers
values(2007,'Pereir','Rome', 1004);
CREATE TABLE Orders (
Onum int NOT NULL,
Amt int,
Odate date ,
Cnum int NOT NULL,
Snum int NOT NULL,
Primary Key (Onum),
foreign key (Cnum) references Customers(Cnum),
foreign key (Snum) references SalesPeople(Snum));
INSERT INTO Orders
values(3001,18.69,3/10/1990, 2008, 1007);
INSERT INTO Orders
values(3003,767.19,3/10/1990,2001,1001);
INSERT INTO Orders
values(3002,1900.10,3/10/1990,2007,1004);
INSERT INTO Orders
values(3005,5160.45,3/10/1990,2003,1002);
INSERT INTO Orders
values(3006,1098.16,3/10/1990,2008,1007);
INSERT INTO Orders
values(3009,1713.2,4/10/1990,2002,1003);
INSERT INTO Orders
values(3007,75.75,4/10/1990,2004,1002);
INSERT INTO Orders
values(3008,4273.00,5/10/1990,2006,1001);
INSERT INTO Orders
values(3010,1309.95,6/10/1990,2004,1002);
INSERT INTO Orders
values(3011,9891.88,6/10/1990,2006,1001); 
SELECT COUNT(City)
FROM SalesPeople
WHERE city = 'Newyork';
SELECT count(Sname)
from Salespeople
WHERE Sname LIKE 'a%' OR 'A%';
SELECT * FROM orders
WHERE amt > 2000;
SELECT COUNT(City)
FROM SalesPeople
WHERE city = 'London' and 'Paris';
Select * From orders; 
