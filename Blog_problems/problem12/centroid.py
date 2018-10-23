def centroid(Ax, Ay, Bx, By, Cx, Cy):
	Ox = (Ax +Bx + Cx) / 3
	Oy = (Ay + By + Cy) / 3

	return (int(Ox), int(Oy))

def main():
	try:
		Ax= int(input("\nEnter Ax:\t"))
		Ay= int(input("\nEnter Ay:\t"))
		Bx= int(input("\nEnter Bx:\t"))
		By= int(input("\nEnter By:\t"))
		Cx= int(input("\nEnter Cx:\t"))
		Cy= int(input("\nEnter Cy:\t"))
	except:
		print("Enter valid integers")

	print("Centroid of the given traingle is:\t"+ str(centroid(Ax, Ay, Bx, By, Cx, Cy)))

if __name__ =="__main__":
	main()