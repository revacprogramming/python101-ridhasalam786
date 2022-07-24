f=open("std.txt",'a+')
flag=input("Do you want to update the file Y/N")
if(flag=='Y'):
	n=int(input("Enter how many students"))
	for i in range(n):
		srn,name,sem,sec,avgmark=input("Enter the SRN number,name, semester,section and average mark of the student\n").split()
		f.writelines(srn+"  "+name+"  "+sem+"  "+sec+"  "+avgmark+"\n")
f.close()
# code to extract 'A' section students with 75% above
print("Contents of student file is")
mylines=[ ]
with open("std.txt",'rt') as outfile:
	for myline in outfile:
		mylines.append(myline.split())
	for element in mylines:
		avgmark=int(element[-1])
		sec=str(element[-2])
		if(avgmark >= 75 and sec=='A'):
			print(element)
