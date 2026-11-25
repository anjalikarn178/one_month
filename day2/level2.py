#1
# addition = 0
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     addition += i
# print(f"The sum of first {n} natural numbers is: {addition}")




#2
# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")




#3
# factorial =1
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     factorial *= i
# print(f"The factorial of {n} is: {factorial}")





#4
# n = int(input("Enter a number: "))
# reversed_n = 0
# while n >0:
#     digit = n %10
#     reversed_n = reversed_n * 10 + digit
#     n //= 10
# print(f"The reversed number is: {reversed_n}")





#5
# n = int(input("Enter a number: "))
# is_prime = True
# if n <= 1:
#     is_prime = False
# else:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
# print(f"The number {n} is {'prime' if is_prime else 'not prime'}")