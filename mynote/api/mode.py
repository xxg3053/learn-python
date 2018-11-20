from mynote.api import db


def list_notes():
    sql = '''select id, title, content from nb_notes'''
    rs = db.getCursor().execute(sql)
    return rs.fetchall()

def add_note(title, content):
    sql = '''insert into nb_notes(title, content) values (:st_title, :st_content)'''
    db.getCursor().execute(sql, {'st_title':title, 'st_content': content})
    db.getConn().commit()

def update_note(id, title, content):
    sql = '''update nb_notes set title=:st_title, content=:st_content where id=:st_id'''
    db.getCursor().execute(sql, {'st_id':id, 'st_title':title, 'st_content': content})
    db.getConn().commit()

def delete_note(id):
    sql = '''delete from nb_notes where id=:st_id'''
    db.getCursor().execute(sql, {'st_id':id})
    db.getConn().commit()

def get_note(id):
    sql = '''select id, title, content from nb_notes where id=:st_id'''
    rs = db.getCursor().execute(sql, {'st_id':id})
    return rs.fetchone()

