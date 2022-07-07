def sub_str(str):
    m=int(input("Enter the starting index: "))
    n=int(input("Enter the ending index: "))
    sub=str[m:n]
    print("The required substring is %s"%sub)

str=input("Enter the string: ")
sub_str(str)

