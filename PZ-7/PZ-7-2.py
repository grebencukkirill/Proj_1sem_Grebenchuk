s =  input('Введите что-нибудь: ')
a = 96
b = 0
for i in range(len(s)):
  try:
    int(s[i])
    continue
  except:
    if (ord(s[i])-1 == a):
      a = ord(s[i])
      b += 1
    else:
      print(f'Алфавитный порядок нарушается на {i+1} элементе списка')
      break
  if b == 0:
    print(0)
