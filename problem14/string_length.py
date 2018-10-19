
#method runs in O(n) time. Inefficient but gets the job done without using any built in library 
def string_length(string):
	count = 0
	for i in string:
		count += 1
	return count

def main():

	string =  input("Enter the string:\t")

	print("length is :\t",string_length(string))


if __name__=="__main__":
	main()
