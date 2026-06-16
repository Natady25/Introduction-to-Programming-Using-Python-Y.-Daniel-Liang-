#Versi 1
sub_total, gratuity_rate = eval(input(
	"Enter the subtotal and a gratuity rate : "))

gratuity = gratuity_rate * sub_total / 100
total = sub_total + gratuity

print("The gratuity is", gratuity, "and the total is", total)

#Versi 2
user_input = input("Enter the subtotal and a gratuity rate : ")
sub_total, gratuity_rate = [float(x) for x in user_input.split(",")]

gratuity = gratuity_rate * sub_total / 100
total = sub_total + gratuity

print(f"The gratuity is {gratuity:.2f} and the total is {total:.2f}")