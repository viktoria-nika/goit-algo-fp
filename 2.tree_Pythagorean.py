
# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

# Необхідно написати програму на Python, яка використовує рекурсію 
# для створення фрактала “дерево Піфагора”.
#  Програма має візуалізувати фрактал “дерево Піфагора”,
#  і користувач повинен мати можливість вказати рівень рекурсії.

# Розв'язок:

import turtle

def draw_branch(length, level):
    if level == 0:
        return
    else:
        turtle.forward(length)  # Малюємо гілку
        turtle.right(30)         # Поворот вправо
        draw_branch(length * 0.7, level - 1)  # Рекурсивний виклик для правої гілки
        turtle.left(60)          # Поворот вліво
        draw_branch(length * 0.7, level - 1)  # Рекурсивний виклик для лівої гілки
        turtle.right(30)         # Повертаємося назад
        turtle.backward(length)  # Повертаємося на початкову позицію

def draw_pythagorean_tree(level):
    turtle.speed(0)          # Найшвидший режим малювання
    turtle.left(90)          # Повертаємо черепашку вгору
    turtle.penup()
    turtle.backward(100)     # Зрушуємо вгору для кращого вигляду
    turtle.pendown()
    turtle.forward(100)      # Повертаємося вниз
    turtle.pendown()
    draw_branch(100, level)  # Малюємо дерево

# Запитуємо користувача про рівень рекурсії
try:
    level = int(input("Введіть рівень рекурсії (наприклад, 6): "))
    if level < 0:
        raise ValueError("Рівень рекурсії не може бути від'ємним.")
except ValueError as e:
    print(f"Помилка вводу: {e}")
else:
    turtle.bgcolor("white")  # Колір фону
    turtle.color("green")     # Колір гілок
    draw_pythagorean_tree(level)
    turtle.hideturtle()        # Сховати черепашку
    turtle.done()              # Завершити малювання