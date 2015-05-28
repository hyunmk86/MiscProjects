'''This program calculates minimum monthly payment and remaining balance each month in a year based on principle and apr'''
b = float(raw_input("please input priciple: "))
apr = float(raw_input("please input apr in decimal: "))
mpr = float(raw_input("please input minimum monthly payment % in decimal: "))
first = b * mpr
rb = b - first
monthcount = 1 
totalpaidcount = 0
while monthcount < 13:
    print "Month: " + str(monthcount)
    mmp = round(b * mpr, 2)
    unpaid = b - mmp
    b = round((unpaid + (.20/12) * unpaid), 2)
    monthcount += 1
    totalpaidcount += mmp
    print "Minimum monthly payment: " + str(mmp)
    print "Remaining balance: " + str(b)
    print ""
print ""
print "Total Paid: " + str(totalpaidcount)
print "Remaining balance: " + str(b) 
    
raw_input("Press enter to exit")    