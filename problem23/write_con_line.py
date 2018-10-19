import sys


def main():
	if(len(sys.argv) >= 2 ):	
		file = open("ip.txt","w")
		if(file.write(sys.argv[1])):
			print("Line successfuly written into ip.txt")
		#important
		file.close()
	else:
		print("Usage: ",sys.argv[0]," 'write this line'")


if __name__=="__main__":
	main()