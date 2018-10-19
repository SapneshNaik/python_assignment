def main():

	file = open("ip.txt")
	print(file.readline())

	#important
	file.close()

if __name__=="__main__":
	main()