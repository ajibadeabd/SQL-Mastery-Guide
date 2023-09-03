# Create Authors Table
-- Create Authors Table
CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(255) NOT NULL,
    birth_date DATE,
    nationality VARCHAR(50)
);

-- This SQL code creates a table named "Authors." Think of this table like a digital library for storing information about authors. Here's what each part of the code means:

-- CREATE TABLE Authors: This part tells the database that we want to create a new table called "Authors."

-- ( 
--     author_id INT PRIMARY KEY, 
--     author_name VARCHAR(255) NOT NULL, 
--     birth_date DATE, 
--     nationality VARCHAR(50) 
-- ): This section defines the structure of the table. It specifies the columns (or fields) the table will have:

-- author_id: This column will hold unique identification numbers for each author. Think of it like an ID card number for each author.

-- author_name: This column will store the name of the author. It's required (NOT NULL) to ensure every author has a name.

-- birth_date: This column will store the author's date of birth.

-- nationality: This column will store the author's nationality.

-- INT, VARCHAR(255), DATE, and VARCHAR(50): These are data types that define the kind of information each column will hold. For example, INT is used for numbers, VARCHAR(255) for text up to 255 characters long, and DATE for dates.

-- PRIMARY KEY: This indicates that the author_id column is the primary key, which means it uniquely identifies each author in the table.

-- Create Customers Table

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    address VARCHAR(255),
    phone VARCHAR(20)
);

-- This code creates a table called "Customers," which is like a digital record of people who buy books from an online store. Here's what each part means:

-- CREATE TABLE Customers: This part tells the database we're creating a new table called "Customers."

-- ( 
--     customer_id INT PRIMARY KEY, 
--     first_name VARCHAR(50) NOT NULL, 
--     last_name VARCHAR(50) NOT NULL, 
--     email VARCHAR(100), 
--     address VARCHAR(255), 
--     phone VARCHAR(20) 
-- ): This section defines the structure of the "Customers" table:

-- customer_id: A unique identification number for each customer, like a membership number.

-- first_name and last_name: Columns for storing the customer's first and last names. They're required to ensure every customer has a name.

-- email: This column can store the customer's email address.

-- address: The customer's address, which can be up to 255 characters long.

-- phone: The customer's phone number.

-- Data types like INT, VARCHAR(50), and VARCHAR(100) specify what kind of data each column will hold.

-- PRIMARY KEY: The customer_id column is the primary key, ensuring each customer has a unique ID.

-- These two tables, "Authors" and "Customers," serve as containers for storing information about authors and customers, respectively. The other tables ("Books," "Orders," "Order_Items," and "Reviews") follow a similar structure to store different types of data in your database.
