# Versi 1
SECONDS_IN_YEAR = 365 * 24 * 60 *60
BIRTH_RATE = 7
DEATH_RATE = 13
IMMIGRANT_RATE = 45

current_population = 312032486

births_per_year = SECONDS_IN_YEAR // BIRTH_RATE
deaths_per_year = SECONDS_IN_YEAR // DEATH_RATE
immigrants_per_year = SECONDS_IN_YEAR // IMMIGRANT_RATE

add_pop_per_year = births_per_year + immigrants_per_year - deaths_per_year

years = 1
while years < 6:
	current_population = current_population + add_pop_per_year

	print("Total population in year", years, "is =", current_population)
	years += 1

# Versi 2
population = 312032486
day = 365

birth_seconds = 7
death_seconds = 13
immigrant_seconds = 45

seconds_year = day * 24 * 60 * 60

birth_in_year = seconds_year // birth_seconds
death_in_year = seconds_year // death_seconds
immigrant_in_year = seconds_year // immigrant_seconds

net_population = birth_in_year - death_in_year + immigrant_in_year

for year in range(1, 6):
  population += net_population
  print(f"Year {year} population = {population}")
