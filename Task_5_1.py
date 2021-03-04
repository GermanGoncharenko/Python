def odd_nums(max):
    for num in range(1, max + 1, 2):
        yield num
odd_to_x = odd_nums(23)
# print(*odd_to_x) # Можно вывести в одну строку с пробелом
# print(*odd_to_x, sep='') # вывести в одну строку слитно
# print(next(odd_to_x), next(odd_to_x)) # последовательно нужное количество(в строку)
print(next(odd_to_x)) # по очереди(в столбик) друг за другом прописывая print
print(next(odd_to_x))
print(next(odd_to_x))
print(next(odd_to_x))
