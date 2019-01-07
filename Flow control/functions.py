'''
num=int(input("enter n:"))
print(fibo(num))
'''

def fibo(n):
    a=0
    b=1
    for x in range(n):
        a = b
        b =a+b
        print(a,'\n')
        return b

    num = int(input("Enter the value of n:"))
    print(fibo(num))
