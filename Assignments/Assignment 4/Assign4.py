
def sumofnum(input1):
    g = input1 +1
    h = sum(range(g)) 
    return h

input1 = input("Enter a number:")
print("The sum is " + str(sumofnum(int(input1))))
