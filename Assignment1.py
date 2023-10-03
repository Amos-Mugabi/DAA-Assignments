# 1. Write an algorithm that outputs the maximum value in an array
def find_maximum(arr):
    # Check if the array is empty
    if len(arr) == 0:
        return None  
    
    # Initialize the max value with the first element of array
    max_value = arr[0]
    

    for num in arr:
        if num > max_value:
            max_value = num  
    
    return max_value


array = [8, 5, 2, 7, 11]


print("Maximum value in the array is:", find_maximum(array))


