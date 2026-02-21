def solution():
    arr=[3,2,4,5]
    arr.sort()
    target=6
    i=0
    j=len(arr)-1
    while i<j:
        curr_sum=arr[i]+arr[j]
        if curr_sum ==target:
           
            print(arr[i],arr[j])
            return True
            
        
        elif curr_sum <target:
            i+=1
        else:
            j-=1
    return False
print(solution())
            
        
        
