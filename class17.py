a = list()
i = 0
count = 0
while i == 0:
    if count == 0:
        n = int(input("Enter the value to be entered into the list "))
        a.append(n)
    else:
        break
    count = int(input("If you want to add values press 1 "))

i = 0
total = 0

for i in a:
	total = a[i-1] + total

print("Total is equal to",total)
