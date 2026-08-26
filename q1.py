n=int(input("Enter the number of integers you want in the list:"))
l=[]
for i in range(n):
    a=int(input("Enter the number:"))
    l.append(a)
L=l[0]
for i in l:
    if i>L:
        L=i
print("Largest: ",L)
S=l[0]
for i in l:
    if i<L:
        S=i
print("Smallest: ",S)
sum=0
for i in l:
    sum=sum+i
print("Sum: ",sum)
e=0
for i in l:
    if i%2==0:
        e=e+1
print("Even count: ",e)
print("Odd count: ",n-e)
print("Reversed: ",end="")
for i in range(n-1,-1,-1):
    print(l[i],end=" ")