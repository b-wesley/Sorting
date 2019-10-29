#if the two vectors are of the same length, adds them and returns the resulting vector,
#returns a vector of 0s if they are not the same length
def addVectors(vector1, vector2):
    temp = [0] * len(vector1)
    if(len(vector1) == len(vector2)):
        for i in range(len(vector1)):
            temp[i] = vector1[i]+ vector2[i]
    return temp

nums1 = [1, 2, 3, 4]
nums2 = [2, 2, 2, 2]
nums3 = [8, 12, 5, 90, 67, 80]

print(addVectors(nums1, nums2))
print(addVectors(nums1, nums3))
