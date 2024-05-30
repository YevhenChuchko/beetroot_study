class OrderedList:

    def __init__(self):
        self.elements = list()

    def insert(self, value):
        self.elements = (
            [element for element in self.elements if element < value]
            + [value]
            + [element for element in self.elements if element > value]
        )

    def binary_search(self, value):
        low = 0
        high = len(self.elements) - 1

        while low <= high:
            mid = (high + low) // 2
            if self.elements[mid] > value:
                high = mid - 1
            elif self.elements[mid] < value:
                low = mid + 1
            else:
                return mid

        return -1

    def recursive_binary_search(self, value):
        return self._recursive_binary_search(value, 0, len(self.elements) - 1)

    def _recursive_binary_search(self, value, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2
        if self.elements[mid] > value:
            return self._recursive_binary_search(value, low, mid - 1)
        elif self.elements[mid] < value:
            return self._recursive_binary_search(value, mid + 1, high)
        else:
            return mid

if __name__ == "__main__":
    container = OrderedList()
    container.insert(40)
    container.insert(20)
    container.insert(60)
    container.insert(50)
    container.insert(30)
    print(container.elements)

    print(container.binary_search(35))
    print(container.recursive_binary_search(50))
    print(container.recursive_binary_search(35))
