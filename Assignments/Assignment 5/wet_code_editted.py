# We're looking to find out how much money we have after a day with friends on Saturday. 
# Our code does the trick but we learned about keeping out code DRY recently and want to make it more efficent by making it DRY.
# I want you to accomplish this by making functions where you see repeated code. 
# Some things to note. When we have a positive number that gets split up and 85% goes into checking and 15% goes into savings. 
# All negative numbers gets taken out of the checking account.


from typing import Tuple



def saturdays_bank_transactions(transactions) -> Tuple[float, float]:
    savings = 1096.25
    checking = 1590.80

    def splitit(checking, savings,amount):
        checking += (amount * 0.85)
        savings += (amount * 0.15)
        return 
    

    def addcheck(checking, amount):
        checking += amount
        return 
    

    for item in transactions:
        if item > 0:
            splitit(checking,savings,item)
        return 

    for item in transactions:
        if item < 0:
            addcheck(checking,item)
        return 


    return checking, savings

if __name__ == "__main__":
    transactions = [300.00, -50.00, -5.00, -20, 15.72, 2083.93, -1034.00, -420.00, -5.23, -15.93, -72.90]
    new_balance = saturdays_bank_transactions(transactions)
    print("Your new checking balance is:", '${:.2f}'.format(round(new_balance[0], 2)), "\nYour new savings balance is: ", '${:.2f}'.format(round(new_balance[1], 2)))