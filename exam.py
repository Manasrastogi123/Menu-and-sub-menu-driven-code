def merge():
    l1=[]
    while True:
     m1=int(input("Enter contents for 1st list(type 0 to finsih)"))
     if m1==0:
         break
     l1.append(m1)
    print("1st list",l1)
        
    l2=[]
    while True:
     m2=int(input("Enter contents for 1st list(type 0 to finsih)"))
     if m2==0:
         break
     l2.append(m2)
    print("1st list",l2)

    print("The Merge of these two lists",l1+l2)
        
def concatinate():
    mul=[]
    while True:
     n=int(input("Enter contents for 1st list(type 0 to finsih)"))
     if n==0:
         break
     mul.append(n)
    print("Your  list",mul)
    
    hello=int(input("Enter number of times to replicate:"))
    print("Replication",mul*hello)


def listoperation():
    
    userl = list()
    
    while True:
        mo = input("Enter an item (type 'done' to finish): ")
        if mo.lower() == 'done':
            break
        userl.append(mo)
    print("length of the list is",len(userl))


def indexvalue():
    op=[10,20,30,40,50,60,70,80]
    print(op)
    x=int(input("Enter Positive index value:"))
    ab=op[x]
    print("Index value:",ab)

    print("IN NEgative")
    opp=[10,20,30,40,50]
    print(opp)
    y=int(input("Enter Negative INdex Value:"))
    ac=opp[y]
    print("Index Value:",ac)

def slice_d():
    print("In Postive")
    showing=[1,2,3,4,5,6]
    print("Your list",showing)
    x1=int(input("Enter the first slice value (in positive)"))
    x2=int(input("Enter Seconf slice value(in positive:)"))
    a=showing[x1:x2]
    print("Sliced value is",a)

    print("/nIn Negative")
    newlist=[1,2,3,4,5,6,7]
    print("Your list",newlist)
    x3=int(input("Enter the first slice value (in negative)"))
    x4=int(input("Enter Seconf slice value(in negative:)"))
    b=newlist[x3:x4]
    print("Sliced Value is",b)


def listwithfunction():
    listtt = list()
    
    while True:
        m = input("Enter an item (type 'done' to finish): ")
        if m.lower() == 'done':
            break
        listtt.append(m)
    
    print("Here is your list:", listtt)

def listwithoutfunction():
    values = []
    
    while True:
        m = input("Enter an item (type 'done' to finish): ")
        if m.lower() == 'done':
            break
        values.append(m)
    
    print("Here is your list:", values)

def multiplevalues():
    good=[]
    given = ["Manas", "Rastogi"]  
    print(given)
    while True:
        god = input("Enter an item (type 'done' to finish): ")
        if god.lower() == 'done':
            break
        good.extend(god) 
    print("New list is",given+good)

def singlelist():
    fan=[1,2,3,4,5,6]
    jk=int(input("Enter to add one value:"))
    fan.append(jk)
    print("New list",fan)


def mainmenu():
    print("1. Display Empty List:")
    print("2. Continue:")
    print("3. Exit:")

def submenu():
    print("1. Create list without using function")
    print("2. Create list using function")
    print("3. Display Values from given list by slicing(Both Postive and Negative)")
    print("4. Display values from given list by indexing(Both positive and Negative)")
    print("5.Display Length of my list")
    print("6.Merge my two lists")
    print("7.Multiplay your list")
    print("8.Add multiple values to our list")
    print("9.Add Single value in given list")
    print("10.Del Elements")
    print("0.Exit")

def delelements():
    print("1.Do Pop()")
    print("2.Do remove")
    print("3.Do Del")
    print("4.Do clear")
    print("0.exit")

def pop():
    valorant=[1,2,3,4,5,6]
    print(valorant)
    cod=int(input("Enter the index to remove:"))
    mw=valorant.remove(cod)
    print("list after poping",valorant)

def remove():
    minecraft=[1,2,3,4,5,6]
    print(minecraft)
    aka=int(input("Enter the index to remove:"))
    valo=minecraft.pop(aka)
    print("list after poping",minecraft)
def dele():
    print("In Postive")
    fortnite=[1,2,3,4,5,6]
    print("Your list",fortnite)
    x5=int(input("Enter the first slice value (in positive)"))
    x6=int(input("Enter Seconf slice value(in positive:)"))
    del fortnite[x5:x6]
    print("Sliced value is",fortnite)


while True:
    mainmenu()
    choice = int(input("Enter your choice from (1-3): "))

    if choice == 1:
        a = []
        print("Here is an Empty list:", a)

    elif choice == 2:
        submenu()
        ch = int(input("Enter Your choice:"))

        if ch == 1:
            listwithoutfunction()
        elif ch==2:
            listwithfunction()
    
        elif ch==3:
            slice_d()

        elif ch==4:
            indexvalue()
            
        elif ch==5:
            listoperation()
        
        elif ch==6:
            merge()

        elif ch==7:
            concatinate()

        elif ch==8:
            multiplevalues()
        
        elif ch==9:
            singlelist()
        
        elif ch==10:
            delelements()
            life=int(input("Enter Your choice:"))
            if life==1:
                pop()
            
            elif life==2:
                remove()

            elif life==3:
                dele()
            elif life==4:
                ending=[1,2,3,4,5]
                print("End")
                ending.clear()   
                print(ending)
            elif life==0:
                break
            else:
                print("Invalid choice")
        elif ch==0:
            break   
        else:
            print("Invalid choice")
    elif choice==3:
        break
    else:
        print("Invalid Choice")