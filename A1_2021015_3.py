def poly(degree,coeff,lb,ub,steps):         #fuction to print value of fuction*stars
    for i in range(lb,ub+1,steps):
        result=0
        for y in range(degree+1):
            Sum=coeff[y]
            for z in range(len(coeff)-y-1):
                Sum=Sum*i
            result=result+Sum
        print(result*"*")
            
def main():                                 #taking inputs and storing values of coeff
    n=int(input("Enter degree of polynomial: "))
    lst=[]
    for i in range (0,n+1):
        temp=int(input(f"Enter coefficiant {i+1}: "))
        lst.append(temp)
    lb=int(input("Enter lower bound of x: "))
    ub=int(input("Enter Upper bound of x: "))
    step=int(input("Enter steps in which x will be incremented: "))
    poly(n,lst,lb,ub,step)
print("Enter the Polynomial fuction details in follwoing section")
print("-----------------Polynomial Fuction-----------------")
main()


