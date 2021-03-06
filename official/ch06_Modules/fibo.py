import sys

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

print("sys.__name__ = ", __name__)
print("sys.path = ", sys.path)
print("sys.platform = ", sys.platform)

if __name__ == "__main__":
    fib(int(sys.argv[1]))
