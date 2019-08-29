"""
This project finds the least amount of coins needed to return change to user, then prints it.
Challenge : if the user inputs non-negative value, the program has to repeat promt.
"""
while True:
    changeOwed = float(input("How much change is owed? "))
    if changeOwed >= 0:
        break
changeRounded = round(changeOwed * 100)
Quarter = 25
Dime = 10
Nickel = 5
Penny = 1
change = changeRounded % Quarter
coinCount = (changeRounded - change) / Quarter
changeNotpaid = change
change = change % Dime
coinCount = coinCount + ((changeNotpaid - change) / Dime)
changeNotpaid = change
change = change % Nickel
coinCount = coinCount + ((changeNotpaid - change) / Nickel)
changeNotpaid = change
change = change % Penny
coinCount = round(coinCount + ((changeNotpaid - change) / Penny))
print ("You need " + str(coinCount) + " coins")
