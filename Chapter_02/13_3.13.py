input_value = int(input("Enter an integer: "))

digit_1 = input_value // 1000
rest_digit_1 = input_value % 1000

digit_2 = rest_digit_1 // 100
rest_digit_2 = rest_digit_1 % 100

digit_3 = rest_digit_2 // 10

digit_4 = rest_digit_2 % 10

print(f"{digit_1}\n{digit_2}\n{digit_3}\n{digit_4}")