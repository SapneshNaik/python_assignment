

def upper_case(string):
	case_dict = {
		'a':'A',
		'b':'B',
		'c':'C',
		'd':'D',
		'e':'E',
		'f':'F',
		'g':'G',
		'h':'H',
		'i':'I',
		'j':'J',
		'k':'K',
		'l':'L',
		'm':'M',
		'n':'N',
		'o':'O',
		'p':'P',
		'q':'Q',
		'r':'R',
		's':'S',
		't':'T',
		'u':'U',
		'v':'V',
		'w':'W',
		'x':'X',
		'y':'Y',
		'z':'Z'
	}

	upper_string = ""
	for char in string:
		try:
			upper_string += case_dict[char]

		#key not found error because the char was not a lpwer case one
		except Exception as e:
			upper_string += char

	return upper_string

def main():

	string = input("Enter the string\t")

	print("Upper case string:\t", upper_case(string))



if __name__=="__main__":
	main()