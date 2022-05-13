def fn(x):                              # function to create and sum terms of polynomial function
    fn=0
    for i in lst:
        fn=fn+x**i
    return fn
def intgfxdx(a,d):                      #integration function
    fa=((a+d)-a)/6*(fn(a)+4*fn((a+(a+d))/2)+fn(a+d))
    return fa

def calculate_area(b,a,d):              # calculate area
    Tarea=0
    if (b-a)%d==0:
        while a<b:
            Tarea=Tarea+intgfxdx(a,d)
            a=a+d
    else:
        return "Invalid"
    return Tarea

print('''Lets calculate area of polynomial function using Simpson's 1/3 Algorithm       
For this you have to give me input as follows
a will be the lower limit
b will be the higher limit
d will the steps/common difference
lst will the a list of exponents of x in fn
----------------------------------------------------------------------------------
kindly enter a,b,d as integers and d as a list(without [ ] and ',')
----------------------------------------------------------------------------------''')              #menu
a=int(input("Enter a: "))
b=int(input("Enter b: "))
d=int(input("Enter c: "))
lst=[int(x) for x in input("Enter List: ").split()]

print(calculate_area(b,a,d))






