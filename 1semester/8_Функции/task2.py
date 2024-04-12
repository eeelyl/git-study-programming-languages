# Чтобы проверить понимание параметров и область их видимости Николай создал 3 функции (представлены ниже).
# Попытайтесь предугадать, как поведет себя каждая из них при запуске (возникнут ли ошибки, что возвратится).

def func1():
    param = 4

    def inner():
        param += 1
    return param


def func2():
    param = 4

    def inner(var):
        var += 1
    inner(param)
    return param


def func3():
    param = 4

    def inner(var):
        var += 1
        return var
    param = inner(param)
    return param


print(func1())
print(func2())
print(func3())
