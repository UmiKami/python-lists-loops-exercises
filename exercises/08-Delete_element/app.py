people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_list = people.copy()
    for i in range(len(people)-1):
        if people[i] == person_name:
            new_list.pop(i)

    return new_list
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))