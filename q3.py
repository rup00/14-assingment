N = int(input("Enter the value of N: "))

a = []

for i in range(1, N+1):
    if(i % 2 == 0):
        a.append(i)

print("The first N even natural numbers are", a)