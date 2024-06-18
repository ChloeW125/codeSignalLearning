"""


Problem: You're given a peculiar list of unique integers - it's sorted in a decreasing order and then rotated at a random pivot. So, while you and I know that it's still sorted, it kicks off from an unpredictable point. Your mission, if you choose to accept it, is to hunt down a specific target number in this array and report its index. If the target turns up missing, return -1.

How is the input scheduled to arrive, you ask? Well, the format is a list with positive integer elements, with possible edge cases being an array of size 1 or the target number not being present in the array! You are guaranteed that the array will always consist of unique numbers.

You need to whip up a solution that takes this list and target number as inputs and returns the index of our target, or -1 if it's on the lam. Now, go give it whatever you've got!
"""

def search_dec_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        #Both mid and target are in the first half
        elif nums[left] >= nums[mid] and nums[left] >= target > nums[mid]:
            right = mid - 1
        #Both mid and target are in the second half
        elif nums[right] <= nums[mid] and nums[right] <= target < nums[mid]:
            left = mid + 1
        #Mid is in the first half but target is in the second
        elif nums[mid] < nums[right]:
            left = mid + 1
        #Mid is in the second half but target is in the first
        else:
            right = mid - 1
    return -1

print(search_dec_rotated([4, 3, 2, 1, 8, 7, 6, 5], 1))  # Expected output: 3
print(search_dec_rotated([9, 8, 7, 6, 5, 4, 3, 2, 1], 4))  # Expected output: 5
print(search_dec_rotated([5, 4, 3, 2, 1], 8))  # Expected output: -1