import sqlite3 as sq

# Создаем подключение к базе данных (файл my_database.db будет создан)
db = sq.connect("my_database.db")
cursor = db.cursor()
# TODO  Содать базу данных ДОХОД, РАХОД.
#  Доход (id, id_group, amount, avto_date,)
#  РАсход (id, id_Group, amount, avto_date,)
#  Group (id, name_group) M2M
#  Statistic (Доход\мес, Расход\мес, ср_доход, ср_расход, Группа_сум\мес . . .)

db.close()
