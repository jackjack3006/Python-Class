'''
PARAMETER PASSING:
Python uses ONLY pass by value
'''

def f1(x):
	x = [3,4,x]
	print("fn",x)
a = [1,2]
f1(a)
print("main",a)

def swap(x,y):
	x,y = y,x
	
print(swap(11,12))

