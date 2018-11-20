from mynote.api import db


sql = ['''drop table if exists nb_notes''',
       '''create table nb_notes(id integer primary key autoincrement, title text, content text)'''
       ]

for s in sql:
    db.getCursor().execute(s)

print('table create end')