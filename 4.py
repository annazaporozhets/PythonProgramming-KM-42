salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]
percent = 0.30

salaries = []
sum_index = []

for salary in salary_list:
    sum = salary * percent 
    new_salaries = salary + sum
    round(sum,2)
    round(new_salaries,2)
    salaries.append(new_salaries)
    sum_index.append(sum)
print("Salary table")

for i in range(len(salary_list)):
    print(f"{salary_list[i]:.2f} {salaries[i]:.2f} {sum_index[i]:.2f}")