'''This program calculate amt needed to pay off debt with apr in 12 month'''
balance = float(raw_input("Please input principle: "))
apr = float(raw_input("Please input APR in decimal: "))
monthlyapr = .20/12
newbalance = balance
payment = round(0,2)
paymentnumber = 1
while newbalance > 0:
    newbalance = balance
    paymentnumber = 1
    payment += 10    
    while paymentnumber <= 12:
        newbalance = newbalance - payment
        newbalance = newbalance + monthlyapr * newbalance
        paymentnumber += 1
print ''
print ''
print "minimum amount required to pay off the balance in 12 month is " + str(payment)
    


    