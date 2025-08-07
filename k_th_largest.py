def kth_largest_manual(arr, k):
    if len(arr) < k:
        return None                                     # Not enough elements to check the highest 

# Create a list with smallest possible numbers initially

    top = [-float('inf')] * k  

    for num in arr:
        
        if num > top[0]:
            
            # Insert the number in correct position manually
            top[0] = num

            # Bubble up to keep smallest element at index 0
            for i in range(1, k):
                if top[i] < top[i-1]:
                    top[i], top[i-1] = top[i-1], top[i]

    
    return top[0]



arr = list(map(int,input("Enter Numbers with the space seperated :").split()))
k = int(input("Enter which highest Number You want :"))
print(f"{k}th largest:", kth_largest_manual(arr, k))
