print("Either input numbers from 1-5 or input the pattern type name")   #menu
options='''1.right angled triangle
2.isosceles triangle
3.kite
4.half kite
5.X'''
print(options)
type=input()

if type=='1' or type=='right angled triangle':                          #code for right angle triangle
    n=int(input("kindly enter the size of Right Angle triangle:"))
    for i in range(n+1):  
        for j in range(i):  
            print(i,end=" ")
        print()

if type=='2' or type=='isosceles triangle':                             #code for isosceles triangle
    n=int(input("kindly enter the size of isosceles triangle:"))
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(end= ' ')
        for k in range(1, (2 * i)):
            print(k, end='')
        print()    

if type=='3' or type=='kite':                                           #code for kite
    n=int(input("kindly enter the size of kite:"))
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(end= ' ')
        for k in range(1, (2 * i)):
            print(k, end='')
        print()
    for i in range(n-1, 0, -1):
        for j in range(1, (n-i+1)):
            print(end=' ')
        for k in range(1, (2*i)):
            print(k, end='')
        print()

if type=='4' or type=='half kite':                                      #code for half kite(2 Right angle triangle)
    n=int(input("kindly enter the size of half kite:"))
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()
    for i in range(n-1, 0, -1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()

if type=='5' or type=='X':                                              #code for X
    n=int(input("kindly enter the size of X:"))
    for i in range(n, 0, -1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(1, 2*i):
            print(j, end="")
        print()
    for i in range(2, n+1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(1, 2*i):
            print(j, end="")
        print()
    