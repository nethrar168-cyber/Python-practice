a=int(input("enter num:"))
factorial=1
if a<0:
	print("factorial does not apply for number less than zero")
elif a==0:
	print("factorial of 0 is 1")
else:
	for i in range(1,a+1):
		factorial=factorial*i
		print("factorial of",a,"is",factorial)
	