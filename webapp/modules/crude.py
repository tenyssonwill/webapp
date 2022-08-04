import sqlite3
from modules.env import EnvVars

class ConnectDb:

    def __init__(self) -> None:
        self.env = EnvVars()
        self.conn = None

    def dbconnect(self):
        conn = sqlite3.connect(self.env.db)
        if conn:
            print('Conectado')
            self.conn = conn
        else:
            print('ERRR')

    def create(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def update(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def read(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        return res
        