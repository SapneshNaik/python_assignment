
def inverse_case(string):
	upper_lower = {
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

	lower_upper = {
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

	inverse_case_string = ""
	for char in string:

		#ignore anything not in range a-z or A-Z
		if char not in upper_lower and char not in lower_upper:
			inverse_case_string += char
			continue

		try:
			inverse_case_string += upper_lower[char]
		except Exception as e:
			inverse_case_string += lower_upper[char]

	return inverse_case_string

def main():

	string = input("Enter the string\t")

	print("Inversed case string:\t", inverse_case(string))



if __name__=="__main__":
	main()