# -*- coding: utf-8 -*-


import sqlite3

conn = sqlite3.connect("test.db")

cursor = conn.cursor()

try:
    cursor.execute('create table user (id varchar(20) primary key AUTOINCREMENT, name varchar(20))')
except sqlite3.OperationalError:
    print("表已经存在")

cursor.execute('insert into user (id, name) values (?, ?) where not exists in (select name from user)', ("1", "onedi"))

print(cursor.rowcount)

cursor.close()
conn.commit()
conn.close()
