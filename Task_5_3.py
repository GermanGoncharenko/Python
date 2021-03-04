from itertools import islice, zip_longest
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']
result = (i for i in zip_longest(tutors, klasses))
print(*islice(result, 7))      # Результат
print(type(result))             # Тип класса
print(list(islice(result, 9)))  # Работа до истощения
