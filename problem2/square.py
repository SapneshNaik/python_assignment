def square(number):
	return number * number


def main():

	try:
		number = int(input("Enter number:\t"))
		print("Square of ", number, "is: ", square(number))

	except:
		print("Please enter a valid integer")


if __name__=="__main__":
	main()