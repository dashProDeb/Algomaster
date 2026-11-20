nums = [1,1,1,2,2,2,3,3,3,4,4,5,5,6,7]

def removeDuplicate( nums, result ) :
    p1 = nums[0]
    p2 = nums[1]
    i = 0
    j = 1 
    while i < j  :
        if(nums[i]==nums[j]):
            p2 += 1
            result[0] = p1 
        else : 
            p1 += 1
            result[i+1] = p2
                          
    print(result)
        
    