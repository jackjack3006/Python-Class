def f1():
	x = 1
	def f2(a):
		x = 4
		print(a+x)
	print(x)
	f2(x)
	print(x)
f1()

# The id's are not same as they are not immutable 

def fun():
	var = 10
	def fun1():
		var = 20
		print(var,id(var))
	print(var,id(var))
	fun1()
fun()
