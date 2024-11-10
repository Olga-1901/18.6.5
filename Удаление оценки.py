import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
        print(f'''{student}
        {students_marks[student]}''')

        print('''
            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
             ''')

while True:
            command = int(input('Введите команду: '))
            if command == 1:
                print('1. Добавить оценку ученика по предмету')
                student = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                mark = int(input('Введите оценку: '))
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    students_marks[student][class_].append(mark)
                    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                else:
                 print('ОШИБКА: неверное имя ученика или название предмета')

            elif command == 2:
                print('2. Вывести средний балл по всем предметам по каждому ученику')
                for student in students:
                    print(student)
                    for class_ in classes:
                        marks_sum = sum(students_marks[student][class_])
                        marks_count = len(students_marks[student][class_])
                        print(f'{class_} - {marks_sum // marks_count}')
                    print()

            elif command == 3:
                print('3. Вывести все оценки по всем ученикам')
                for student in students:
                    print(student)
                    for class_ in classes:
                        print(f'\t{class_} - {students_marks[student][class_]}')
                    print()

            elif command == 4:
                print('4. Удалить оценку:')
                name = input('Введите имя ученика: ')
                class_ = input('Введите предмет: ')
                print(f'''{name}
                    Оценки по: {class_} {students_marks[student][class_]}''')
                mark = int(input('Введите оценку которую нужно удалить:'))
                if name in students_marks.keys() and class_ in students_marks[student].keys():
                    if mark in students_marks[student][class_]:
                     students_marks[student][class_].remove(mark)
                    print('Оценка удалена')
                    print(f'''{name}
                    {students_marks[student]}''')
                else:
                   print('Оценки в списке нет')



Александра
        {'Математика': [1, 3, 1], 'Русский язык': [3, 1, 4], 'Информатика': [1, 3, 4]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
             
Ангелина
        {'Математика': [5, 2, 5], 'Русский язык': [3, 3, 1], 'Информатика': [3, 1, 3]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
             
Аполлон
        {'Математика': [1, 5, 4], 'Русский язык': [2, 5, 1], 'Информатика': [5, 2, 1]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
             
Дарья
        {'Математика': [1, 3, 3], 'Русский язык': [2, 1, 1], 'Информатика': [5, 3, 2]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
             
Ярослав
        {'Математика': [2, 3, 1], 'Русский язык': [3, 2, 3], 'Информатика': [2, 3, 2]}

            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценку
             
Введите команду: 4
4. Удалить оценку:
Введите имя ученика: Дарья
Введите предмет: Математика
Дарья
                    Оценки по: Математика [2, 3, 1]
Введите оценку которую нужно удалить:1
Оценка удалена
Дарья
                    {'Математика': [2, 3], 'Русский язык': [3, 2, 3], 'Информатика': [2, 3, 2]}

