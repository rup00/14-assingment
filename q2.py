N = int(input("Enter the value of N: "))

l = [] 

for i in range(1, N + 1): 
	if(i % 2 != 0): 
		l.append(i) 
		
print(l)