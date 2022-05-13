def getReverse(n):
    
    num=list(n)
    num.reverse()
    n=''.join(num)
    return n        # I avoided typecasting final n to int cause 100 was giving 1 instead of 0001

def checkPalindrome(n):
    
    num=list(n)
    num.reverse()
    pali=''.join(num)
    if n==pali:
        return True
    return False

def checkNarcissistic(n):
    sum=0
    length=len(n)
    for i in n:
        sum=sum+int(i)**length
    n=int(n)
    if n==sum:
        return True
    return False

def findDigitSum(n):
    n=int(n)
    res=[]
    if 0<=n<10:
        res.append(n)
    elif n>=10:    
        while n>=10:
            lst=[int(x) for x in str(n)]
            sum1=sum(lst)
            res.append(sum1)
            n=sum1
    if res!=[]:
        fsum=sum(res)
    else:
        fsum="Error! Enter correct"
    
    return fsum

def findSquareDigitSum(n):                  # it took me more than 24 hours to figure out the right code T-T
    
    n=int(n)
    res=[]
    sq=10
    
    while sq>=10:
        if 0<=n<10:
            sq=n*n
            n=sq
            res.append(sq)
            
    
    
        elif n>=10:    
            while n>=10:
                lst=[int(x) for x in str(n)]
                x = [num ** 2 for num in lst]
                sq=sum(x)
                res.append(sq)
                n=sq
   
   
   
   
   
    if res!=[]:
        fsq=sum(res)
    else:
        fsq="Error! Enter correct"
    
    return fsq

while True:                                             #looping the whole menu again and again
    print('''--------------------------------------------------------------------------------------------------------------------------------
Hello User, Welcome to the Application. Please select one of the following operations.
1. Find reverse of a number
2. Check whether a number is a palindrome or not.
3. Check whether a number is a Narcissistic number or not.
4. Find the sum of digits of a number
5. Find the sum of squares of digits of a number.
6. Select 6 to exit the application.
--------------------------------------------------------------------------------------------------------------------------------\n''')
    option=input("Enter here: ")
    if option=='1':
        print("Great! You want reverse of a number")
        n=input("Enter the number:")
        print(f"Reverse of {n} is {getReverse(n)}")
    
    if option=='2':
        print("Great! You want to check for a Palindrome")
        n=input("Enter the number:")
        if checkPalindrome(n)==True:
            print(f"wow!! {n} is Palindrome")
        else:
            print(f"oh no!! {n} is not a Palindrome. Better luck next time")

    if option=='3':
        print("You wanted to see if a number Narcissistic or not")
        n=input("Enter the number:")
        if checkNarcissistic(n)==True:
            print(f"Narcissistic much? Yes {n} is a Narcissistic number")
        else:
            print(f"Thank god {n} is not a Narcissistic number")

    if option=='4':
        print("Great! You want sum of digits in a number")
        n=input("Enter the number:")
        print(f" The sum of digits of {n} is {findDigitSum(n)}")
          

    if option=='5':
        print("Great :)! You want sum of square of digits in a number")
        n=input("Enter the number:")
        print(f"The sum of square of digits of {n} is {findSquareDigitSum(n)}")
    
    if option=='6':
        exit()





