import os
def main():
	found = False
	dir_path = input("Enter asbolute path\t: ")
	try:
		for fname in os.listdir(dir_path):
		    if fname.endswith('.pdf'):
		        print("\n"+fname + " found")
		        found = True
		if not found:
			print("No pdf file found in current dir")
	except Exception as e:
		print("Inalid asbolute path")

if __name__ =="__main__":
	main()