empfile=open("emp.txt")
flag=input("Do you want to update the file Y/N")
if(flag=='Y'):
    n=int(input("Enter how many Employees"))
    for i in range(n):
        Emp_code, Emp_name,Basic_salary, DA, LIC,PF=input("Enter the Emp_code, Emp_name, Basic_Salary, DA, LIC and  PF\n").split()
        Total_deductions=float(LIC)+float(PF)
        Gross_salary=float(Basic_salary)+float(DA)
        Net_salary=Gross_salary-Total_deductions
        empfile.writelines(Emp_code+" "+Emp_name+" "+str(Basic_salary)+" "+str(DA)+" "+str(Gross_salary)+" "+str(Net_salary)+" "+str(LIC)+" "+str(PF)+" "+str(Total_deductions)+"\n")
empfile.close()
print("\nEmployee details Emp_code, Emp_name, Basic_Salary, DA,Gross_salary, Net_salary, LIC and  PF, Total_deductions are\n")
with open("emp.txt") as outfile: 
    for oneline in outfile:
             print(oneline)
