def input_two_numbers():
    a,b = input("Enter two integers ").split()
    a=int(a)
    b=int(b)
    return a, b


def add(a, b):
    s = a + b
    return s


def output(a, b, sum):
    print("%s+%s is %s"%(a,b,sum))


def main():
    a,b = input_two_numbers()
    sum = add(a, b)
    output(a, b, sum)


if __name__ == '__main__':
    main()

  
'''def add(a, b):
    pass  # ...


def output(a, b, sum):
    pass  # ...


def main():
    a, b = input_two_numbers()
    sum = add(a, b)

  

    output(a, b, sum)


if __name__ == '__main__':
    main()
'''

