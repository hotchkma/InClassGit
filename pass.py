import random

def passw(n):
		password = ""
		for x in range(0,n):
				password += str(random.randrange(0,10,1))
		print(password)
