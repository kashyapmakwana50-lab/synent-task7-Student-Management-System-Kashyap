# Student Management System – Project Report

## 1. Objective

The objective of this project is to develop a simple command-line Student Management System that allows users to add, view, update, and delete student records.

## 2. Methodology

The program stores student information in a `students.json` file, allowing records to remain available after the program is closed.

Each student record contains:

* Student ID
* Name
* Age
* Course

The system provides five menu options: Add Student, View Students, Update Student, Delete Student, and Exit.

## 3. Implementation

The program uses Python's `json` module for storing and retrieving student records and the `os` module to check whether the JSON file exists.

Separate functions are used for each major operation. The program also checks for duplicate Student IDs before adding a new record. During updates, users can leave a field blank to keep its existing value.

## 4. Testing and Results

The system was tested by adding multiple student records, viewing the stored records, updating student information, and deleting records.

Duplicate Student IDs and non-existent Student IDs were also tested. The program correctly displayed appropriate messages for these cases.

## 5. Conclusion

The Student Management System successfully provides basic student record management with persistent JSON-based storage. The project demonstrates the use of Python functions, file handling, JSON data management, loops, conditional statements, and user input.
