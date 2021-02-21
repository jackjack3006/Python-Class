WAP using functions to generate prime numbers using method of sieve of eratosthenes

def sieve(n):
	prime = list()
	for i in range(2,n+1):
		if i not in prime:
			print(i)
			for j in range(i*i,n+1,i):
				prime.append(j)
n = int(input("Enter the number until which u want to find the prime numbers for "))
print(sieve(n))
		

WAP using recursion to reverse a string
word = 'hello'
def reverse(word):
	if len(word) == 0:
		return word
	else:
		return reverse(word[1:]) + word[0]
print(reverse(word))


WAP using callbacks to find sum, double and triple of a given number

def f(func,n):
	func(n)
def sum1(n):
	const = 0
	for i in range(1,n+1):
		const = const + i
	print(const)
def double(n):
	print(n*2)
def triple(n):
	print(n*3)
f(sum1,10)
f(double,10)
f(triple,10)	



WAP using recursion to find a^b

def exponent(a,b):
	if b == 0:	
		return 1
	else:	
		return a*exponent(a,b-1)
print(exponent(2,3))	



#WAP using closure and callback find nth fibonacci number

#WAP to increment a given number n by 5 times using closure 

