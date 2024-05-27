#Це алгоритм, заснований на порівнянні, в якому кожна пара сусідніх
# елементів порівнюється, і елементи міняються місцями, якщо вони не впорядковані.


def bubble_sort(sequence):
    for counter in range(len(sequence)):    # зовнішній цикл, що ітерує весь список
        for index in range(len(sequence) - counter - 1):    # Внутрішній цикл для непосортованої частини списку
            if sequence[index] > sequence[index+1]:    # Порівнюємо сусідні елементи
                sequence[index], sequence[index+1] = sequence[index+1], sequence[index]   # міняємо їх місцями, якщо вони в неправильному порядку
        print(sequence)    # Прінтимо список після кожної ітерації зовнішнього циклу
    return sequence

if __name__ == "__main__":
    to_sort = [15, 9, 8, 1, 4, 11, 7, 12, 13, 6, 5, 3, 16, 2, 10, 14]
    print(bubble_sort(to_sort))
