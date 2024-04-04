nums = [1, 2, 4, 6, 3, 7, 8]
n = len(nums) + 1
xor_all = 0

# XOR all numbers from 1 to n
for i in range(1, n + 1):
    xor_all ^= i

# XOR all elements in the nums list
for num in nums:
    xor_all ^= num

print(xor_all)  # Output: 5
