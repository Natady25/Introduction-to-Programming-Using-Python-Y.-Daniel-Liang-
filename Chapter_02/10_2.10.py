#Versi 1 
velocity, acceleration = eval(input("Enter speed and acceleration: "))

length = (velocity ** 2) / (2 * acceleration)

print("The minimum runway length for this airplane is",
	round(length * 1000) / 1000, "meters")

#Versi 2
user_input = input("Enter speed and acceleration: ")
velocity, acceleration = [float(x) for x in user_input.split(",")]

length = (velocity ** 2) / (2 * acceleration)

print(f"The minimum runway length for this airplane is {length:.3f} meters")