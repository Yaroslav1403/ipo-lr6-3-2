#Импортируем модуль random для генерации случайных размеров матрицы, cоздания матрицы с случайными элементами
import random

#Инициализируем переменные для генерации случайных размеров матрицы
height = random.randint(4, 8)
width = random.randint(4, 8)

#Создаём список с элементами будущей матрицы
numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]

#Создаём список с элементами, не кратными 3
not_three = []

#Инициализируем переменную суммы для хранения суммы чисел из списка not_three
total_sum = 0 

#Создаём матрицу с случайными элементами
matrica = [[random.choice(numbers) for j in range(width)] for i in range(height)]

#Внешним циклом проходимся по строкам матрицы
for i in range(height):
    #Внутренним циклом проходимся по элементам каждой строки 
    for j in range(width):
        #Выводим матрицу с разделением пробелами
        print(matrica[i][j], end = "  ")
    #Переходим на новую строку после каждой строки матрицы
    print() 

#Внешним циклом проходимся по строкам матрицы
for a in matrica:
    #Внутренним циклом проходимся по элементам каждой строки
    for b in a:
        #Если элемент b не кратен 3 
        if b % 3 != 0:  
            #Добавляем элемент b в список not_three
            not_three.append(b)

#Выводим на экран список not_three, который содержит все числа из матрицы, которые не кратны 3
print(f"Cписок чисел, не кратных трем: {not_three}")

#Создаём цикл, который перебирает все элементы в списке not_three и добавляет их к переменной v
for v in not_three:
    total_sum += v

#Выводим итоговую сумму чисел из списка not_three.
print("Сумма равна: ", total_sum)
