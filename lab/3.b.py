
def read():
    str=input("Enter the string: ")
    return str

def up_str(str):
    str_up=str.upper()
    return str_up

def output(str,str_up):
    print("Given String: %s"%st)
    print("String converted to Upper case: %s"%up)

st=read()
up=up_str(st)
output(st,up)



