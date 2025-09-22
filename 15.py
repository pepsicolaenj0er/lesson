import csv
from statistics import mean
with open ("employees.csv" , newline="" , encoding="utf=8") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

departments = {}
for x in employees:
    dept = x["department"]
    salary = int (x["salary"])
    departments.setdefault(dept,[]).append(salary)

print("Средняя зарплата по отделам:")
for dept, salaries in departments.items():
    print(f"{dept}: {mean(salaries):.2f}")

maxSalary = max(employees, key=lambda e: int(e["salary"]))
print ("самая большая зарплата" , maxSalary)

print("сотрудники с зарплатой больше 1300")
for x in employees: 
    if x ["department"] == "IT" and int(x["salary"]) > 1300:
        print(x["name"])