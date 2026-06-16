import math

MONTHLY_INTEREST_RATE = 5 / 100 / 12
months = int(input("Number of months: "))
monthly_saving = float(input("Enter the monthly saving amount: "))
account_value = 0

for i in range (months):
	account_value = (monthly_saving + account_value) * (1 + MONTHLY_INTEREST_RATE)

final_value = math.floor(account_value * 100) / 100

print(f"After {months} month, the account value is {account_value:.2f}")