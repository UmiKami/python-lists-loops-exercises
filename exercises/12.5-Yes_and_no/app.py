theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def zero_or_one(num):
    if num == 0:
        return "woko"
    else:
        return "wiki"

new_list = list(map(lambda num: zero_or_one(num), theBools))

print(new_list)