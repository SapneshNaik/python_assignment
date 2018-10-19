#Class with mostly static methods to calculate the area of an object
import math

class Area:

	@staticmethod
	def circle(radius):
		pi = 3.141592653589793
		return (pi * (radius * radius))

	@staticmethod
	def triangle(height, base):
		return ((height * base)/2)

	@staticmethod
	def square(side):
		return (side * side)