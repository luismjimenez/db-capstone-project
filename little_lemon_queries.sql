-- View for orders with quantity greater than 2
CREATE VIEW OrdersView AS (
SELECT OrderID, Quantity, Bill_Amount
FROM Orders
WHERE Quantity > 2
);

-- Order details for orders with cost greater than 150
SELECT
	c.CustomerID,
    c.FullName,
    o.OrderID,
    o.TotalCost,
    m.Cuisine,
    mi.CourseName
FROM Orders o
INNER JOIN Customers c
  ON o.CustomerID = c.CustomerID
INNER JOIN Menus m
  ON o.MenuID = m.MenuID
INNER JOIN MenuItems mi
  ON m.MenuItemsID = mi.MenuItemsID
WHERE o.TotalCost > 150
ORDER BY o.TotalCost;

-- stored procedure to get the order with the max quantity 
CREATE PROCEDURE GetMaxQuantity()  
SELECT MAX(Quantity) AS "Max Quantity in Order"
FROM Orders;

CALL GetMaxQuantity();

-- prepared statement to get order details using user input order id
PREPARE GetOrderDetail 
FROM 'SELECT OrderID, Quantity, TotalCost FROM Orders WHERE OrderID = ?';

SET @id = 1;
EXECUTE GetOrderDetail USING @id;

-- stored procedure to cancel a booking
DROP procedure CancelBooking;
DELIMITER //
CREATE PROCEDURE CancelBooking(IN CancelID INT)
BEGIN
DELETE FROM Bookings WHERE BookingID = CancelID;
SELECT CONCAT("Order ",CancelID, " is cancelled.") AS Confirmation FROM Bookings;
END//
DELIMITER ;

CALL CancelBooking(5);

-- update booking procedure
CREATE PROCEDURE UpdateBooking(IN UpdateID INT, IN TableNo INT)
UPDATE Bookings
SET TableNumber = TableNo
WHERE BookingID = UpdateID;

CALL UpdateBooking(6, 1);

SELECT * FROM Bookings;

-- a procedure to add a booking
CREATE PROCEDURE AddBooking(IN AddBookingID INT, IN AddBookingDate DATE, IN AddTableNo INT, IN AddCustomerID INT, IN AddEmployeeNum INT)
INSERT INTO Bookings (BookingID, BookingDate, TableNumber, CustomerID, EmployeeID)
VALUES (AddBookingID, AddBookingDate, AddTableNo, AddCustomerID, AddEmployeeNum);

-- call the procedure 
CALL AddBooking(5, "2022-12-30", 4, 3, 1);

-- check the bookings table
SELECT * FROM Bookings;

-- a procedure to check whether a table in the restaurant is already booked
DROP PROCEDURE IF EXISTS CheckBooking;
CREATE PROCEDURE CheckBooking(IN CheckBookingDate DATE, IN CheckTable INT)
SELECT IF((BookingDate = CheckBookingDate AND tableNumber = CheckTable), 
		CONCAT("Table ",CheckTable, " is already booked."), CONCAT("Table ",CheckTable, " is available.")) AS "Booking Status"
FROM Bookings
WHERE BookingDate = CheckBookingDate AND TableNumber = CheckTable;

CALL CheckBooking("2022-12-30", 5);

-- check Bookings table
SELECT * FROM Bookings;
