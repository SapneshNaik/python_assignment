
def concat(string1, string2):
	return string1+string2


def main():

	#input() returns a string by default. So no need to handle any exceptions... Hopefully

	string1 = input("\nEnter first string\n")
	string2 = input("\nEnter second string\n")

	print( "\nResult:\n", concat(string1, string2))

if __name__=="__main__":
	main()