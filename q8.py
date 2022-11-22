l1 = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6]
print("Original list:")
print(l1)
res = []
for i in l1:
    if i not in res:
        res.append(i)
print("\nDistinct elements along with their frequencies:")
for i in res:
    print(i, l1.count(i))