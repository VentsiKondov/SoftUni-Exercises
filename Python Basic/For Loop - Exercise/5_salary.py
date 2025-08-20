browser_tabs = int(input())
salary = int(input())
negative_salary = False
web_sites_taxes = {
    'Facebook': 150,
    'Instagram': 100,
    'Reddit': 50
}

for _ in range(1, browser_tabs+1):
    current_browser = input()
    if current_browser in web_sites_taxes:
        salary -= web_sites_taxes[current_browser]

    if salary <= 0:
        negative_salary = True
        break

if negative_salary:
    print(f"You have lost your salary.")
else:
    print(salary)
