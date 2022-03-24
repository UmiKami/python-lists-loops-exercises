par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for char in par:
    holder = 0
    for i in par:
        if char.lower() == i.lower() and char != " ":
            holder+=1
            counts[char.lower()] = holder

print(counts)

