# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],[5, 5, 5, 4, 5]]
# students = {'Jonny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
from sys import modules

grades = {'Jonny': (5, 3, 3, 5, 4),
           'Bilbo': (2, 2, 2, 3),
           'Steve': (4, 5, 5, 2),
           'Khendrik': (4, 4, 3),
           'Aaron': (5, 5, 5, 4, 5)}
# Запись данных
student0 = (grades.get('Jonny'))
student1 = (grades.get('Bilbo'))
student2 = (grades.get('Steve'))
student3 = (grades.get('Khendrik'))
student4 = (grades.get('Aaron'))
# Сумма всех оценок
a = (sum(grades['Jonny']))
b = (sum(grades['Bilbo']))
c = (sum(grades['Steve']))
d = (sum(grades['Khendrik']))
f = (sum(grades['Aaron']))
# Кол-во оценок каждого студента
a1 = (len(student0))
b1 = (len(student1))
c1 = (len(student2))
d1 = (len(student3))
f1 = (len(student4))
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
