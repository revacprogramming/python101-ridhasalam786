def read():
    for i in range(2):
        tup_i=()
        l_i=[]
        n=input("Enter elements of list: ")
        if n=="done":
            break
        num=int(n)
        l_i.append(num)
        tup_i=tuple(l_i)
        print(tup_i)

read()