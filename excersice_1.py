n = input("How many Triangular numbers do you want to print (including 0):" )
n = int(n)
sum = 0

for i in range(n+1):
    sum = sum + i
print("The Triangular number is: ", sum)