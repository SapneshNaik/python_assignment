
def vowel_count(string):
	vowels = ['a', 'e', 'i', 'o', 'u']

	vowel_count = 0

	for i in string:
		if i in vowels:
			vowel_count += 1

	return vowel_count



def main():

	string = input("\nEnter the string\n")

	print("Vowel count: ", vowel_count(string))



if __name__=="__main__":
	main()