'''
Given an integer array nums, return true if there exists a
triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].
 If no such indices exists, return false.

'''

def increasingTriplet(nums: list[int]) -> bool:
    res = []
    f = float('inf')
    s = float('inf')
    t = float('inf')

    for n in nums:
        # If n is less than f, it means n can be a potential candidate for
        # the first element of an increasing triplet subsequence.
        # So, it updates f to n.
        if n <= f:
            f = n
        # If n is greater than f and less than s, it means n can be a potential
        # candidate for the second element of an increasing triplet subsequence.
        #  So, it updates s to n.
        elif n <= s:
            s = n
        # If n is greater than both f and s, it indicates the presence of an
        # increasing triplet subsequence. So, it returns True.
        elif n > s:
            t = n
            print(f, s, t)
            return True

    # If the loop completes without finding an increasing triplet subsequence,
    # it means there is no such subsequence in the array, so it returns False.
    print(f, s, t)
    return False



if __name__ == "__main__":
    l = [1,10,2,0,0,0]
    print(increasingTriplet(l))

