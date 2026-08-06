# employees salary
def count_salary(gaji=5000000, bonus=0, tax=0.05):
    dirty_salary = gaji + bonus
    tax_amount = dirty_salary *  tax
    return dirty_salary - tax_amount
    
print(count_salary())
print(count_salary(6000000, 500000))
print(count_salary(gaji=7000000, bonus=0, tax=0.1))