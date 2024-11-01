eggs 		= int (input("Enter how many dozens of eggs: "))
dzns 		= eggs // 12
ppd 		= 0
remainder 	= eggs % 12
tp			= 0 
if dzns > 0 and dzns < 4:
	ppd = 0.50
elif dzns >= 4 and dzns < 6:
	ppd = 0.45
elif dzns >= 6 and dzns < 11:
	ppd = 0.40
elif dzns >= 11:
	ppd = 0.35

tp = dzns * ppd + (remainder * 1.0/12 * ppd)
print("Price per dozen:" + str(ppd))
print("Total price is:" + str(tp))
input()