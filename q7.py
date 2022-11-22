my_list = [1, 2, 'a', 'b']

new_list = []

for i in my_list:
    if type(i) == int:
        new_list.append(i)

print(new_list)