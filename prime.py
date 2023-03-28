"""
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the third number :"))

if(num1 > num2) and (num1 > num3):
    print("The greatest number is ", num1)
elif(num2 > num1) and (num2 > num3):
    print("The greatest number is ", num2)
else:
    print("The greatest number is ", num3)
    
num4 = int(input("Enter the number to find even or odd :"))

if(num4 % 2 == 0):
    print("The given number",num4,"is a even number")
else:
    print("The given number",num4,"is a odd number")
    
num5 = int(input("Enter the first number :"))
num6 = int(input("Enter the second number :"))
temp = 0

print("Before swapping")
print("X=",num5)
print("Y=",num6)

print ("After swapping")
temp = num5
num5 = num6
num6 = temp

print("X=",num5)
print("Y=",num6)


n = int(input("Enter a number to find factorial: "))

factorial = 1
for i in range(1, n+1):
    factorial *= i

print("The factorial of the given number",n,"is",factorial)


string1 = 'PRADEEP'
for letters in string1:
    print(letters)

    
list1 = [1,2,3,4,5]
for res in list1:
    print(res)
    
    
n = int(input("Enter the number to print its table :"))

for i in range(1,11):
    res = n * i
    print(n,"*",i,"=", res)
    
n = int(input("Enter limit :"))

a = 0
b = 1

for i in range(1,n):
    print(a)
    c = a + b
    a = b
    b = c
    
    
n = int(input("Enter the number to check whether it is prime or not :"))
count =0

for i in range(2,n):
    if n % i == 0:
        count = count+1
        
if count == 0:
    print(f"The following number {n} is a prime number")
else:
    print(f"The following number {n} is not a prime number")
    """

n1, n2, n3=(int(input("enter the number :").split())
        
s = (n1 + n2 + n3)/3
print(s)