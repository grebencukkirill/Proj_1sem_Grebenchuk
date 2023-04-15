# Вариант 3
import sqlite3 as sq
info_form = [
    (1, 'Александр', 'Петров', '1998-06-16', 'муж.', '2016-03-15', 'Бухгалтер', 'Бухгалтерия' , 25000),
    (2, 'Мария', 'Иванова', '1984-03-04', 'жен.', '2004-11-27', 'Медицинская сестра', 'Хирургия', 34000),
    (3, 'Иван', 'Смирнов', '1980-11-12', 'муж.', '2005-06-02', 'Врач', 'Терапия', 60000),
    (4, 'Ольга', 'Кузнецова', '1986-08-22', 'жен.', '2010-03-10', 'Медицинская сестра', 'Неврология', 31000),
    (5, 'Дмитрий', 'Егоров', '1975-05-07', 'муж.', '1999-11-22', 'Врач', 'Онкология', 110000),
    (6, 'Елена', 'Белова', '1989-01-31', 'жен.', '2018-08-17', 'Фармацевт', 'Аптека', 40000),
    (7, 'Алексей', 'Козлов', '1983-12-08', 'муж.', '2012-05-25', 'Врач', 'Кардиология', 67000),
    (8, 'Марина', 'Попова', '1990-02-14', 'жен.', '2016-11-14', 'Системный администратор', 'IT', 33000),
    (9, 'Сергей', 'Гусев', '1978-09-23', 'муж.', '2001-07-20', 'Врач', 'Хирургия', 78000),
    (10, 'Анна', 'Романова', '1995-04-17', 'жен.', '2019-09-11', 'Стоматолог', 'Стоматология', 55000),
    (11, 'Игорь', 'Иванов', '1987-07-02', 'муж.', '2015-01-17', 'Программист', 'IT', 63000),
    (12, 'Екатерина', 'Соколова', '1982-03-29', 'жен.', '2006-12-05', 'Медицинская сестра', 'Онкология', 32000),
    (13, 'Александра', 'Морозова', '1991-08-18', 'жен.', '2018-05-16', 'Врач', 'Неврология', 59000),
    (14, 'Илья', 'Петров', '1977-12-11', 'муж.', '2002-09-22', 'Врач', 'Терапия', 72000),
    (15, 'Надежда', 'Васильева', '1993-11-03', 'жен.', '2019-06-18', 'Медицинская' 'сестра', 'Кардиология', 34000),
    (16, 'Константин', 'Гаврилов', '1981-06-06', 'муж.', '2009-02-09', 'Врач', 'Неврология', 66000),
    (17, 'Татьяна', 'Кузьмина', '1994-01-25', 'жен.', '2018-10-14', 'Медицинская сестра', 'Терапия', 35000),
    (18, 'Андрей', 'Лебедев', '1985-04-06', 'муж.', '2014-03-21', 'Врач', 'Онкология', 70000),
    (19, 'Юлия', 'Беляева', '1992-09-10', 'жен.', '2017-07-07', 'CIO', 'IT', 120000),
    (20, 'Артем', 'Воробьев', '1989-07-28', 'муж.', '2016-04-23', 'Врач', 'Кардиология', 68000)
]
info_list = [
    ('1', '3', '2022-05-10', '2022-05-15', 'Острый бронхит', 'J20.9', '0'),
    ('2', '12', '2022-08-02', '2022-08-09', 'Грипп', 'J11.1', '1'),
    ('3', '6', '2023-04-02', '2023-04-06', 'Пневмония', 'J18.9', '0'),
    ('4', '5', '2022-06-08', '2022-06-16', 'Ангина', 'J02.9', '1'),
    ('5', '17', '2022-12-24', '2022-12-28', 'Грипп', 'J11.1', '1'),
    ('6', '2', '2022-10-15', '2022-10-22', 'Острый бронхит', 'J20.9', '0'),
    ('7', '9', '2023-04-05', '2023-04-07', 'Грипп', 'J11.1', '0'),
    ('8', '14', '2023-03-24', '2023-03-30', 'Ангина', 'J02.9', '0'),
    ('9', '8', '2022-11-08', '2022-11-15', 'Острый бронхит', 'J20.9', '1'),
    ('10', '20', '2022-06-03', '2022-06-05', 'Ангина', 'J02.9', '1')
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
        base_rate DECIMAL NOT NULL
    )""")
    cur.execute("""CREATE TABLE IF NOT EXISTS list(
        id INTEGER PRIMARY KEY,
        id_p INTEGER,
        starting_date DATE NOT NULL,
        ending_date DATE NOT NULL,
        reason VARCHAR NOT NULL,
        diagnosis VARCHAR NOT NULL,
        paid BOOLEAN NOT NULL,
        FOREIGN KEY (id_p) REFERENCES form(id) ON DELETE CASCADE ON UPDATE CASCADE
    )""")

# with sq.connect('salary.db') as con:
#     cur = con.cursor()
#     cur.executemany('INSERT INTO form VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)', info_form)
#     cur.executemany('INSERT INTO list VALUES(?, ?, ?, ?, ?, ?, ?)', info_list)

con = sq.connect('salary.db')
cur = con.cursor()
cur.executescript("""SELECT first_name, last_name, post FROM form;
SELECT first_name, last_name, base_rate FROM form;
SELECT first_name, last_name FROM form WHERE department='IT';
SELECT first_name, last_name FROM form WHERE hire_date>'01.01.2022';
SELECT * FROM list WHERE id_p=2;
SELECT * FROM list WHERE paid = 1;
SELECT * FROM list WHERE STRFTIME('%Y-%m',starting_date)=STRFTIME('%Y-%m','now');
SELECT AVG(base_rate) AS base_rate_avg FROM form;
SELECT first_name, last_name FROM form WHERE base_rate>100000;
SELECT SUM(julianday(list.ending_date) - julianday(list.starting_date)) FROM list;
SELECT list.*, form.* FROM list INNER JOIN form ON (list.id_p=form.id);
SELECT list.*, form.* FROM list INNER JOIN form ON (list.id_p=form.id) WHERE STRFTIME('%Y-%m', list.starting_date) = STRFTIME('%Y-%m', 'now');
""")
# Вывести список всех сотрудников и их должностей
cur.execute("SELECT first_name, last_name, post FROM form")
result = cur.fetchall()
print(result)
# Вывести список всех сотрудников и их базовых ставок
cur.execute("SELECT first_name, last_name, base_rate FROM form")
result = cur.fetchall()
print(result)
# Вывести список всех сотрудников, работающих в отделе "IT"
cur.execute("SELECT first_name, last_name FROM form WHERE department='IT'")
result = cur.fetchall()
print(result)
# Вывести список всех сотрудников, принятых на работу после 1 января 2022 года
cur.execute("SELECT first_name, last_name FROM form WHERE hire_date>'01.01.2022'")
result = cur.fetchall()
print(result)
# Вывести список всех больничных листов, выписанных сотруднику с id = 42
cur.execute("SELECT * FROM list WHERE id_p=2")
result = cur.fetchall()
print(result)
# Вывести список всех больничных листов, оплаченных компанией
cur.execute("SELECT * FROM list WHERE paid = 1")
result = cur.fetchall()
print(result)
# Вывести список всех сотрудников, имеющих больничные листы на текущий месяц
cur.execute("SELECT * FROM list WHERE STRFTIME('%Y-%m',starting_date)=STRFTIME('%Y-%m','now')")
result = cur.fetchall()
print(result)
# Вывести среднюю базовую ставку всех сотрудников
cur.execute("SELECT AVG(base_rate) AS base_rate_avg FROM form")
result = cur.fetchall()
print(result)
# Вывести список всех сотрудников, имеющих базовую ставку выше 100 000
cur.execute("SELECT first_name, last_name FROM form WHERE base_rate>100000")
result = cur.fetchall()
print(result)
# Вывести список всех сотрудников и общее количество дней, проведенных ими на больничном
cur.execute("SELECT SUM(julianday(list.ending_date) - julianday(list.starting_date)) FROM list")
result = cur.fetchall()
print(result)
# Вывести информацию о сотрудниках и их больничных листах за последний месяц
cur.execute("SELECT list.*, form.* FROM list INNER JOIN form ON (list.id_p=form.id) WHERE STRFTIME('%Y-%m', list.starting_date) = STRFTIME('%Y-%m', 'now')")
result = cur.fetchall()
print(result)
# Вывести среднюю продолжительность больничных листов сотрудников в каждом отделе
cur.execute("SELECT form.department, SUM(julianday(list.ending_date) - julianday(list.starting_date)) FROM list INNER JOIN form ON (list.id_p=form.id) GROUP BY form.department")
result = cur.fetchall()
print(result)
# Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли
cur.execute("SELECT form.first_name, form.last_name, MAX(STRFTIME('%Y-%m-%d', list.starting_date)) FROM list INNER JOIN form ON (list.id_p=form.id) GROUP BY form.id")
result = cur.fetchall()
print(result)
# Вывести список сотрудников и информацию о первом больничном листе, который они оформляли
cur.execute("SELECT form.first_name, form.last_name, MIN(STRFTIME('%Y-%m-%d', list.starting_date)) FROM list INNER JOIN form ON (list.id_p=form.id) GROUP BY form.id")
result = cur.fetchall()
print(result)
# Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году
cur.execute("SELECT form.first_name, form.last_name, SUM(julianday(list.ending_date) - julianday(list.starting_date)) FROM list INNER JOIN form ON (list.id_p=form.id) GROUP BY form.id")
result = cur.fetchall()
print(result)

# UPDATE

# Обновить базовую ставку сотрудника на определенной должности

# Обновить отдел для всех сотрудников в определенном диапазоне возраста

# Обновить дату найма для сотрудника, получившего повышение

# Обновить причину больничного листа для сотрудника

# Обновить базовую ставку сотрудника в таблице "Анкета" на определенный




cur.close()
con.close()

