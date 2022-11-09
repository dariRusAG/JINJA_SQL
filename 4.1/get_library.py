# Контроллер (управляющая программа) – в ней будет реализовываться логика
# программы, выполняться обращение к базе данных и генерироваться шаблон

# В программе-контроллере осуществляется:
# - соединение с базой данных;
# - выбор информации из базы данных;
# - генерация шаблона;
# - вывод результата в файл.

# импортируем необходимые модули
from jinja2 import Template
import sqlite3
import library_model

# устанавливаем соединение с базой данных (база данных из ЛР 1)
conn = sqlite3.connect("../library.sqlite")

# # открываем файл с дампом базой данных
# f_damp = open('library.db', 'r', encoding='utf-8-sig')
# # читаем данные из файла
# damp = f_damp.read()
# # закрываем файл с дампом
# f_damp.close()
#
# # запускаем запросы
# conn.executescript(damp)
# # сохраняем информацию в базе данных
# conn.commit()

# выбираем записи из таблицы publisher
df_publisher = library_model.get_publisher(conn)
# выбираем записи из таблицы genre
df_genre = library_model.get_genre(conn)
# выбираем записи из таблицы reader
df_reader = library_model.get_reader(conn)
# выбираем записи из таблицы author
df_author = library_model.get_author(conn)
# выбираем записи из таблицы book_author
df_book_author = library_model.get_book_author(conn)
# выбираем записи из таблицы book
df_book = library_model.get_book(conn)
# выбираем записи из таблицы book_reader
df_book_reader = library_model.get_book_reader(conn)

# закрываем соединение с базой
conn.close()

# добавляем все таблицы в массив
df_list = [df_publisher, df_genre, df_reader, df_author, df_book_author, df_book, df_book_reader]
df_name_list = ["publisher", "genre", "reader", "author", "book_author", "book", "book_reader"]

# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open('library_temp.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)

# генерируем результат на основе шаблона
result_html = template.render(list_table=df_name_list,
                              list_relation=df_list,
                              len=len,
                              zip=zip)

# создаем файл для HTML-страницы
f = open('library.html', 'w', encoding='utf-8-sig')
# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
