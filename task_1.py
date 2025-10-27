def caching_fibonacci():
    # Створюємо словник для кешування
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        # Рекурсивний виклик з кешуванням результату
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(f"Fibonacci(10): {fib(10)}")  # Виведе 55
print(f"Fibonacci(15): {fib(15)}")  # Виведе 610

# Перевірка, чи кеш працює для вже обчисленого значення
print(f"Fibonacci(10): {fib(10)}")