class Fibonacci:
    def __init__(self, max_limit=4000000):
        self.max_limit = max_limit
        self.a, self.b = 1, 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.b <= self.max_limit:
            if not self.b % 2:
                result = self.b
                self.a, self.b = self.b, self.a + self.b
                return result
            self.a, self.b = self.b, self.a + self.b
        raise StopIteration


def fibonacci_sum():
    sum_even = 0
    for fib in Fibonacci():
        sum_even += fib
    return sum_even


print(fibonacci_sum())
