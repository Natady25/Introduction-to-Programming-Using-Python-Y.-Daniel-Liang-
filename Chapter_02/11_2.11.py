MONTHS_IN_YEAR = 12

final_account_value = int(input("Enter final account value: "))
annual_interest_rate = float(input("Enter annual interest rate in percent: "))
number_of_years = int(input("Enter number of years: "))

monthly_interest_rate = annual_interest_rate / 100 / MONTHS_IN_YEAR
number_of_months = number_of_years * MONTHS_IN_YEAR

initial_deposit_amount = final_account_value / ((1 + monthly_interest_rate) ** number_of_months)

print(f"Initial deposit value is {initial_deposit_amount}")