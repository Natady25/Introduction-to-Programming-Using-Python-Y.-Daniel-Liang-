#Versi 1
feetToMeter = 0.305

feet = eval(input("Enter a value for feet: "))

meter = feet * feetToMeter

print(feet, "feet is", meter, "meters")

#Versi 2
feetToMeter = 0.305

feet = float(input("Enter a value for feet: "))

meter = feet * feetToMeter

print(f"{feet} feet is {meter} meters")