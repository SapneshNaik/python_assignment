#O(n) time
def is_palindrome(my_list): 
	my_list_copy = my_list.copy()
	my_list_copy.reverse()
	if my_list == my_list_copy:
		return True
	return False


def main():
	

	list1= ["a", 1, 3 , 3, 1 , "a"]

	list1_copy = list1.copy()

	list2= ["a", 1, 3 , 4, 1 , "a"]

	print("list1:\t", list1)
	print("list2:\t", list2)

	if(is_palindrome(list1)):
		print("list1 is a apalindrome")
	else:
		print("list1 is not a is not apalindrome")

	if(is_palindrome(list2)):
		print("list2 is not a is a apalindrome")
	else:
		print("list2 is not a apalindrome")

if __name__=="__main__":
	main()