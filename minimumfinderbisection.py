#Finds minimum payment required to make payment in full using bisection method
balance = float(raw_input("Please input principle: "))
interest = float(raw_input("Please input apr in decimal: "))
newbalance = balance
monthlyinterest = interest/12
lowerlimit = 0
upperlimit = (balance*(1+monthlyinterest)**12)/12
payment = 0

while balance > .02 or balance < -.02:
    balance = newbalance
    month = 1
    payment = (lowerlimit + upperlimit)/2
    while month <= 12:
        balance = round(balance - payment,2)
        balance = round(balance + monthlyinterest * balance,2)
        month += 1
    if balance > 0:
        lowerlimit = payment
    else:
        upperlimit = payment

print "Lowest payment: " + str(round(payment,2))
raw_input("Please press enter to exit")
