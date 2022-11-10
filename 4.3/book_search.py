from jinja2 import Template
import sqlite3
import book_search_model


def check_choice(genre, author, publisher):
    if type(genre) == int:
        genre = (genre, 0)

    if type(author) == int:
        author = (author, 0)

    if type(publisher) == int:
        publisher = (publisher, 0)

    if genre is None:
        genre = tuple(book_search_model.get_genre_id(conn)["genre_id"])

    if author is None:
        author = tuple(book_search_model.get_author_id(conn)["author_id"])

    if publisher is None:
        publisher = tuple(book_search_model.get_publisher_id(conn)["publisher_id"])

    # if 9 in author and 8 not in author:
    #     author += (8, )
    # elif 8 in author and 9 not in author:
    #     author += (9, )
    #
    # if 4 in author and 5 not in author:
    #     author += (5, )
    # elif 5 in author and 4 not in author:
    #     author += (4, )

    return genre, author, publisher


def check_view(genre, author, publisher):
    if type(genre) == int:
        genre = (genre, 0)

    if type(author) == int:
        author = (author, 0)

    if type(publisher) == int:
        publisher = (publisher, 0)

    if genre is None:
        genre = (0, 0)

    if author is None:
        author = (0, 0)

    if publisher is None:
        publisher = (0, 0)

    return genre, author, publisher


conn = sqlite3.connect("../library.sqlite")

# выбираем записи из таблицы genre
df_genre = book_search_model.get_genre(conn)
# выбираем записи из таблицы author
df_author = book_search_model.get_author(conn)
# выбираем записи из таблицы publisher
df_publisher = book_search_model.get_publisher(conn)

list_df = [df_genre, df_author, df_publisher]
list_name_df = ["Жанр", "Автор", "Издательство"]

genre_choice = (1, 2, 3)
author_choice = (2, 3, 4)
publisher_choice = None

genre_view, author_view, publisher_view = check_view(genre_choice, author_choice, publisher_choice)

list_view = [genre_view, author_view, publisher_view]

genre_choice, author_choice, publisher_choice = check_choice(genre_choice, author_choice, publisher_choice)

list_choice = [genre_choice, author_choice, publisher_choice]

books_list = book_search_model.books_output(genre_choice, author_choice, publisher_choice, conn)

conn.close()

f_template = open('book_search_temp.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

template = Template(html)
result_html = template.render(
    name_box=list_name_df,
    combo_box=list_df,
    list_choice=list_choice,
    list_view=list_view,
    books=books_list,
    len=len,
    zip=zip)

# создаем файл для HTML-страницы
f = open('book_search.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
