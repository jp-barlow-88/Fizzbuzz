from sympy import primerange as prime
a = 0
b = 99
plist = list(prime(a, b))


def fizz(x):
    if x in plist:
        if x % 4 == 0:
            return 'BuzzWhizz'
        elif x % 2 == 0:
            return 'FizzWhizz'
        else:
            return 'Whizz'
    if x % 2 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    elif x % 4 == 0:
        return 'Buzz'
    elif x % 2 == 0:
        return 'Fizz'
    else:
        return x


if __name__ == '__main__':
    for i in range(0, 101):
        print(fizz(i))
