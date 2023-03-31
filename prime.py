
n = int(input("Enter the number to check whether it is prime or not :"))
count =0

for i in range(2,n):
    if n % i == 0:
        count = count+1
        
if count == 0:
    print(f"The following number {n} is a prime number")
else:
    print(f"The following number {n} is not a prime number")
    

