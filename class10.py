def outer(msg):
	#This is my outer encloser
	def inner():
		#This is the nested func
		print(msg)
	return inner
diff = outer("This is an example for closure")
diff()
print(id(diff()))

def f1():
	def f2():
		print("hello")
		print("world")
	return f2
c = f1()
c()
