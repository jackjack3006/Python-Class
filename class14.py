def make_pretty(func):
	def inner():
		print("I got decorated")
		func()
	return inner
def ordinary():
	print("I am ordinary")
ordinary = make_pretty(ordinary)
ordinary()
@make_pretty       #Shortcut for the above code
def ordinary():
	print("I am ordinary")

print(ordinary()) #None is returned because our func() here has not object it calls to be returned

def deco(fn):
	def what(*x):
		print(fn.__name__) #Used to find the name of the function	
		return fn(*x)
	return what
def sq(x):
	return x*x
def cube(x):
	return x*x*x
def add(x,y):
	return x+y

sq = deco(sq)
cube = deco(cube)
add = deco(add)

print(sq(10))
print(cube(10))
print(add(10,30))
