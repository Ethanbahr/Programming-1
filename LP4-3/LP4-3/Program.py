doe = int (input("Enter how many dozens of eggs: "))
ppd = 0
tp 	= 0
remainder = doe % 12
if doe > 0 and doe < 4:
	ppd = 0.50
elif doe >= 4 and doe < 6:
	ppd = 0.45
elif doe >= 6 and doe < 11:
	ppd = 0.40
elif doe >= 11:
	ppd = 0.35

tp = doe * ppd + (remainder * 1/0.5)
print("Price per dozen:" + str(ppd))
print("Total price is:" + str(tp))
input()