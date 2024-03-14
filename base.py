import sqlite3
import random
import string

# Connect to SQLite database
conn = sqlite3.connect('books.db') #Name Of DB
cursor = conn.cursor()

# Book table
cursor.execute('''CREATE TABLE IF NOT EXISTS Book (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    num_pages INTEGER,
                    cover_type TEXT,
                    category TEXT
                )''')

# Random book record
def generate_random_book():
    name = ''.join(random.choices(string.ascii_uppercase, k=5))
    num_pages = random.randint(50, 500)
    cover_type = random.choice(['Hardcover', 'Paperback', 'E-book'])
    category = random.choice(['Fiction', 'Non-fiction', 'Science Fiction', 'Mystery', 'Thriller'])
    return (name, num_pages, cover_type, category)

# Generate 10 random book entries
books = [generate_random_book() for _ in range(10)]
cursor.executemany('''INSERT INTO Book (name, num_pages, cover_type, category) 
                    VALUES (?, ?, ?, ?)''', books)

#commint connect!
conn.commit()

cursor.execute('''SELECT AVG(num_pages) FROM Book''')
avg_pages = cursor.fetchone()[0]
print("Average number of pages:", avg_pages)

# Print Largest Book name
cursor.execute('''SELECT name FROM Book ORDER BY num_pages DESC LIMIT 1''')
largest_book_name = cursor.fetchone()[0]
print("Name of the largest book:", largest_book_name)

# Close the connection
conn.close()
