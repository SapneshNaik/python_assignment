import re

def valid_email(email):
	return re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
	
def main():
	email = input("Enter email\t")

	if valid_email(email) is None:
		print("Invalid email id")
	else:
		print("Valid email")


if __name__=="__main__":
	main()