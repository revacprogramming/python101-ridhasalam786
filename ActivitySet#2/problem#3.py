
def get_cs():
    str=input("Enter the string:")
    print("String:%s"%str)
    nstr = str.split(";")
    return nstr

def cs_to_lot(cs):
    z = []
    for i in cs:
        x = i.split('=')
        y = (x[0],x[1])
        z.append(y)
    return z

def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)

if __name__ == "__main__":
    main()

  

'''def get_cs():
  str=input("Enter the string:")
  print("String:%s"%str)


def cs_to_lot(cs):
    """convert connected string to list of strings"""


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()'''