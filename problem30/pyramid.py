#O(n) time
def print_pyramid(level): 
	spaces = 2 * (level) - 2
	for i in range(level):
		sp = " " * spaces
		print(sp + ". " * i)
		spaces -= 1


def main():
	try:
		level = int(input("Enter pyramid level\t"))
		print_pyramid(level)
	except:
		print("Please enter a valid integer")


if __name__=="__main__":
	main()