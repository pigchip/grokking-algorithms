#BINARY-SEARCH
#GETTING AN ORDER ARRAY OR LIST AND AN ELEMENT TO FIND ON THE LIST
def binary_search(list,value):
    #GET THE LOW AND HIGH VARIABLES TO KEEP TRACK OF THE LIMITS THAT WE WILL BE SEARCHING ON THE ARRAY
    low = 0
    high = len(list) - 1
    #SEARCHING ON ALL ELEMENTS
    while low <= high:
        index = (low+high) // 2
        guess = list[index]
        #WE ALREADY GUESS THE ELEMENT
        if guess == value:
            return index
        if guess > value:
            high = index - 1
        else:
            low = index + 1
    return None
    
my_list = [1,20,34,55,100]
print(binary_search(my_list,55))
print(binary_search(my_list,2))