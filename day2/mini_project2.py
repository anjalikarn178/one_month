def calculate_hra(basic_salary):
    hra = 0.2 * basic_salary
    return hra


def calculate_da(basic_salary):
    da = 0.1 * basic_salary
    return da


def calculate_gross_salary(basic_salary):
    hra = calculate_hra(basic_salary)
    da = calculate_da(basic_salary)
    gross_salary = basic_salary + hra + da
    return gross_salary


def evaluate_performance(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 60:
        return "Average"
    else:
        return "Poor"


def display_report(name, emp_id, salary, score):
    print("=================================================================")
    print("                  EMPLOYEE PERFORMANCE REPORT")
    print("=================================================================")
    print()
    print(f"Employee Name: {name}")
    print(f"Employee ID: {emp_id}")
    print()
    print(f"Basic Salary: {salary}")
    print(f"hra: {calculate_hra(salary)}")
    print(f"da: {calculate_da(salary)}")
    print(f"gross_salary: {calculate_gross_salary(salary)}")
    print()
    print(f"Performance Score: {score}")
    print(f"Category: {evaluate_performance(score)}")



name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
basic_salary = float(input("Enter basic salary: "))
score = float(input("Enter performance score (0-100): "))
display_report(name, emp_id, basic_salary, score)