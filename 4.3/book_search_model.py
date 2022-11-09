import pandas as pd


def get_genre(conn):
    return pd.read_sql('''
    SELECT 
    genre_id AS id,
    COUNT(genre_id) AS Количество_экземпляров, 
    genre_name AS Название
    FROM genre
    JOIN book USING (genre_id)
    GROUP BY genre_id
    ORDER BY Название
    ''', conn)


def get_author(conn):
    return pd.read_sql('''
        SELECT 
        author_id AS id,
        COUNT(author_id) AS Количество_экземпляров, 
        author_name AS Название
        FROM author
        JOIN book_author USING (author_id)
        GROUP BY author_id
        ORDER BY Название
        ''', conn)


def get_publisher(conn):
    return pd.read_sql('''
        SELECT 
        publisher_id AS id,
        COUNT(publisher_id) AS Количество_экземпляров, 
        publisher_name AS Название
        FROM publisher
        JOIN book USING (publisher_id)
        GROUP BY publisher_id
        ORDER BY Название
        ''', conn)


def books_output(genre, author, publisher, conn):
    return pd.read_sql(f'''
        SELECT 
        title AS Название,
        GROUP_CONCAT(author_name) AS Авторы,
        genre_name AS Жанр, 
        publisher_name AS Издательство,
        year_publication AS Год_издания,
        available_numbers AS Количество
        FROM book
        JOIN publisher USING (publisher_id)
        JOIN book_author USING (book_id)
        JOIN author USING (author_id)
        JOIN genre USING (genre_id)
        WHERE genre_id in {genre}
            AND author_id in {author}
            AND publisher_id in {publisher}
        GROUP BY book_id
        ORDER BY Название
        ''', conn)


def get_genre_id(conn):
    return pd.read_sql('''
        SELECT genre_id
        FROM genre
        ''', conn)


def get_author_id(conn):
    return pd.read_sql('''
        SELECT author_id
        FROM author
        ''', conn)


def get_publisher_id(conn):
    return pd.read_sql('''
        SELECT publisher_id
        FROM publisher
        ''', conn)

