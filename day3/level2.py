#1
# import math
# tup =(1,2,3,4,34,55,66)
# list_of_tup = list(tup)
# sum=0
# smallest = math.inf
# largest = -math.inf
# for num in list_of_tup:
#     sum+=num
#     if num>largest:
#         largest = num
#     if num<smallest:
#         smallest = num
# print("The sum of the numbers is:", sum)
# print("The maximum number is:", largest)
# print("The minimum number is:", smallest)





#2
# student =("anjali", 20, "female", "Bangalore")
# name, age, gender, city = student
# print("Name:", name)
# print("Age:", age)
# print("Gender:", gender)
# print("City:", city)





#3
# list1 =[]
# list2 =[]
# while True:
#     n = input("Enter a number (or type 'done' to finish): ")
#     if n == 'done':
#         break
#     list1.append(int(n))

# while True:
#     n = input("Enter a number (or type 'done' to finish): ")
#     if n == 'done':
#         break
#     list2.append(int(n))
    
# list1_set = set(list1)
# list2_set = set(list2)
# print("The common elements are:", list(list1_set.intersection(list2_set)))






#4
# sentence = input("Enter a sentence: ")
# unique_words = set(sentence.lower().split())
# print("The unique words in the sentence are:", unique_words)  





#5
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# union_set = set1.union(set2)
# print("The union of the two sets is:", union_set)   
# intersection_set = set1.intersection(set2)
# print("The intersection of the two sets is:", intersection_set)
# difference_set = set1.difference(set2)
# print("The difference of the two sets is:", difference_set)
