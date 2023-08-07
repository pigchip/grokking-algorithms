def findSmallest(arr):              #Define a function "findSmallest" that accepts an array
    smallest = arr[0]               #Start by setting the first element as the smallest
    smallest_index = 0              #Create a variable to track the smallest index
    for i in range(1,len(arr)):     #Go through every element from the 1st index till the last one 
        if arr[i] < smallest:       #Compare if the element is the smallest
            smallest_index = i      #If it's the smallest save the index
    return smallest_index           #Return smallest_index

def selectionSort(arr):                     #Define a function that will sort the elements
    newArr = []                             #Initialize a new array
    for i in range(len(arr)):               #Go through every element
        smallest = findSmallest(arr)        #Find the smallest index
        newArr.append(arr.pop(smallest))    #Eliminate the smallest element from the array and added to a NEW array
    return newArr                           #It will be added in order from smallest to highest

print(selectionSort([5,3,6,2,10]))          #Test with an array