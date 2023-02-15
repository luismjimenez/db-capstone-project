{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## LittleLemonDB Capstone Project \n",
    "- Creating a database client for Little Lemon using the Mysql python connector API/driver to interact with Little Lemon's database \n",
    "- Updating and deleting records in a MySQL database using Python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use to install mysql connector API if not installed\n",
    "# !pip install mysql-connector-python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# use to import the mysql connector API\n",
    "import mysql.connector as connector"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 1\n",
    "In the previous exercise you created a Python environment. In the first task of this exercise, you are tasked with extending the environment to connect with your database and interact with the data it holds. \n",
    "\n",
    "Your first step is to import the connector module, enter your user details and connect with the database (Hint: you can use an alias when importing the module).\n",
    "\n",
    "This gives you access to all the functionality available from the connector API, which can be accessed through the variable named connector (or whichever alias you choose). "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Establish connection b/w Python and MySQL database via connector API\n",
    "connection=connector.connect(\n",
    "                             user=\"YOUR_USERNAME\", # use your own\n",
    "                             password=\"YOUR_PASSWORD\", # use your own\n",
    "                             database=\"LittleLemonDB\"\n",
    "                            )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a cursor object to communicate with entire MySQL database\n",
    "cursor = connection.cursor()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Once, the connection is established, and you have a cursor object, you can select the database `little_lemon` using the code below and work with the respective table to accomplish the required tasks.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'littlelemondb'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Set the little_lemon database for use \n",
    "cursor.execute(\"USE LittleLemonDB\")\n",
    "\n",
    "# Confirm the database in use\n",
    "connection.database"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 2\n",
    "In this second task, you now need to query the database to show all tables within the database. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Tables in the LittleLemonDB database:\n",
      "--------------------------------------\n",
      "()\n",
      "('Bookings',)\n",
      "('Customers',)\n",
      "('Employees',)\n",
      "('MenuItems',)\n",
      "('Menus',)\n",
      "('Orders',)\n"
     ]
    }
   ],
   "source": [
    "# Task 1 show your database tables\n",
    "\n",
    "# create SQL query as a string object and add to a variable\n",
    "show_tables_query = \"\"\"SHOW tables\"\"\" \n",
    "\n",
    "# execute the query\n",
    "cursor.execute(show_tables_query)\n",
    "\n",
    "# fetch the results from the cursor\n",
    "results = cursor.fetchall()\n",
    "\n",
    "# Retrieve the column names\n",
    "cols = cursor.column_names[1:]\n",
    "\n",
    "# print column names and the records from results using for loop\n",
    "print(\"Tables in the LittleLemonDB database:\")\n",
    "print(\"--------------------------------------\")\n",
    "print(cols)\n",
    "for result in results:\n",
    "    print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Testing connection and database "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('CustomerID', 'FullName', 'ContactNumber')\n",
      "(1, 'Vanessa McCarthy', 111111)\n",
      "(2, 'Marcos Romero', 222222)\n",
      "(3, 'Anna Iversen', 333333)\n",
      "(4, 'Joakim Iversen', 444444)\n",
      "(5, 'Diana Pinto', 555555)\n",
      "(6, 'Hiroki Yamane', 666666)\n"
     ]
    }
   ],
   "source": [
    "### Testing connection and database ###\n",
    "\n",
    "orders_query = \"\"\"SELECT * FROM Customers\"\"\" \n",
    "\n",
    "# execute the query\n",
    "cursor.execute(orders_query)\n",
    "\n",
    "# fetch the results from the cursor\n",
    "results = cursor.fetchall()\n",
    "\n",
    "# Retrieve the column names\n",
    "cols = cursor.column_names\n",
    "\n",
    "# print column names and the records from results using for loop\n",
    "print(cols)\n",
    "for result in results:\n",
    "    print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Task 3\n",
    "\n",
    "Query with table JOIN\n",
    "\n",
    "For the third and final task, Little Lemon need you to return specific details from your database. They require the full name and contact details for every customer that has placed an order greater than $60 for a promotional campaign. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Customers with orders greater than $60:\n",
      "---------------------------------------\n",
      "('CustomerID', 'FullName', 'ContactNumber', 'TotalCost')\n",
      "(3, 'Anna Iversen', 333333, 250)\n",
      "(4, 'Joakim Iversen', 444444, 200)\n",
      "(1, 'Vanessa McCarthy', 111111, 100)\n",
      "(2, 'Marcos Romero', 222222, 150)\n",
      "(6, 'Hiroki Yamane', 666666, 90)\n"
     ]
    }
   ],
   "source": [
    "ordersgt60 = \"\"\"\n",
    "SELECT c.CustomerID, c.FullName, c.ContactNumber, o.TotalCost\n",
    "FROM Orders o\n",
    "INNER JOIN Customers c\n",
    "  ON o.CustomerID = c.CustomerID\n",
    "WHERE o.TotalCost > 60\n",
    "\"\"\"\n",
    "\n",
    "# execute the query\n",
    "cursor.execute(ordersgt60)\n",
    "\n",
    "# fetch results from the cursor, store in  a variable\n",
    "results = cursor.fetchall()\n",
    "\n",
    "# retrieve column names from the cursor\n",
    "cols = cursor.column_names\n",
    "\n",
    "# print the cols and results\n",
    "print(\"Customers with orders greater than $60:\")\n",
    "print(\"---------------------------------------\")\n",
    "print(cols)\n",
    "for result in results:\n",
    "    print(result)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Connection is already closed.\n"
     ]
    }
   ],
   "source": [
    "# Let's close the cursor and the connection\n",
    "if connection.is_connected():\n",
    "    cursor.close()\n",
    "    print(\"The cursor is closed.\")\n",
    "    connection.close()\n",
    "    print(\"MySQL connection is closed.\")\n",
    "else:\n",
    "    print(\"Connection is already closed.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.15"
  },
  "vscode": {
   "interpreter": {
    "hash": "7c4f38b42c52578f71e97848146a9c1f396fd1ce601a5fe9f664b95ee68a6a5a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
