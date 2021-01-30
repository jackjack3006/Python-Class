def f1(a,b):
	print(a,b)
f1(10,20)
f1(True,"True")
f1([1,2],(2,3))

def mul(a,b = 10):
	print(a*b)
x = mul(10,20)

y = mul(30)
def multiple(*arg):
	print(arg,type(arg))
multiple(11)
multiple(11,22)
