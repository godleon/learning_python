
class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []

    def f(self):
        return 'Hello World!'


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = MyClass()
print(x.__doc__)
print(x.f())

x = Complex(3.0, -4.5)
print(x.r)
print(x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
