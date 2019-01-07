
str = "PythomProgram"
str1 = "Edureka"
str2 = 'p,r,o,g,r,a,m'

# To Find

print(str.find("program"))

print(str1.find("ureka"))

# str = "Python Programming"

#Replace

print(str1.replace('Ed','M'))
print(str.replace('Pro','My') and str.replace('Py', 'U'))   #check the syntax

#split

print(str2.split(','))

#count

print(str.count('o', 0,13 ))
print(str.count('m',6,13))
print(str.count('m',0))

# Upper

print(str.upper())

# Max

print(max (str))

# Min

print(min (str))

# isalpha

print(str.isalpha())