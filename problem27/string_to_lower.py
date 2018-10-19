

def lower_case(string):
	case_dict = {
		'A':'a',
		'B':'b',
		'C':'c',
		'D':'d',
		'E':'e',
		'F':'f',
		'G':'g',
		'H':'h',
		'I':'i',
		'J':'j',
		'K':'k',
		'L':'l',
		'M':'m',
		'N':'n',
		'O':'o',
		'P':'p',
		'Q':'q',
		'R':'r',
		'S':'s',
		'T':'t',
		'U':'u',
		'V':'v',
		'W':'w',
		'X':'x',
		'Y':'y',
		'Z':'z'
	}

	lower_string = ""
	for char in string:
		try:
			lower_string += case_dict[char]

		#key not found error because the char was not a lower case one
		except Exception as e:
			lower_string += char
	return lower_string

def main():

	string = input("Enter the string\t")

	print("Lower case string:\t", lower_case(string))



if __name__=="__main__":
	main()