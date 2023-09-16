'''
Given an integer array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

def moveZeroes(nums: list[int]) -> None:
    '''
    Создаём указатель на самое левое свободное место (там где 0)
    Идём по входному массиву и проверяем число, если 0, то идём дальше,
    если не 0, то меняем положения числа и того где указатель

    По времени O(n)
    '''
    index_not_null_number = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        else:
            if i != index_not_null_number:
                nums[index_not_null_number], nums[i] = nums[i], nums[index_not_null_number]
            index_not_null_number += 1

if __name__ == "__main__":
    l = [1,0,1,0,3,12,0]
    moveZeroes(l)
    print(l)


