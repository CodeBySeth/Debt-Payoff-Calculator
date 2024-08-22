class debt:
    debtValue = 0
    interest  = 0
    payment   = 0
    monthlyAccInt = 0

    # parameterized constructor
    def __init__(self, d, i, p):
        self.debtValue = d
        self.interest  = i
        self.payment   = p
        
        
        

def calculateInterest(interest, loanAmount):
    loanType = input("Is the loan a credit card? (y or n): ")
    if loanType == "y":
        return (interest / 365) * 30
    else:
        loanLength = int(input("How long is the length of the loan: "))
        return interest * loanAmount * loanLength
        
        


#Collect debt information
income   = float(input("What is your salary: "))
debtList = []

while True:
    value    = float(input("Enter debt value: "))
    if value == 0.0:
        break
    interest = float(input("Enter interest value: ")) / 100
    payment  = float(input("Enter payment value: "))

    obj = debt(value, interest, payment)

    obj.monthlyAccInt = calculateInterest(interest, value)

    debtList.append(obj)


# Consolidated
total = 0

for debtObj in debtList:
    total += debtObj.debtValue

months  = total / income
year    = int(months / 12)
months -= int(year * 12)

print(f"""Your debt will be paid off in {year} years and {int(months)} months with it consolidated.""")


# Avalanche
i = 0
incomeAve = income

#Sort list by interest rate
for i in range(len(debtList)):
    for i in range(len(debtList) - 1):
        if debtList[i].interest < debtList[i + 1].interest:
            temp            = debtList[i + 1]
            debtList[i + 1] = debtList[i]
            debtList[i]     = temp
    
months = 0

#Calculate the time to pay off the debt
for i in range(len(debtList)):
    months_snowball = debtList[i].debtValue / incomeAve
    incomeAve      += debtList[i].payment
    months         += months_snowball

#Display the time calculated
year    = int(months / 12)
months -= int(year * 12)
print(f"""Your debt will be paid off in {year} years and {int(months)} months with the avalanche method.""")



#Snowball
i = 0
incomeSnow = income

#Sort list by payment value
for i in range(len(debtList)):
    for i in range(len(debtList) - 1):
        if debtList[i].payment > debtList[i + 1].payment:
            temp            = debtList[i + 1]
            debtList[i + 1] = debtList[i]
            debtList[i]     = temp
    
months = 0

#Calculate the time to pay off the debt
for i in range(len(debtList)):
    months_snowball = debtList[i].debtValue / incomeSnow
    incomeSnow     += debtList[i].payment
    months         += months_snowball
#Display the time calculated
year    = int(months / 12)
months -= int(year * 12)
print(f"""Your debt will be paid off in {year} years and {int(months)} months with the snowball method.""")



#Highest payment first
i = 0
incomeHP = income

#Sort list by payment value
for i in range(len(debtList)):
    for i in range(len(debtList) - 1):
        if debtList[i].payment < debtList[i + 1].payment:
            temp            = debtList[i + 1]
            debtList[i + 1] = debtList[i]
            debtList[i]     = temp
    
months = 0

#Calculate the time to pay off the debt
for i in range(len(debtList)):
    months_snowball = debtList[i].debtValue / incomeHP
    incomeHP       += debtList[i].payment
    months         += months_snowball
    

#Display the time calculated
year    = int(months / 12)
months -= int(year * 12)
print(f"""Your debt will be paid off in {year} years and {int(months)} months with the highest payment method.""")