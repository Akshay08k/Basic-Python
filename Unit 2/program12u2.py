def decor(fun):
    def inner():
        value = fun()
        return value+3
    return inner
@decor
def num():
    return 10
print(num())