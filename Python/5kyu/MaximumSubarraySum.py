# Maximum subarray sum

def max_sequence(arr):
    size = len(arr)
    
    if size == 0:
        return 0
    else:
        max_so_far = arr[0]
        current_max = arr[0]

        for i in range(1,size):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far,current_max)
        return max_so_far if max_so_far >= 0 else 0