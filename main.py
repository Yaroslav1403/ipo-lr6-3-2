import random

#Генерация случайных размеров матрицы
height = random.randint(4, 8)
width = random.randint(4, 8)

#Создаём список с элементами будущей матрицы
numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2]

#Создаём список с элементами, не кратными 3
not_three = []

#Переменная суммы
total_sum = 0 

#Создание матрицы с случайными элементами
matrica = [[random.choice(numbers) for j in range(width)] for i in range(height)]

#Выводим матрицу
for i in range(height):
    for j in range(width):
        print(matrica[i][j], end="  ")
    #Переход на новую строку после каждой строки матрицы
    print() 

#Создаём цикл для перебора строк матрицы, а затем каждого отдельного элемента этой матрицы
for a in matrica:
    for b in a:
        #Проверяем, не кратно ли число 3
        if b % 3 != 0:  
            not_three.append(b)

print(f"Cписок чисел, не кратных трем: {not_three}")

#Создаём цикл, который будет перебирать элементы матрицы для нахождения суммы 
for v in not_three:
    total_sum += v

print("Сумма равна: ", total_sum)
