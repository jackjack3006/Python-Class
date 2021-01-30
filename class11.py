def f1(a,b):
	def f2():
		print(a)
	def f3():
		print(b)
	return f2,f3
c,d = f1(4,5)
del f1 #Used to delete the function
c()
d()
