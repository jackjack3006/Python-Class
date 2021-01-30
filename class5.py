def mymax(*arg):
	great = arg[0]
	for x in arg:
		if x > great:
			great = x
	return great
print(mymax(10,20))
print(mymax("tiger","zebra","elephant","ant","zzz"))



def f3(*args):
	print(args)
val = (5,6,7)
f3(val,type(val)) # One element tuple
f3(*val,type(val)) # Each element is considered as an element in the tuple


def f5(a,b,*args,**kwargs):
	print("a,b is",a,b)
	print("args = ",args,type(args))
	print("kwargs = ",kwargs,type(kwargs))
f5(2,3,4,5,"abc","pes","python",red = 'r',orange = 'o',green = 'g')
