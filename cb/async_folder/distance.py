# program that will load 2 arrays. Element of the first array are cooordinates X. and 
# the elements of the second array are the coordinates Y of point on a plane.
# Find the point and print the index of coordinates of the point which is the closet to the starting point.
# coordinates (x0),(y0).
from cgi import print_arguments
import math

x = [3,32,15,43,5,22,90,1]
y = [3,32,15,43,5,22,90,1]


for i in range(len(x)):
    x[i] = math.sqrt(x[i]**2 + y[i]**2)
    print(x[i])