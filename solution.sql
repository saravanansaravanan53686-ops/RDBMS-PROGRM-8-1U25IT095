CREATE DATABASE officeDB;
USE officeDB;
CREATE TABLE Employee(
  EmployeeID VARCHAR(30)PRIMARY KEY,
  EmployeeName VARCHAR(30),
  Department VARCHAR(20),
  Salary DECIMAL(10,2)
);
INSERT INTO Employee
VALUES
(101,'Ravi','HR',25000),
(102,'Meena','IT',40000),
(103,'Kumar','Finance',35000),
(104,'Suresh','IT',45000),
(105,'Latha','HR',30000);

SELECT COUNT(Salary)As Total Employees
FROM  Employee;

SELECT MAX(Salary)As Highest Salary
FROM Employee;

SELECT MIN(Salary)As Lowest Salary
FROM Employee;

SELECT AVG(Salary)As Average Salary
FROM Employee;
  
  
