# Книжные магазины предлагают следующие коллекции книг.
# Магистр - Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги - Толстой, Грибоедов, Чехов, Пушкин
# БукМаркет - Пушкин, Достоевский, Маяковский
# Галерея - Чехов, Тютчев, Пушкин. Определить:
# 1. Полный список всех книг магазинов.
# 2. Какие книги есть во всех магазинах.
# 3. Хотя бы одну книгу, которая есть не во всех магазинах.

books = {
    'Магистр': ['Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'],
    'ДомКниги': ['Толстой', 'Грибоедов', 'Чехов', 'Пушкин'],
    'БукМаркет': ['Пушкин', 'Достоевский', ''],
    'Галерея': ['Чехов', 'Тютчев', 'Пушкин']
}

books_1 = set(books['Магистр'])
books_2 = set(books['ДомКниги'])
books_3 = set(books['БукМаркет'])
books_4 = set(books['Галерея'])

all = books_1 | books_2 | books_3 | books_4

print('Все книги:', *all)
print('Есть во всех магазинах:',*(books_1 & books_2 & books_3 & books_4))
print('Есть не во всех магазинах:',*(all-(books_1 & books_2 & books_3 & books_4)))