def is_prime(n):
    if n < 2:
        return False
    k=0
    for i in range(1,int(n**0.5)):
        if n%i==0:
            k+=1
        if k>1:
            return False
            break
    else:#This else block will be executed only when the for loop never encounters the break statement
        return True

n=int(input("Enter a number greater than 2:"))

if not n>2:
    print("Number not greater than 2")
    exit()
for i in range(2,n+1):
    if is_prime(i):
        print(i, end=" ")




