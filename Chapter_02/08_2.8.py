#Versi 1
water_c = 4184

water_mass = float(input("Enter the amount of water in kilograms: "))
initial_temp = float(input("Enter the initial temperature: "))
final_temp = float(input("Enter the final temperature: "))

energy_joules = water_mass * (final_temp - initial_temp) * water_c

print("The energy needed is ", energy_joules)


#Versi 2
water_c = 4184

water_mass = float(input("Enter the amount of water in kilograms: "))
initial_temp = float(input("Enter the initial temperature: "))
final_temp = float(input("Enter the final temperature: "))

energy_joules = water_mass * (final_temp - initial_temp) * water_c

print(f"The energy needed is {energy_joules}")