import sqlite3
import logging
conn = sqlite3.connect('my_first_db.db')

def create_table():
    """
    Create table
    """

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER
        )
    """)
    conn.commit()


def insert_book(title, author, year):
    """
    Insert a new book
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO books(title, author, year)
            VALUES(?,?,?)
        """, (title, author, year))
        conn.commit()
    except Exception as e:
        logging.error(e)
        return False

    return True

def delete_book(title):
    """
    Delete a book
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM books WHERE title=?
        """, (title,))
        conn.commit()
    except Exception as e:
        logging.error(e)
        return False

    return True

def get_book(title):
    """
    Get a book
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM books WHERE title=?
        """, (title,))
        book = cursor.fetchone()
    except:
        return None

    return book

def update_book(old_title,title, author, year):
    """
    Update a book
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE books
            SET title=?, author=?, year=?
            WHERE title=?
        """, (title, author, year, old_title))
        conn.commit()
    except Exception as e:
        logging.error(e)
        return False

    return True


def get_all_books():
    """
    Get all books
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM books
        """)
        books = cursor.fetchall()
    except:
        return None

    return books