	
def main():
	with open('ip.csv') as csv_file:
	    print("There are a total of ", len(csv_file.readlines()) - 1, " students")

if __name__=="__main__":
	main()