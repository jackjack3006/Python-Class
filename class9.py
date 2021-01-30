def outer(msg):
	#This is my outer encloser
	def inner():
		#This is the nested func
		print(msg)
def f():
	x = 5
	y = 10
	return x
h = f()
print(h)
