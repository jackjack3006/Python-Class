#call back
#mechanism of passing a function as argument and calling the function indirectly
def f1():
	print("this is f1")
def f2():
	print("this is f2")
def f3():
	a = 10
	b = 20
	x = (a+b)/(a*b)
	print(x)
def outer(fn):  #Function to call a function
	fn()
outer(f1)
outer(f2)
outer(f3)

def mymax(*arg):
	great = arg[0]
	for x in arg:
		if x > great:
			great = x
	return great

print(max(10,20))
print(max(20,30,40,50))
print(max("tiger","zebra","elephant","ant","zzz"))

print(mymax(10,20))
print(mymax("tiger","zebra","elephant","ant","zzz"))

def mymax(*arg,key = None):    #Used to pass function
	if key == None:
		great = arg[0]
		for x in arg:
			if x > great:
				great = x
		return great
	else:
		great = arg[0]
		print(key)
		for x in arg:
			if key(x) > key(great):
				great = x
	return great
print(mymax(10,20))
print(mymax("tiger","zebra","elephant","ant","zzz",key = len))
