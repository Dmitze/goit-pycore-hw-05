import re
from typing import Callable

def generator_numbers(text: str):
    # Шукаємо дійсні числа, що відокремлені пробілами
    pattern = r"\s+(\d+\.\d+)\s+"
    
    for match in re.finditer(pattern, " " + text + " "):
        yield float(match.group(1))

def sum_profit(text: str, func: Callable):
    total = 0.0
    # Використовуємо генератор для підсумовування чисел
    for number in func(text):
        total += number
    return total

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

# Ще один тест
text2 = "Тут немає чисел, а тут є 10.5 та ще 0.5."
print(f"Сума для другого тексту: {sum_profit(text2, generator_numbers)}")