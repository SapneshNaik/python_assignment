
import sys
from euclidean import Euclidean


def get_coordinates(D3 = False):
	try:
		#get first point coordinates
		x1 = float(input("\nEnter x1\n"));
		y1 = float(input("Enter y1\n"));

		if D3:
			z1 = float(input("Enter z1\n"));

		#get second point coordinates
		x2 = float(input("Enter x2\n"));
		y2 = float(input("Enter y2\n"));

		if D3:
			z2 = float(input("Enter z2\n"));

		if D3:
			return [x1, y1, z1], [x2, y2, z2]
		else:
			return [x1, y1], [x2, y2]

	except:
		print("Enter valid integers")
		sys.exit()

def show_options():
	print("\n1 : 2D distance\n")
	print("\n2 : 3D distance\n")
	print("\n3 : Quit\n")


def main():

	show_options()

	while True:
		try:
			choice = int(input("\nEnter choice\n"))
		except:
			print("Enter valid integers")
			continue

		if choice == 1:
			try:
				point1, point2 = get_coordinates(False)
				euc = Euclidean(point1, point2)
				print("\n2D Distance is:\t",euc.distance_2d())

			except Exception as e:
				print(e)
				print("Enter valid coordinates")
				continue

		elif choice == 2:
			try:
				point1, point2 = get_coordinates(True)
				euc = Euclidean(point1, point2)
				print("\n3D Distance is:\t",euc.distance_3d())

			except Exception as e:
				print(e)
				print("Enter valid coordinates")
				continue

		elif choice == 3:
			print("\tBye\n")
			sys.exit()

		else:
			print("\nInvalid choice\n")



if __name__ == "__main__":
	main()


