# -*- coding: utf-8 -*-
import ast
f=open("data.txt","r+")
data=ast.literal_eval(f.read())
f.close()
############# Defined Function #############
def showData(i):
    print("-------"*8)
    print("Name : {} {}".format(data[i][0],data[i][1]))
    print("Mobile : {}".format(data[i][2]))
    print("Email ID : {}".format(data[i][3]))
    print("-------"*8)
############# END of Defined Functions########
########### LOOP Main Control ################
while True:
    print('****** Please Choose Preferred Option ******* ')
    print('1. Add New Contact\n2. Search Contact\n3. Quit')
    choice=int(input("Choice :    " ))
    if choice == 1:
        f_name=input("Enter First Name : ")
        l_name=input("Enter Second Name : ")
        phone=input("Enter Phone No : ")
        email=input("Enter Email Id(If No, Skip) : ")
        if email== "":
            email="NULL"
        else : pass
        data.append([f_name,l_name,phone,email])
        f=open("data.txt","w")
        f.write(str(data))
        f.close()
    elif choice == 2:
        print("-"*50)
        print("Choices : ")
        print("1. Search By First Name\n2. Search By Last Name\n3.Search By Mobile No\n4.Search By Email ID")
        choice1=int(input("\nEnter Your Preferred Choice : "))
        if choice1==1:
            x=str(input("Enter First Name :"))
            for i in range(0,len(data)):
                if data[i][0]==x:
                    showData(i)
        elif choice1==2:
            x=str(input("Enter Last Name :"))
            for i in range(0,len(data)):
                if data[i][1]==x:
                    showData(i)
        elif choice1==3:
            x=str(input("Enter Phone No : "))
            for i in range(0,len(data)):
                if data[i][2]==x:
                    showData(i)
        elif choice1==4:
            x=str(input("Enter Email ID :"))
            for i in range(0,len(data)):
                if data[i][3]==x:
                    showData(i)
    elif choice==3:
        break
    else : print("----------- Please Enter Correct Command ---------")
############# EDIT LOOP ################


    