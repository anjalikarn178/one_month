#1
# my_dict = {}
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# my_dict["name"] = name
# my_dict["age"] = age
# print(my_dict)
# print(my_dict.get("name"))





#2
# sentence = input("Enter a sentence: ")
# words = sentence.lower().split()
# my_dict = {}
# for word in words:
#     my_dict[word] = my_dict.get(word, 0) + 1
# print(my_dict)





#3
# word = input("Enter a word: ")
# my_dict = {}
# for char in word:
#     my_dict[char] = my_dict.get(char, 0) + 1
# print(my_dict)






#4
# scores = {"Aarav": 88, "Diya": 95, "Kabir": 91}
# top_student = max(scores, key=scores.get)
# top_marks = scores[top_student]
# print(f"Highest scorer: {top_student} ({top_marks})")





#5
# employees = {}
# while True:
#     name = input("Enter employee name (or type 'done' to finish): ")
#     if name == 'done':
#         break
#     emp_id = input("Enter employee ID: ")
#     basic_salary = float(input("Enter basic salary: "))
#     employees[emp_id] = {"name": name, "basic_salary": basic_salary}

# average_salary = sum(emp["basic_salary"] for emp in employees.values()) / len(employees)
# print(f"Average salary of employees: {average_salary:.2f}")
