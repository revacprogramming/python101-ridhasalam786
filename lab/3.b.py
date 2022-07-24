def read():
    lst=[]
    while True:
      str=input("Enter the string: ")
      if str=='done':break
      lst.append(str)
    return lst

def up_str(str):
    for i in str:
        str_up=i.upper()
        print(str_up)

st=[]
st=read()
up=up_str(st)
  




