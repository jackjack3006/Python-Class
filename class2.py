'''

All names created outside a function are known as global variables
All name created within a function are knowd as local variables

How to access and modify a Global Variable

Cannot access the variable with the same name in the same function
'''

e = 5
def add():
	s = e
	#e = 10
#	s = 10
	print(s,e)
add()

#Modifying a global variable
e = 5
def add():
	global e #Helps in modifying a global variable
	e = 10
	print(e)
add()
print(e)
