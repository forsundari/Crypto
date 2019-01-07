
'''
# Print a String
print("Twinkle Twinkle little star \n\n\t how I wonder what you are?\n\n\t\t Up above the world so high"
      "\n\nLike a diamond in this sky")
'''
##########################
import datetime as datetime

'''
#print Python version

import sys
print("Python version\n")
print(sys.version)
print("python version info\n")
print(sys.version_info)
'''
#############################
'''
#print datetime

import datetime
print("date display")
now = datetime.datetime.now()
print(now.strftime("%y-%m-%d %h:%m:%s"))
print(now.date())
print(now.time())
#print(now.combine())
print(now.astimezone())
'''
#############################
'''
#Area of the circle

#3.14 R **2

#r= 2

print("Area of the circle")
r= float(input("Enter the value\n"))
Area = 3.14*r**2
print("Area of the circle = ", Area)
'''
##############################
'''
#Adding two string
fname = str(input("Enter first name"))
lname = str(input("Enter last name"))
print( fname + " " + lname)
'''
#################################
''''
#list and tuples

values = (input("Enter the values"))
list = values.split(',')
tuple = tuple(list)
print("list",list)
print('tuples',tuple)
'''
#################################
''''
#get file name

file = input("Enter file name")
fileext = file.split(".")
print("Extention file"+repr(fileext[-1]))
'''
################################
''''
#Display the color of list
color = input("Enter the colors")
list = color.split(',')
print('color', list)
print(list[:4])
print(list[0:])
print(list[2:3])
print(list[0:1])
'''
##############################
''''
date = input('Enter the date')
list = date.split('/')
print('date',list)
print(date)
no = datetime.datetime.now("%y/%m/%d")
print(datetime)
'''
######################
''''
ex_date =(12,12,1212)
print("exam date %i/%i/%i"% ex_date)
'''''
###################
'''
a = int(input("Enter value"))
n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print(n1+n2+n3)
'''
####################

#print Doc string
'''
print(abs.__doc__)
'''
##################3
'''''
import calendar
year = int(input("Enter the year :"))
month = int(input("Enter the month"))
print(calendar.month(year,month))

#print(calendar.weekday(year,month,datetime))
'''
####################3

'''
#print("a string that you dont have to escape\nThis \nis a .....multiline\nheredoc string......>example")
print('' a string that you dont have to escape\n This \nis a .....multiline\nheredoc string......>example'')

'''
''''
from datetime import date
fdate = date(2018,12,14)
lname = date(2018,11,10)
edate = fdate - lname
print(edate)
print(edate.days)
'''
####################16
'''
x = int(input("Enter the value:"))
y = x-17
#print("y =",y)
if x>17 :
    r=y*2
    print("r=",r)
    
else:
    print("y=",y)
    '''
######################
'''''
def diff(n):
    if n <=17 :
        return 17-n
    else:
        return (n - 17)*2
print (diff(22))
print (diff(14))
print (diff(17))
'''
########################17
''''
#test whether the number is 100 0f 1000 and 2000
def num(n):
    return (abs(n <=1000)) and (abs(n <= 2000))
     #return num(102)
print(num(200))
'''
#########################18
''''

x =int( input('Enter the value of x:'))
y = int(input('Enter the value of y:'))
z = int(input('Enter the value of z:'))
sum = (x + y +z)
print(sum)
if x == y == z:
    print("sum of equal:", sum)
     
else:
    sum1 = sum *3
    print(sum1)
'''
######################
'''''
def values_of(x,y,z):
    """

    :type x: int
    """
    sum = x+y+z
    if x==y==z:
        sum = sum*3
        return sum
    print (values_of (3,2,1))
    print (values_of (2,2,2))
'''
''''
######################
def mystring(str):
    if len(str)>= 2 and str[:2] == 'Is':
        return str
    return 'Is' + str
print(mystring("Array"))
print(mystring("Isempty"))
'''
def larger_string(str, n):
    result =" "
    for i in range (n):
        result = result + str
    return result

print(larger_string('abs', 2))
print(larger_string('.ph', 3))




