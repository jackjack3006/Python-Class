def is_called():
	def isreturned():
		print("hello")
	return isreturned
new = is_called()
new()
