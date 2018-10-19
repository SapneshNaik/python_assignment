#The Euclidean distance between two points in either the plane or 3-dimensional space 
#measures the length of a segment connecting the two points. 

#The Pythagorean Theorem can be used to calculate the distance between two points. In a 2d or 3d space.
import sys
import math

class Euclidean:

	def __init__(self, point1, point2):
	    self.point1 = point1
	    self.point2 = point2

	def distance_2d(self):
		#(x2 -x1)
		x_diff = self.point2[0] - self.point1[0]
		#(y2-y1)
		y_diff = self.point2[1] - self.point1[1]
		# distance is square root of sum of square of x and y distances
		square_sum = (x_diff * x_diff) + (y_diff * y_diff)
		return math.sqrt(square_sum)

	def distance_3d(self):
		#(x2 -x1)
		x_diff = self.point2[0] - self.point1[0]
		#(y2-y1)
		y_diff = self.point2[1] - self.point1[1]
		#(z2-z1)
		try:
			z_diff = self.point2[2] - self.point1[2]
		except:
			print("Not a 3d object")
			sys.exit()

		# distance is square root of sum of square of x and y and z distances
		square_sum = (x_diff * x_diff) + (y_diff * y_diff) + (z_diff * z_diff)
		return math.sqrt(square_sum)