# Function assumes that input array is ordered and values
# are not repeated.
# Returns -1 if the value is not in the array,
# otherwise returns the index of where the value is in the array

def binary_search(input_array,value):
    N = len(input_array)
    imin, imax = 0, N-1

    while imin<=imax:
        half = int((imin+imax)/2) # Same as imin+(imax-imin)/2
        if value == input_array[half]:
            return half
        elif value < input_array[half]:
            imax = half-1
        else:
            imin = half+1
    
    return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 29
print("array")
print(test_list)
print("Search for {}".format(test_val1))
print(binary_search(test_list, test_val1))
print("Search for {}".format(test_val2))
print(binary_search(test_list, test_val2))
