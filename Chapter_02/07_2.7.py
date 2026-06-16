#Versi 1
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365

minutes = int(input("Enter the number of minutes: "))

total_days = minutes // minutes_per_hour // hours_per_day

years = total_days // days_per_year

remaining_days = total_days % days_per_year

print(minutes, "minutes is approximately", years, "years and", remaining_days, "days")


#Versi 2
minutes_per_hour = 60
hours_per_day = 24
days_per_year = 365

minutes = int(input("Enter the number of minutes: "))

total_days = minutes // minutes_per_hour // hours_per_day

years = total_days // days_per_year

remaining_days = total_days % days_per_year

print(f"{minutes} minutes is approximately {years} years and {remaining_days} days")