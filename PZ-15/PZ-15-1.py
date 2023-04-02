import sqlite3 as sq
info_form = [
    (1, 'Александр', 'Петров', '1998-06-16', 'муж.', '2016-03-15', 'Бухгалтер', 'Бухгалтерия' , 25000),
    (2, 'Мария', 'Иванова', '1984-03-04', 'жен.', '2004-11-27', 'Медицинская сестра', 'Хирургия', 34000),
    (3, 'Иван', 'Смирнов', '1980-11-12', 'муж.', '2005-06-02', 'Врач', 'Терапия', 60000),
    (4, 'Ольга', 'Кузнецова', '1986-08-22', 'жен.', '2010-03-10', 'Медицинская сестра', 'Неврология', 31000),
    (5, 'Дмитрий', 'Егоров', '1975-05-07', 'муж.', '1999-11-22', 'Врач', 'Онкология', 75000),
    (6, 'Елена', 'Белова', '1989-01-31', 'жен.', '2018-08-17', 'Фармацевт', 'Аптека', 40000),
    (7, 'Алексей', 'Козлов', '1983-12-08', 'муж.', '2012-05-25', 'Врач', 'Кардиология', 67000),
    (8, 'Марина', 'Попова', '1990-02-14', 'жен.', '2016-11-14', 'Медицинская сестра', 'Педиатрия', 33000),
    (9, 'Сергей', 'Гусев', '1978-09-23', 'муж.', '2001-07-20', 'Врач', 'Хирургия', 78000),
    (10, 'Анна', 'Романова', '1995-04-17', 'жен.', '2019-09-11', 'Стоматолог', 'Стоматология', 55000),
    (11, 'Игорь', 'Иванов', '1987-07-02', 'муж.', '2015-01-17', 'Врач', 'Гастроэнтерология', 63000),
    (12, 'Екатерина', 'Соколова', '1982-03-29', 'жен.', '2006-12-05', 'Медицинская сестра', 'Онкология', 32000),
    (13, 'Александра', 'Морозова', '1991-08-18', 'жен.', '2018-05-16', 'Врач', 'Неврология', 59000),
    (14, 'Илья', 'Петров', '1977-12-11', 'муж.', '2002-09-22', 'Врач', 'Терапия', 72000),
    (15, 'Надежда', 'Васильева', '1993-11-03', 'жен.', '2019-06-18', 'Медицинская' 'сестра', 'Кардиология', 34000),
    (16, 'Константин', 'Гаврилов', '1981-06-06', 'муж.', '2009-02-09', 'Врач', 'Неврология', 66000),
    (17, 'Татьяна', 'Кузьмина', '1994-01-25', 'жен.', '2018-10-14', 'Медицинская сестра', 'Терапия', 35000),
    (18, 'Андрей', 'Лебедев', '1985-04-06', 'муж.', '2014-03-21', 'Врач', 'Онкология', 70000),
    (19, 'Юлия', 'Беляева', '1992-09-10', 'жен.', '2017-07-07', 'Фармацевт', 'Аптека', 42000),
    (20, 'Артем', 'Воробьев', '1989-07-28', 'муж.', '2016-04-23', 'Врач', 'Кардиология', 68000)
]
info_list = [

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
