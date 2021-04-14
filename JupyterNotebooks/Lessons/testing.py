rainbow = ["red", "orange", "yellow"]

for color in rainbow:
    print(color.title())


for number in range(0,12,3):
    print(number)


a = True 
b = False

if a and b:
    print("this")

elif b and False:
    print("b")

elif b or False:
    print("c")

elif a and True:
    print("finally this")

arr = [2,5,6,1,4,3]
arr.pop()
arr.append(7)
arr.sort()
arr.append(3)
print(arr[5])

arr = [2,5,6,1,4,3]
print(arr[3:5])

this = "Quick brown fox jumped over the lazy dog."
print(this[16:22])