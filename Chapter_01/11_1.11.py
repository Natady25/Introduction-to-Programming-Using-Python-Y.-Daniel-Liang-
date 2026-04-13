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