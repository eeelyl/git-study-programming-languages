def convert_number(func_list):
    def converter(n):
        results = {}
        for func in func_list:
            results[func.__name__] = func(n)
        return results
    return converter


# Пример использования
funcs = [float, bin, hex, str]

converter = convert_number(funcs)
n = 25
results = converter(n)

print(f"Преобразуем полученное число {n} в типы:")
for func_name, result in results.items():
    print(f"{func_name} => {result}")
