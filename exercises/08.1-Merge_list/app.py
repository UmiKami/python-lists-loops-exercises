chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    chunk1 = chunk_one.copy()
    for names in chunk_two:
        chunk1.append(names)
    return chunk1 
    
print(merge_list(chunk_one, chunk_two))
