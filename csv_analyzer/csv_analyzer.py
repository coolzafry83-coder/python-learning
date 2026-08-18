import csv


def load_data(filename):
    employees = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["Salary"] = int(row["Salary"])
            employees.append(row)

    return employees


def analyze_data(employees):
    salaries = [employee["Salary"] for employee in employees]

    total_salary = sum(salaries)
    average_salary = total_salary / len(salaries)
    highest_salary = max(salaries)
    lowest_salary = min(salaries)

    highest_employee = max(employees, key=lambda employee: employee["Salary"])
    lowest_employee = min(employees, key=lambda employee: employee["Salary"])

    print("Total salary:", total_salary)
    print("Average salary:", average_salary)
    print("Highest salary:", highest_salary)
    print("Lowest salary:", lowest_salary)

    print("Highest paid employee:", highest_employee["Name"])
    print("Salary:", highest_employee["Salary"])

    print("Lowest paid employee:", lowest_employee["Name"])
    print("Salary:", lowest_employee["Salary"])

    print("Total employees:", len(employees))


employees = load_data("employees.csv")
analyze_data(employees)