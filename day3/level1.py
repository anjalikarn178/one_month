#1
# nums =[]
# sum =0
# while True:
#     num = input("enter a number (or type 'done' to finish): ")
#     if num == 'done':
#         break
#     nums.append(int(num))
# for num in nums:
#      sum+=num
# print("The sum of the numbers is:", sum)




#2
# import math
# nums = []
# max = -math.inf
# min = math.inf
# while True:
#     n = input("Enter a number (or type 'done' to finish): ")
#     if n == 'done':
#         break
#     nums.append(int(n))

# for num in nums:
#     if num > max:
#         max = num
#     if num < min:
#         min = num
        
# print("The maximum number is:", max)
# print("The minimum number is:", min)





#3
# nums = []
# while True:
#     n = input("Enter a number (or type 'done' to finish): ")
#     if n == 'done':
#         break
#     nums.append(int(n))

# unique_elements = list(set(nums))
# print("The unique elements are:", unique_elements)






#4
# import math
# nums = [] 
# largest = -math.inf
# second_largest = -math.inf
# while True:
#     n = input("Enter a number (or type 'done' to finish): ")
#     if n == 'done':
#         break
#     nums.append(int(n))
    
    
# unique_elements = list(set(nums))

# for num in unique_elements:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("The largest number is:", largest)
# print("The second largest number is:", second_largest)




#5
# nums = []
# while True:
#     n = input("Enter a number (or type 'done' to finish): ")
#     if n == 'done':
#         break
#     nums.append(int(n))
    
# left =0
# right = len(nums) - 1
# while left < right:
#     nums[left], nums[right] = nums[right], nums[left]
#     left += 1
#     right -= 1
    
# print("The reversed list is:", nums)
