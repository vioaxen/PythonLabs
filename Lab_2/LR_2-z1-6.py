num1 = 4.89304 - 8.1276j
num2 = 0.09378 - 1.38576j

abs_num1 = abs(num1)
abs_num2 = abs(num2)

conj_num1 = num1.conjugate()
conj_num2 = num2.conjugate()

sqrt_num1 = num1 ** 2
sqrt_num2 = num2 ** 2

is_equal = sqrt_num1 == sqrt_num2

print(f"Модуль числа {num1}: {abs_num1:}")
print(f"Модуль числа {num2}: {abs_num2:}")
print(f"Сопряженное число для {num1}: {conj_num1}")
print(f"Сопряженное число для {num2}: {conj_num2}")
print(f"Квадрат числа {num1}: {sqrt_num1}")
print(f"Квадрат числа {num2}: {sqrt_num2}")
print(f"Результаты квадратов чисел равны: {is_equal}")
