#wap to check fibonacci series of number.
a=int(input())
b=int(input())
n=int(input())
if n==1:
    print(a)
elif n==2:
    print(a,b)
else:
    print(a,b)
    for i in range(n-2):
        c=a+b
        print(c)
        a,b=b,c
    
