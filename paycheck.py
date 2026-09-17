# Name: Chane Taylor
# Date: 2026-09-16
# Read inputs
name = input()
hours_worked = float(input())
hourly_rate = float(input())
tax_rate = float(input())

gross_pay = hours_worked * hourly_rate
tax_withheld = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_withheld
# Print output
print(f"Employee: {name}")
print(f"Gross pay: ${gross_pay:.2f}")
print(f"Tax withheld: ${tax_withheld:.2f}")
print(f"Net pay: ${net_pay:.2f}")
