'''
num = int(input('Enter the value of num'))
while(num == 1):
    print(num)
    break
else:

    num +=1
    #num -=1
    print(num)
'''
################################
'''
count = 0
while True:
    print(count)
    count +=1
    if (count > 10):
        break
'''
#############################

'''
for x in range(20):
    if (x%2) ==0:
        print(x)
        continue
'''
for x in range(20):
    if (x%2)==1:
        print(x)
        continue
