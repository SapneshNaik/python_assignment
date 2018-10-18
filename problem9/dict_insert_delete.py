
def main():

	print("\nEnter 3 students details\n")

	students = dict()

	#insert
	for i in range(3):
		students[input("Enter Registration number\t")] = input("Enter Name\t")

	print("\n")
	print(students)
	print("\n")

	students.pop(input("enter a Registration Number to delete\t"))
	
	print("\n")
	print(students)
	print("\n")



if __name__ == "__main__":
	main()