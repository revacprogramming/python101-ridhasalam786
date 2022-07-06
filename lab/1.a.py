def input_srn():
    print("Input SRN")
    while True:
        n=input("Enter the srn no.s (type done to stop): ")
        if n == "done":
            break
        if len(n) > 6:
            print("Invalid input")
            print("Try again")
            continue
        num = int(n)
        list1.append(num)
    print(list1)



def append_srn(list1):
    print("Add SRN")
    while True:
        n=input("Enter the new srn no.s (type done to stop or if no elements to be added): ")
        if n == "done":
            break
        if len(n) >6:
            print("Invalid input")
            print("Try again")
            continue
        m = int(input("Enter the respective index: "))
        num = int(n)
        list1.insert(m,num)
    print(list1)

def search_srn(list_1):
    print("Search SRN")
    p=int(input("Enter the element for which index required: "))
    q=list1.index(p)
    print(q)

def merge_srn(srn_list1,srn_list2):
    print("Merge SRN")
    list2=[]
    list2=srn_list1+srn_list2
    print(list2)

list1=[]
while True:
    a = input("Enter the function (type done to stop): ")
    if a=="done":
        break
    if a=="input srn":
        input_srn()
    elif a=="add new srn":
        append_srn(list1)
    elif a=="search srn":
        search_srn(list1)
    elif a=="merch srn lists":
        srn_list1 =input_srn()
        srn_list2 =input_srn()
        merge_srn(srn_list1,srn_list2)