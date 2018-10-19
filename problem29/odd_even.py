
def list_count(my_list, odd = False):
	count = 0
	if odd:
		for element in my_list:
			if element % 2 != 0:
				count += 1
	
	else:
		for element in my_list:
			if element % 2 == 0:
				count += 1

	return count


def list_sum(my_list, odd = False):
	total = 0
	if odd:
		for element in my_list:
			if element % 2 != 0:
				total += element
	
	else:
		for element in my_list:
			if element % 2 == 0:
				total += element

	return total

def list_avg(my_list, odd = False):

	total = list_sum(my_list, odd)
	count = list_count(my_list, odd)
	
	return (total/count)


def main():

	my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	print("\n Total Even:\t", list_count(my_list, odd = True))

	print("\n Total Odd:\t", list_count(my_list))
	
	print("\n Even sum:\t", list_sum(my_list))
	
	print("\n Odd sum:\t", list_sum(my_list, True))

	print("\n Even average:\t", list_avg(my_list))
	
	print("\n Odd average:\t", list_avg(my_list, True))


if __name__=="__main__":
	main()