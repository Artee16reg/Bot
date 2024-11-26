import sqlite3 as sq

# Создаем подключение к базе данных (файл my_database.db будет создан)
db = sq.connect('my_database.db')
cursor = db.cursor()

db.close()