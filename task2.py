from collections import deque
import timeit

class FifoDeque:
    '''
    - в deque есть встроенная оптимизация, выполняется быстрее;
    - читается проще.
    '''
    def __init__(self, size):
        self.size = size
        self.buffer = deque(maxlen=size)

    def enqueue(self, item):
        if len(self.buffer) == self.size:
            self.buffer.popleft()
        self.buffer.append(item)

    def dequeue(self):
        if len(self.buffer) == 0:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()

    def is_empty(self):
        return len(self.buffer) == 0

    def is_full(self):
        return len(self.buffer) == self.size

    def current_size(self):
        return len(self.buffer)


class FifoCustom:
    '''
    - кастомная версия, поэтому больше свободы для изменений/добавлений.
    '''
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * size
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, item):
        if self.is_full():
            self.head = (self.head + 1) % self.size
        else:
            self.count += 1
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return item

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def current_size(self):
        return self.count


size = 1000000

sol1 = """
buffer = FifoDeque(size)
for i in range(size):
    buffer.enqueue(i)
for i in range(size):
    buffer.dequeue()
"""

sol2 = """
buffer = FifoCustom(size)
for i in range(size):
    buffer.enqueue(i)
for i in range(size):
    buffer.dequeue()
"""

setup = """
from __main__ import  FifoDeque, FifoCustom, size
"""

time1 = timeit.timeit(sol1, setup=setup, number=1)
time2 = timeit.timeit(sol2, setup=setup, number=1)


print(f"Время FifoDeque: {time1} секунд")
print(f"Время FifoCustom: {time2} секунд")

