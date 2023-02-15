-- to check the database was created
-- SHOW DATABASES;

-- make sure you choose the database to use
USE LittleLemonDB;

-- check tables were added
-- show tables;

-- Code below prevents error when inserting data due to foreign keys
-- SET FOREIGN_KEY_CHECKS=0;

INSERT INTO MenuItems (MenuItemsID, CourseName, Type, Price)
VALUES
(1,'Olives','Starters',5),
(2,'Flatbread','Starters', 5),
(3, 'Minestrone', 'Starters', 8),
(4, 'Tomato bread','Starters', 8),
(5, 'Falafel', 'Starters', 7),
(6, 'Hummus', 'Starters', 5),
(7, 'Kabasa', 'Main Courses', 17),
(8, 'Greek salad', 'Main Courses', 15),
(9, 'Bean soup', 'Main Courses', 12),
(10, 'Pizza', 'Main Courses', 15),
(11,'Greek yoghurt','Desserts', 7),
(12, 'Ice cream', 'Desserts', 6),
(13, 'Cheesecake', 'Desserts', 4),
(14, 'Athens White wine', 'Drinks', 25),
(15, 'Corfu Red Wine', 'Drinks', 30),
(16, 'Turkish Coffee', 'Drinks', 10);

INSERT INTO Menus (MenuID, MenuItemsID, Cuisine)
VALUES
(1, 1, 'Greek'),
(2, 7, 'Greek'),
(3, 10, 'Greek'),
(4, 13, 'Greek'),
(5, 3, 'Italian'),
(6, 9, 'Italian'),
(7, 12, 'Italian'),
(8, 15, 'Italian'),
(9, 5, 'Turkish'),
(10, 17, 'Turkish'),
(11, 11, 'Turkish'),
(12, 16, 'Turkish');

INSERT INTO Customers (CustomerID, FullName, ContactNumber)
VALUES
(1, 'Vanessa McCarthy', 111111),
(2, 'Marcos Romero', 222222),
(3, 'Anna Iversen', 333333),
(4, 'Joakim Iversen', 444444),
(5, 'Diana Pinto', 555555),
(6, 'Hiroki Yamane', 666666);

INSERT INTO Employees (EmployeeID, Name, Role, Address, Contact_Number, Email, Annual_Salary)
VALUES
(01,'Mario Gollini','Manager','724, Parsley Lane, Old Town, Chicago, IL', 351258074, 'Mario.g@littlelemon.com', '70000'),
(02,'Adrian Gollini','Assistant Manager','334, Dill Square, Lincoln Park, Chicago, IL', 351474048, 'Adrian.g@littlelemon.com', '65000'),
(03,'Giorgos Dioudis','Head Chef','879 Sage Street, West Loop, Chicago, IL', 351970582, 'Giorgos.d@littlelemon.com', '50000'),
(04,'Fatma Kaya','Assistant Chef','132  Bay Lane, Chicago, IL', 351963569, 'Fatma.k@littlelemon.com', '45000'),
(05,'Elena Salvai','Head Waiter','989 Thyme Square, EdgeWater, Chicago, IL', 351074198, 'Elena.s@littlelemon.com', '40000'),
(06,'John Millar','Receptionist','245 Dill Square, Lincoln Park, Chicago, IL', 351584508, 'John.m@littlelemon.com', '35000');

INSERT INTO Bookings (BookingID, BookingDate, TableNumber, CustomerID, EmployeeID)
VALUES
(1, '2020-01-15', 3, 3, 1),
(2, '2020-08-25', 1, 4, 2),
(3, '2021-08-17', 1, 1, 3),
(4, '2021-08-14', 4, 2, 4),
(5, '2020-12-20', 6, 6, 6),
(6, '2020-03-01', 5, 5, 5);

INSERT INTO Orders (OrderID, MenuID, CustomerID, Quantity, TotalCost)
VALUES
(1, 1, 3, 6, 250),
(2, 2, 4, 5, 200),
(3, 2, 1, 3, 100),
(4, 3, 2, 4, 150),
(5, 1, 6, 2, 90),
(6, 4, 5, 1, 60);

