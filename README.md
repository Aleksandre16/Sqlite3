                                                                                                          SQL Lite HomeWork TBC

# Book Database Manager

This Python script interacts with a SQLite database to manage a collection of books. It performs the following tasks:

1. Creates a SQLite database and a table named 'Book' to store book entries.
2. Generates 10 random book entries with random values for name, number of pages, cover type, and category.
3. Inserts the generated book entries into the database.
4. Calculates and prints the average number of pages of all books.
5. Retrieves and prints the name of the book with the largest number of pages.

## Prerequisites

- Python 3.x
- SQLite3 module (included in Python standard library)

## How to Use

1. Clone or download the repository to your local machine.
2. Make sure you have Python installed.
3. Run the script using the command:

   
This Python script does the following:

Connects to a SQLite database named 'books.db'.
Creates a table named 'Book' with columns for name, number of pages, cover type, and category.
Generates 10 random book entries with random values for each column.
Inserts these generated books into the database.
Calculates and prints the average number of pages of all books.
Retrieves and prints the name of the book with the largest number of pages.
Closes the database connection.
