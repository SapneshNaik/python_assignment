

def main():

	branches = ["EWT", "Embedded Linux", "CTV", "AES", "BDA"]

	print("\nInitial branches\n")
	print(branches)

	print("\nAdding Medical Software\n")
	branches.append("Medical Software")
	print(branches)

	print("\nAdding inserting Cloud computing at the 2nd position\n")
	branches.insert(1, "Cloud computing")
	print(branches)


	print("\nSort list ascending\n")
	branches.sort()
	print(branches)


	print("\nsort list descending\n")
	branches.sort(reverse = True)
	print(branches)


if __name__=="__main__":
	main()