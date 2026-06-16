#Versi 1
MONTHS_IN_YEAR = 12

investment_amount = int(input("Enter investment amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
number_of_years = int(input("Enter number of years: "))

monthly_interest_rate = annual_interest_rate / 100 / MONTHS_IN_YEAR
number_of_months = number_of_years * MONTHS_IN_YEAR

future_investment_value = investment_amount * ((1 + monthly_interest_rate)
	** number_of_months)

print(f"Accumulated value is {future_investment_value:.2f}")

#Versi 2
import math

MONTHS_IN_YEAR = 12

investment_amount = int(input("Enter investment amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
number_of_years = int(input("Enter number of years: "))

monthly_interest_rate = annual_interest_rate / 100 / MONTHS_IN_YEAR
number_of_months = number_of_years * MONTHS_IN_YEAR

future_investment_value = investment_amount * ((1 + monthly_interest_rate)
	** number_of_months)

print(f"Accumulated value is {math.floor(future_investment_value * 100)
	/ 100}")