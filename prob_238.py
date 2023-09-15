'''
Given an integer array nums, return an array answer such that answer[i] is equal
 to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

'''

def prod(nums: list[int]) -> list[int]:
    '''
    Используются префиксы и постфиксы. (Можно использовать 1 переменную)
    Сначала проходим по входному массиву, добавляем префикс, умноженный на
    текущее значение из выходного массива. Затем перемножаеи префикс и элемент
    их входного массива
    Во второй прогонке так же по входному массиву, но идём в обратном направлении
    В итоге получаем искомый результат.
    Сложно объяснил
    [1, 2, 3, 4] входной массив
    [1, 1, 2, 6] выходной массив после первого прохода
    [1, 1, 2, 3, 12] изменения префикса последнее значение не используется
    [24, 12, 8, 6] Выходной массив после 2го прохода
    [1, 4, 12, 24, 24]  изменение постфикса последнее значение не используется
    '''
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] *= prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res

if __name__ == "__main__":
    l = [1, 2, 3, 4]
    print(prod(l))

