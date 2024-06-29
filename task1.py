import timeit
import time

def isEven(value):
      time.sleep(0.1)
      return value % 2 == 0

def isEven_new(value):
      time.sleep(0.1)
      return (value & 1) == 0


arr = list(range(-100, 1, 100))

# Решение isEven
sol1 = """
result = [isEven(x) for x in arr]
"""

# Решение isEven_new
sol2 = """
result = [isEven_new(x) for x in arr]
"""

# Подготовка для timeit
setup = """
from __main__ import isEven, isEven_new, arr
"""

# Измерение времени выполнения
time1 = timeit.timeit(sol1, setup=setup, number=1)
time2 = timeit.timeit(sol2, setup=setup, number=1)


print(f"Время выполнения решения №1: {time1} секунд")
print(f"Время выполнения решения №2: {time2} секунд")
