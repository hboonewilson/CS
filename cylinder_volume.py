import math
def cylinder_vol(radius , height):
	math.pi*radius**2*height


prompt = "Tell us some specifics about the cylinder and we'll tell you the volume"
print(prompt)

rad = float(input("Enter the cylinder's radius: "))
h = float(input("Enter the cylinder's height: "))

cylinder_vol(rad , h)
