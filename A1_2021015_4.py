def boolv(x):                               #converts input string to boolean
    if x=="True" or x=="true":
        x=True
    elif x=="False" or x=="false":
        x=False
    else:
        x="error! enter correct input"
    return x


def fn1(b1):                                #boolean fuction one(HardCoded)
    if boolv(b1)==True and not boolv(b1)==True:
        return True
    elif boolv(b1)==False:
        return False
    else:
        return("Error! Input correct value")
        

def fn2(b1,b2,b3):                          #boolean fuction two(HardCoded)
    b1=boolv(b1)
    b2=boolv(b2)
    b3=boolv(b3)
    if (b1 or b2)==True and (b2 or not b3)==True:
        return True
    else:
        return False


def isSatisfiable():                       #main function(takes input, print fuction value)
    print('''----------------------------------------------
    Choose which function you want to execute -
    1. Fuction 01 - [b1 and not b1]
    2. Fuction 02 - [(b1 or b2) and (b2 or not b3)]
    ---------------------------------------------- ''')
    fn=input("kindly enter the the function number(1/2): ")
    if fn=="1":
        print("Great! Fuction 1 is [b1 and not b1]")
        b1=input("Enter b1: ")
        if fn1(b1)==True:
            print("\nSatisfiable")
            print(b1)
        elif fn1(b1)==False:
            print("\nUnsatisfiable")
        else:
            print("Error! enter correct input")
        
        
    
    
    elif fn=="2":
        print("\nGreat! Function 2 is [(b1 or b2) and (b2 or not b3)]")
        b1=input("Enter b1: ")
        b2=input("Enter b2: ")
        b3=input("Enter b3: ")
        if fn2(b1,b2,b3)==True:
            print("\nSatisfiable")
            print(boolv(b1),",",boolv(b2),",",boolv(b3))
        elif fn2(b1,b2,b3)==False:
            print("\nUnsatisfiable")
        
        
    else:
        print("Error! Enter correct integer.")

isSatisfiable()                           #initiating main function




