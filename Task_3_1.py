box = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
       "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
def num_translate(number):
    return box.get(number)
print(num_translate(input("Number translate: ")))



