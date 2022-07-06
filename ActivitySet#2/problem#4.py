def get_cs():
    str=input("Enter the string:")
    print("Given String:%s"%str)
    nstr = str.split(";")
    return nstr


def cs_to_lot(cs):
    z = []
    for i in cs:
        x = i.split('=')
        y = (x[0],x[1])
        z.append(y)
    return z



def lot_to_cs(lot):
    m = []  # to convert tuple into list
    for i in lot:
        a = list(i)
        m.append(a)

    l = []  # to join = btw list items
    for i in m:
        s = "="
        s = s.join(i)
        l.append(s)

    # to join ; btw list items
    nlot = ";"
    nlot = nlot.join(l)
    return nlot


def main():
    cs=get_cs()
    print("\t")

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print("Given string to list:",lot)
    print("\t")

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print("List to string:",cs)
    print("\t")


if __name__ == '__main__':
    main()


'''def get_cs():
    """get string input"""


def cs_to_lot(cs):
    """convert connected string to list of strings"""


def lot_to_cs(lot):
    """convert list of strings to connected string"""


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main() '''

