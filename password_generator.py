#take how long you want the password to be
#Generate as secure a password as possible for that length
import random

pass_length = None
while type(pass_length) != int:
	pass_length = input("How long do you want your password to be? ")
	try:
		pass_length = int(pass_length)
	except:
		print("Please enter a number")

def passmake(pass_length):
	password = []
	iterations = pass_length // 4
	remainder = pass_length % 4
	for num in range(0, iterations):
		lower = chr(random.randint(97,122))
		upper = chr(random.randint(65,95))
		number = chr(random.randint(48,57))
		symbol = chr(random.randint(32,64))
		password.extend([lower, upper, number, symbol])
	for num in range(0, remainder):
		lower = chr(random.randint(97,122))
		upper = chr(random.randint(65,95))
		number = chr(random.randint(48,57))
		symbol = chr(random.randint(32,64))
		char = random.choice([lower,upper,number,symbol])
		password.extend(char)

	return "".join(password)

print(passmake(pass_length)) 
