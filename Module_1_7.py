student = {'Jonny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],[5, 5, 5, 4, 5]]
sorted_student = sorted(student)
# Сумма оценок
a = (sum(grades[0]))
b = (sum(grades[1]))
c = (sum(grades[2]))
d = (sum(grades[3]))
f = (sum(grades[4]))
# Кол-во оценок каждого студента
a1 = (len(grades[0]))
b1 = (len(grades[1]))
c1 = (len(grades[2]))
d1 = (len(grades[3]))
f1 = (len(grades[4]))
# Средний балл каждого студента
a2 = a/a1
b2 = b/b1
c2 = c/c1
d2 = d/d1
f2 = f/f1
print ( sorted_student[0],':', (a2))
print ( sorted_student[1],':', (b2))
print ( sorted_student[2],':', (c2))
print ( sorted_student[3],':', (d2))
print ( sorted_student[4],':', (f2))
