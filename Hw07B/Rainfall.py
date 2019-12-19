def RainFall():

    ifs = open("months.txt",'r')
    lines = ifs.readlines()
    monthNames=["January","February","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
    monthNames = lines
    rainfall=[0]*12
    for i in range(len(monthNames)):
        rainfall[i]=int(input("Enter Total Rain in "+monthNames[i]+" "))
    print("Total Rainfall:",sum(rainfall))
    print("Average Rainfall:", sum(rainfall)/len(rainfall))
    print(str(monthNames[rainfall.index(min(rainfall))]),"has the lowest rainfall:",min(rainfall))
    print(str(monthNames[rainfall.index(max(rainfall))]), "has the highest rainfall:",max(rainfall))


RainFall()