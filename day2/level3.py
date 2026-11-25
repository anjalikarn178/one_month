#1
# def add(num1, num2):
#     return num1 + num2
# def sub(num1, num2):
#     return num1 - num2
# def mul(num1, num2):
#     return num1 * num2
# def div(num1, num2):
#     if num2 != 0:
#         return num1 / num2
#     else:
#         return "Error: Division by zero is not allowed."
    
# print(add(1,2))






#2
# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)
    
# num = int(input("Enter a number: "))
# print(f"The {num}th Fibonacci number is: {fibonacci(num)}")





#3
# def is_palindrome(num):
#     reversed_num = rev(num)
#     if num == reversed_num:
#         return True
#     else:
#         return False
    
# def rev(num):
#     reversed_num = 0
#     while num>0:
#         digit = num % 10
#         reversed_num = reversed_num * 10 + digit
#         num //= 10
#     return reversed_num

# num = int(input("Enter a number: "))
# if is_palindrome(num):
#     print(f"{num} is a palindrome.")
# else:
#     print(f"{num} is not a palindrome.")





#4
# def is_armstrong(num):
#     if num < 0:
#         return False
#     num_str = str(num)
#     num_digits = len(num_str)
#     sum_of_powers = 0
#     for digit in num_str:
#         sum_of_powers += int(digit) ** num_digits
#     return sum_of_powers == num

# n = int(input("Enter a number: "))
# if is_armstrong(n):
#     print(f"{n} is an Armstrong number.")
# else:
#     print(f"{n} is not an Armstrong number.")




#5
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=" ")

num1 = int(input("Enter the starting number of the range: "))
num2 = int(input("Enter the ending number of the range: "))
print_primes_in_range(num1,num2)
