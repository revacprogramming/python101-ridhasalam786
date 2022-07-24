class ARS:
    def __init__(self,name,source,destination,travel_date):
        self.pass_name=name
        self.pass_source=source
        self.pass_destination=destination
        self.pass_travel_date=travel_date
    def display_pass_details(self):
        print(self.pass_name,"\t\t",self.pass_source,"\t\t",self.pass_destination,"\t\t",self.pass_travel_date)
Airlineobject=[]
n=int(input("How many passengers"))
for i in range(n):
    name=input("Enter Name\n")
    source=input("Enter Source\n")
    destination=input("Enter Destination\n")
    travel_date=input("Enter Travel Date\n")
    Airlineobject.append(ARS(name,source,destination,travel_date))
print("Passenger Details travelled from Bengaluru to London are\n")
for i in range(0,len(Airlineobject)):
    if((Airlineobject[i].pass_source=="Bengaluru") and (Airlineobject[i].pass_destination=="London")):
        Airlineobject[i].display_pass_details()
print("Passenger Details travelled from USA to China on 10th feb 2020 are\n")
for i in range(0,len(Airlineobject)):
    if((Airlineobject[i].pass_source=="USA") and (Airlineobject[i].pass_destination=="China") and Airlineobject[i].pass_travel_date=="10/Feb/2020"):
        Airlineobject[i].display_pass_details()
