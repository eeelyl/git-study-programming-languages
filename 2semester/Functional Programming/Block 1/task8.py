from functools import lru_cache
import time


@lru_cache()
def LRU_count_stairs(n):
    if n <= 1:
        return 1
    else:
        total = 0
        for i in range(n):
            total += LRU_count_stairs(i)
        return total


def count_stairs(n):
    if n <= 1:
        return 1
    else:
        total = 0
        for i in range(n):
            total += count_stairs(i)
        return total


n = 25
start_time = time.time()
res_LRU = LRU_count_stairs(n)
end_time = time.time()
print(
    f"Количество лесенок из {n} кубиков: {res_LRU}. Время: {end_time-start_time}")
start_time = time.time()
res = count_stairs(n)
end_time = time.time()
print(
    f"Количество лесенок из {n} кубиков: {res}. Время: {end_time - start_time}")
