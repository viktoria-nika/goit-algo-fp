# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
# написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
# написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

# Розв'язок

# Створюємо вузол з даними і посиланням на наступний вузол
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Створюємо однозв'язний списк з методами для додавання, реверсування, сортування та об'єднання списків
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # Додає новий вузол в кінець списку
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self): # Виводить елементи списку
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def reverse(self): # Реверсує порядок вузлів у списку
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо наступний вузол
            current.next = prev       # Реверсуємо посилання
            prev = current            # Переходимо вперед
            current = next_node       # Переходимо на наступний вузол
        self.head = prev              # Зміна голови на останній елемент

    def insertion_sort(self): # Сортує список за допомогою вставок
        sorted_list = SinglyLinkedList()
        current = self.head
        while current:
            sorted_list.sorted_insert(current.data)
            current = current.next
        self.head = sorted_list.head  # Після сортування змінюємо голову

    def sorted_insert(self, data): #  Вставляє новий елемент у відсортовану частину списку
        new_node = Node(data)
        if not self.head or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def merge_sorted_lists(self, other_list): # Об'єднує два відсортовані списки в один, підтримуючи порядок.
        merged_list = SinglyLinkedList()
        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.append(current1.data)
                current1 = current1.next
            else:
                merged_list.append(current2.data)
                current2 = current2.next
        
        # Додаємо залишені елементи
        while current1:
            merged_list.append(current1.data)
            current1 = current1.next

        while current2:
            merged_list.append(current2.data)
            current2 = current2.next

        return merged_list
    
# Приклад 

# Створюємо два однозв'язні списки
list1 = SinglyLinkedList()
list1.append(9)
list1.append(3)
list1.append(12)
list1.append(6)

list2 = SinglyLinkedList()
list2.append(18)
list2.append(15)
list2.append(24)
list2.append(21)

# Виводимо початкові списки
print("Список 1:")
list1.print_list()

print("Список 2:")
list2.print_list()

# Реверсуємо перший список
list1.reverse()
print("Список 1 після реверсування:")
list1.print_list()

# Сортуємо перший список
list1.insertion_sort()
print("Список 1 після сортування:")
list1.print_list()

# Об'єднуємо два відсортовані списки
merged_list = list1.merge_sorted_lists(list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()