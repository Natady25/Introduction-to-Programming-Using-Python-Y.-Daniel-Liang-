user_input = input("Enter balance and interest rate (e.g., 3 for 3%): ")
balance, annual_interest_rate = [float(x) for x in user_input.split(",")]

interest = balance * (annual_interest_rate / 1200)

print(f"The interest is {interest:.5f}")