import sqlite3 as sql

boglanish1 = sql.connect("susy.db")
boglanish2 =  boglanish1.cursor()
boglanish2.execute(''' 
CREATE TABLE IF NOT EXISTS Mevas(
    turi TEXT
    rang TEXT
    narx INTEGER
)
''')