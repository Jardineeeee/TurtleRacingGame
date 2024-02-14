# Author: Jardine
# Date: 2/7/2024
# Desc: Class exercise 2 (math formulas)


#1. Given two points p1 and p2, calculate
#   the distannce between them

p1 = (3,5)
p2 = (6,17)

x1, y1 = p1[0], p1[1]
x2, y2 = p2[0], p2[1]

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print ('The distance = ' , distance)

#2. Using the formula for a line
#   calculate the value of y if
#   the slope = 1.33, b = 2, and
#   the value of x = 7

x = 7
b = 2
m = 1.33
y= (m * x) + b
print ('y is equal to ', y)
