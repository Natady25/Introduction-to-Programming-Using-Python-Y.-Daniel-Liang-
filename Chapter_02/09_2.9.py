#Versi 1
temp_outside = float(input(
	"Enter the temperature in Fahrenheit between -58 and 41: "))

if -58 <= temp_outside <= 41:
	wind_speed = float(input(
		"Enter the wind speed in miles per hour: "))

	if wind_speed >= 2:
		temp_wc = 35.74 + (0.6215 * temp_outside) - (35.75 *
			wind_speed ** 0.16) + (0.4275 * temp_outside *
			wind_speed ** 0.16)
		print(f"The wind chill index is {temp_wc:.5f}")

	else:
		print("Wind speed must more than or equal 2 mph")
else:
	print("Outside temperature must be beetween -58 and 41 Fahrenheit")