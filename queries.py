import sqlite3

conn = sqlite3.connect("library.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
);

INSERT INTO books VALUES
(1, 'Data Science Basics', 'Technology', 1450, 12),
(2, 'Clean Code', 'Technology', 1200, 8),
(3, 'The Silent Patient', 'Fiction', 1350, 2),
(4, 'Atomic Habits', 'Self-Help', 900, 15),
(5, 'The Alchemist', 'Fiction', 700, 4),
(6, 'Python Crash Course', 'Technology', 950, 10),
(7, 'Gone Girl', 'Fiction', 800, 20),
(8, 'Sapiens', 'History', 1100, 6),
(9, 'The Kite Runner', 'Fiction', 650, 3);
""")
conn.commit()

print("Books above Rs.1000 (sorted):")
cur.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC;
""")
for row in cur.fetchall():
    print(row)

print("\nBooks with renamed column (AS):")
cur.execute("""
SELECT title AS book_title, price
FROM books;
""")
for row in cur.fetchall():
    print(row)

print("\nLow-stock Fiction books:")
cur.execute("""
SELECT title, genre, price, stock
FROM books
WHERE genre = 'Fiction' AND stock < 5;
""")
for row in cur.fetchall():
    print(row)

conn.close()