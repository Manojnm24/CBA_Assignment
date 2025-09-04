#Given a tuple of coordinates, calculate the distance between two points.

import math

point1 = (3, 4)
point2 = (7, 1)

distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
print(f"Distance between points: {distance:.2f}")

#Distance between points: 5.00