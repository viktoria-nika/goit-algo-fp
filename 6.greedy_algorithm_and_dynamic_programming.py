# Завдання 6. Жадібні алгоритми та динамічне програмування

# Необхідно написати програму на Python, яка використовує два підходи
#  — жадібний алгоритм та алгоритм динамічного програмування
#  для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
# Кожен вид їжі має вказану вартість і калорійність. 
# Дані про їжу представлені у вигляді словника, де ключ — назва страви, 
# а значення — це словник з вартістю та калорійністю.

# Розв'язок

# Запишемо наш словник з продуктами
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Розрахуємо співвідношення калорій до вартості
    ratios = [(item, values['calories'] / values['cost']) for item, values in items.items()]
    # Сортуємо за співвідношенням, від найбільшого до найменшого
    ratios.sort(key=lambda x: x[1], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item, ratio in ratios:
        cost = items[item]['cost']
        if cost <= budget:
            selected_items.append(item)
            total_calories += items[item]['calories']
            budget -= cost
            
    return selected_items, total_calories

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    n = len(items)
# Сортуємо за співвідношенням, від найбільшого до найменшого
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    item_list = list(items.keys())
# Заповнюємо таблицю
    for i in range(1, n + 1):
        item = item_list[i - 1]
        cost = items[item]['cost']
        calories = items[item]['calories']
        
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]
    
    # Відновлення обраних продуктів
    total_calories = dp[n][budget]
    selected_items = []
    remaining_budget = budget
    
    for i in range(n, 0, -1):
        if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:
            selected_items.append(item_list[i - 1])
            remaining_budget -= items[item_list[i - 1]]['cost']

    return selected_items, total_calories

# Приклад 
budget = 100
greedy_result = greedy_algorithm(items, budget)
dynamic_result = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print("Обрані страви:", greedy_result[0])
print("Сумарна калорійність:", greedy_result[1])

print("\nАлгоритм динамічного програмування:")
print("Обрані страви:", dynamic_result[0])
print("Сумарна калорійність:", dynamic_result[1])