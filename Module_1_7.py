# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],[5, 5, 5, 4, 5]]
# students = {'Jonny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
from sys import modules

module1 = {'Jonny': (5, 3, 3, 5, 4),
           'Bilbo': (2, 2, 2, 3),
           'Steve': (4, 5, 5, 2),
           'Khendrik': (4, 4, 3),
           'Aaron': (5, 5, 5, 4, 5)}
# Запись данных
a0 = (module1.get('Jonny'))
b0 = (module1.get('Bilbo'))
c0 = (module1.get('Steve'))
d0 = (module1.get('Khendrik'))
f0 = (module1.get('Aaron'))
# Сумма всех оценок
a = (sum(module1['Jonny']))
b = (sum(module1['Bilbo']))
c = (sum(module1['Steve']))
d = (sum(module1['Khendrik']))
f = (sum(module1['Aaron']))
# Кол-во оценок каждого студента
a1 = (len(a0))
b1 = (len(b0))
c1 = (len(c0))
d1 = (len(d0))
f1 = (len(f0))
# Средний балл каждого студента
a2 = a/a1
b2 = b/b1
c2 = c/c1
d2 = d/d1
f2 = f/f1
print ( 'Jonny: ', (a2))
print ( 'Bilbo: ', (b2))
print ( 'Steve: ', (c2))
print ( 'Khendrik', (d2))
print ( 'Aaron: ', (f2))
