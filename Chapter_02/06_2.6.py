#Versi 1
number = int(input("Enter the number between 0 and 1000: "))

digit_1 = number % 10
rest_digit_1 = number // 10

digit_2 = rest_digit_1 % 10
rest_digit_2 = rest_digit_1 // 10

digit_3 = rest_digit_2 % 10

digit_sum = digit_1 + digit_2 + digit_3

print("The sum of the digits is", sum)

#Versi 2
number = int(input("Enter the number between 0 and 1000: "))

digit_1 = number % 10
rest_digit_1 = number // 10

digit_2 = rest_digit_1 % 10
rest_digit_2 = rest_digit_1 // 10

digit_3 = rest_digit_2 % 10

digit_sum = digit_1 + digit_2 + digit_3

print(f"The sum of the digits is {sum}")