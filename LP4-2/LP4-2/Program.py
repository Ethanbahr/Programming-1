#to be completed
plwt = int (input("Enter package weight in kilograms: "))
pl 	 = int (input("Enter package length in centimeters: "))
pw 	 = int (input("Enter package width in centimeters: "))
ph 	 = int (input("Enter package height in centimeters: "))
pv 	 = pl * pw * ph

if plwt < 27 and pv < 100000:
	print("Package too heavy and too large")
elif plwt < 27:
	print("Package too heavy")
elif pv < 100000:
	print("Package too large")
input()	#Press 'Enter' to close; only needed for SharpDevelop
	