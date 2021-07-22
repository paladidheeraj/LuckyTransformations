print("Enter the size of array and number of operations to be performed")
n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(k):
    for j in range(n-1):
        if l[j]==4 and l[j+1]==7:
            if j%2==0:
                l[j+1]=4
            else:
                l[j]=7
print("The array after performing required operations is")
for i in range(n):
    print(l[i],end=" ")
        
