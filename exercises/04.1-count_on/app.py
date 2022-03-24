my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

#your code go here:
new_list = []

for items in my_list:
    if type(items) in (list, dict):
        new_list.append(items)

print(new_list)