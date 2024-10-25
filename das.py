my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print("Дан список:", my_list)

while True:
    number = int(input("Введите положительное число из списка: "))
    if number == 0:
        print("Число не является положительным.")
        break
    elif number < 0 and number in my_list:
        print("Число отрицательное.")
        break
    elif number in my_list:
        print(number)
        continue
    elif number not in my_list:
        print("Число не является элементом списка.")
        break
