# Lists

filename = "dataset/romeo.txt"
fh = open(filename)
lst = list()
for line in fh:
    line.rstrip()
    w=line.split()
    for i in w:
        if i in lst:
            continue
        else:
            lst.append(i)
lst.sort()
print(lst)


