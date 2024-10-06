print("Python is a high-level, object-oriented, interpreted language that is easy to learn and use. It is known for its readability and simplicity.")
n=int(input("enter a number: "))
def evod():
    if(n%2==0):
        print(f'{n} is even')
    else:
        print(f'{n} is odd')
def rev():
    temp=n
    reve=0
    while(temp!=0):
        rem=temp%10
        reve=reve*10+rem
        temp=temp//10
    print(f"reverse of number is {reve}")
def sumdig():
    temp=n
    reve=0
    while(temp!=0):
        rem=temp%10
        reve=reve+rem
        temp=temp//10
    print(f"Sum of digits of a number is {reve}")
def pallindrome():
    temp=n
    cons=n
    reve=0
    while(temp!=0):
        rem=temp%10
        reve=reve*10+rem
        temp=temp//10
    if(cons==reve):
        print(f"{reve} is a pallindrome")
    else:
        print(f"{reve} is not a pallindrome")
def fact():
    res=1
    for i in range(1,n+1):
        res=res*i
    print(f"factorial of {n} is {res}")
def sum():
    res=1
    for i in range(1,n+1):
        res=res+i
    print(f"sum of first {n} digits are {res}")
def evsum():
    res=0
    for i in range(1,n+1):
        if(i%2==0):
            res=res+i
    print(f"sum of first {n} even digits are {res}")
def oddsum():
    res=0
    for i in range(1,n+1):
        if(i%2==1):
            res=res+i
    print(f"sum of first {n} odd digits are {res}")
def evcount():
    res=0
    for i in range(1,n+1):
        if(i%2==0):
            print(i, end="," if i < n-1 else "\n")
def oddcount():
    for i in range(1,n+1):
        if(i%2==1):
            print(i, end="," if i < n-1 else "\n")
def prime():
    a=n
    count=0
    for i in range(1,a+1):
        if(a%i)==0:
            count+=1
    if(count==2):
        print(f"{a} is a prime number")
    else:
        print(f"{a} is not a prime number")
def primeseries():
    for i in range(2,n+1):
        count=0
        for j in range(2,i):
            if(i%j==0):
                count=1
                break
        if(count==0):
            print(i, end="," if i < n else " ")
    print(" ")
def square():
    for i in range(1,n+1):
        print(i*i, end="," if i < n else "\n ")
def cube():
    for i in range(1,n+1):
        print(i*i*i, end="," if i < n else "\n ")
while True:
    print("""Select an operation to perform on the given number
      1 - To find the given number is even or odd
      2 - To find reverse of a number
      3 - To find sum of digits of a number
      4 - To check he given number is palindome or not
      5 - To find facorial of a given number
      6 - To find sum of first n numbers
      7 - To find sum of first n even numbers
      8 - To find sum of first n odd numbers
      9 - To find print of first n even numbers
      10 - To find print of first n odd numbers
      11 - To check weather the given number is prime or not
      12 - To print first n prime numbers
      13 - To print squares of n numbers
      14 - To print cubes of n numbers
      15 - To perform all operations
      16 - Exit""")
    z=int(input())
    if(z==1):
        evod()
    elif(z==2):
        rev()
    elif(z==3):
        sumdig()
    elif(z==4):
        pallindrome()
    elif(z==5):
        fact()
    elif(z==6):
        sum()
    elif(z==7):
        evsum()
    elif(z==8):
        oddsum()
    elif(z==9):
        oddcount()
    elif(z==10):
        evcount()
    elif(z==11):
        prime()
    elif(z==12):
        primeseries()
    elif(z==13):
        square()
    elif(z==14):
        cube()
    elif(z==15):
        evod()
        rev()
        sumdig()
        pallindrome()
        fact()
        sum()
        evsum()
        oddsum()
        evcount()
        oddcount()
        prime()
        primeseries()
        square()
        cube()
    elif(z==16):
        print("Exited...")
        break
