weight 	= int (input("Enter package weight in kilograms: "))
length 	= int (input("Enter package length in centimeters: "))
width	= int (input("Enter package width in centimeters: "))
height 	= int (input("Enter package height in centimeters: "))
volume	= length * width * height

if volume > 100000 and weight > 27:
	print("Package too heavy and too large!")
elif volume > 100000:
	print("Package too large!")
elif weight > 27:
	print("Package too heavy!")	
else:
	print("Package is acceptable.")
input()	#Press 'Enter' to close; only needed for SharpDevelop