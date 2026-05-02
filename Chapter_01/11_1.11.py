# Versi 1
birth_in_7_sec = 1
birth_per_hour = 3600 // 7
birth_per_day = 24 * birth_per_hour

immigrants_in_45_sec = 1
immigrants_per_hour = 3600 // 45
immigrants_per_day = 24 * immigrants_per_hour

deaths_in_13_sec = 1
deaths_per_hour = 3600 // 13
deaths_per_day = 24 * deaths_per_hour

current_population = 312032486
add_pop_per_day = birth_per_day + immigrants_per_day - deaths_per_day
add_pop_per_year = 365 * add_pop_per_day

years = 1
a = current_population + add_pop_per_year
while years < 6:

	print("Total population in year", years, "is =", a)
	years += 1
	a += add_pop_per_year

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
