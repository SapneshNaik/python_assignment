
def vowel_count(string):

	vowel_count = 0
	vowels = ['a', 'e', 'i', 'o', 'u']
	for i in string:
		if i in vowels:
			vowel_count += 1

	return vowel_count



def main():

	file  = open("ip.txt")
	text = file.read()
	file.close()

	print("Vowel count in  ip.txt: ", vowel_count(text))



if __name__=="__main__":
	main()