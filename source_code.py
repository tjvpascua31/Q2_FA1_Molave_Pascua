# Functions

def add_numbers(num1, num2):
	return num1 + num2

def sub_numbers(num1, num2):
	return num1 - num2

def mul_numbers(num1, num2):
	return num1 * num2
	
def div_numbers(num1, num2):
	return num1 / num2

def input_wrapper(text, conv, err_message):
	while True:
		try:
			result = conv(input(text))
			return result
		except ValueError:
			print("Invalid!", err_message)

# Get user input via input_wrapper
float_errmsg = "Input must be a float"
user_num1 = input_wrapper("Enter First Number: ", float, float_errmsg)
user_num2 = input_wrapper("Enter First Number: ", float, float_errmsg)
print(
"""
Operation option:
	1 - addition
	2 - subtraction
	3 - multiplication
	4 - division

Type the number that corresponds with the operation."""
)

# Repeat input until a valid option (1, 2, 3, 4)
operator = 0
while True:
	operator = input_w("Enter choice: ", int, "Enter an integer!")
	if operator in range(1, 5):
		break
	else:
		print("Number must be in the choices!")

# Match option with function
match operator:
	case 1:
		result = add_numbers(user_num1, user_num2)
	case 2:
		result = sub_numbers(user_num1, user_num2)
	case 3:
		result = mul_numbers(user_num1, user_num2)
	case 4:
		result = div_numbers(user_num1, user_num2)

print("Result:", result)
