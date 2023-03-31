import sqlite3 as sq
info_from = [

]
with sq.connect('salary.db') as con:
    con.execute('PRAGMA foreign_keys = ON')
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS form(
        id INTEGER PRIMARY KEY,
        first_name VARCHAR NOT NULL, 
        last_name VARCHAR NOT NULL, 
        birth_date DATE NOT NULL,
        sex VARCHAR NOT NULL,
        hire_date DATE NOT NULL,
        post VARCHAR NOT NULL,
        department VARCHAR NOT NULL,
        base_rate DECIMAL NOT NULL,
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS list(
        id INTEGER PRIMARY KEY,
        id_p INTEGER PRIMARY KEY,
        starting_date DATE NOT NULL,
        ending_date DATE NOT NULL,
        reason VARCHAR NOT NULL,
        diagnosis VARCHAR NOT NULL,
        paid BOOLEAN NOT NULL,
        FOREIGN KEY (id_p) REFERENCES from(id) ON DELETE CASCADE ON UPDATE CASCADE
    )""")

with sq.connect('salary.db') as con:
    cur = con.cursor()
    cur.executemany('INSERT INTO form VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', info_form)
    cur.executemany('INSERT INTO form VALUES(?, ?, ?, ?, ?, ?, ?)', info_list)

with sq.connect('salary.db') as con:
    cur = con.cursor()
    cur.execute('SELECT first_name, last_name, post FROM from')
    cur.execute('SELECT first_name, last_name, base_rate FROM from')
    cur.execute('SELECT first_name, last_name FROM from WHERE department='IT'')
    cur.execute('SELECT first_name, last_name FROM from WHERE hire_date>'01.01.2022'')
    cur.execute('SELECT * FROM list WHERE id_p=42')
    cur.execute('SELECT * FROM list WHERE paid = TRUE')
    cur.execute('SELECT * FROM list WHERE MONTH(starting_date)=MONTH(NOW())')
