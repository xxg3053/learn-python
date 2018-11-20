import os

from mynote.api import server

root_path = os.path.dirname(os.getcwd() + '/mynote')
db_path = root_path + '/api/mynote.db'
app = server.create_app(root_path=root_path, db_path=db_path)

if __name__ == '__main__':
    app.run()