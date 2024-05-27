# Простеньке, безмолісне сортування шляхом знаходження мінімального значення елементу та
# його додавання у відсортований список методом pop

def min_sort(sequence):
    result = list()  # Створюємо порожній список
    for counter in range(len(sequence)):    # Проходимо по всіх елементах початкового списку
        min_element = min(sequence)     # Знаходимо мінімальний елемент у списку
        index_of_min = sequence.index(min_element)  # Знаходимо індекс мінімального елемента
        sequence.pop(index_of_min)  # Видаляємо мінімальний елемент з початкового списку
        result.append(min_element)  # Додаємо мінімальний елемент до результатного списку
        # result.append(sequence.pop(sequence.index(min(sequence))))  - скорочена версія
    return result

if __name__ == "__main__":
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    print(min_sort(to_sort))