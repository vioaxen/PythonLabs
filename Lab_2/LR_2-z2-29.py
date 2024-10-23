import random

random_number = random.randint(100, 999)

binary_form = bin(random_number)[2:]
hexadecimal_form = hex(random_number)[2:]

combined_string = binary_form + hexadecimal_form

print(f"Случайное трёхзначное число: {random_number}")
print(f"Двоичная форма: {binary_form}")
print(f"Шестнадцатеричная форма: {hexadecimal_form}")
print(f"Соединённая строка: {combined_string}")