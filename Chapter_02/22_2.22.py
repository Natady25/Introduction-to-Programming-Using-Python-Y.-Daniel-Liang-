years = int(input("Enter the number of years: "))
SECONDS_IN_YEARS = years * 365 * 24 * 60 * 60
BIRTH_RATE = 7
DEATH_RATE = 13
IMMIGRANT_RATE = 45

current_population = 312032486

births_in_year = SECONDS_IN_YEARS // BIRTH_RATE
deaths_in_year = SECONDS_IN_YEARS // DEATH_RATE
immigrants_in_year = SECONDS_IN_YEARS // IMMIGRANT_RATE

add_pop_in_year = births_in_year + immigrants_in_year - deaths_in_year
total_population = current_population + add_pop_in_year

print(f"Total population in {years} years is {total_population}")