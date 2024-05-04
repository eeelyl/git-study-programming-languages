from functools import lru_cache


@lru_cache()
def count_stairs(n):
    if n <= 1:
        return 1
    else:
        total = 0
        for i in range(n):
            total += count_stairs(i)
        return total


n = 35
res = count_stairs(n)
print(f"Количество лесенок из {n} кубиков: {res}")
