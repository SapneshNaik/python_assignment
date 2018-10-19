def main():

	file = open("ip.txt")
	text = file.read()

	print(text[::2])

	#important
	file.close()

if __name__=="__main__":
	main()