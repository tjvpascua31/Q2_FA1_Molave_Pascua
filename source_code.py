def add_numbers(num1, num2):
	return num1 + num2

def sub_numbers(num1, num2):
	return num1 - num2

def mul_numbers(num1, num2):
	return num1 * num2
	
def div_numbers(num1, num2):
	return num1 / num2

def input_w(text, conv, err_message):
	while True:
		try:
			result = conv(input(text))
			return result
		except ValueError:
			print("Invalid!", err_message)

double_errmsg = "Input must be a float"
user_num1 = input_w("Enter First Number: ", float, double_errmsg)
user_num2 = input_w("Enter First Number: ", float, double_errmsg)

print(
"""
Operation option:
	1 - addition
	2 - subtraction
	3 - multiplication
	4 - division

Type the number that corresponds with the operation."""
)

opr = 0
while True:
	opr = input_w("Enter choice: ", int, "Enter an integer!")
	if opr in range(1, 5):
		break
	else:
		print("Number must be in the choices!")

match opr:
	case 1:
		result = add_numbers(user_num1, user_num2)
	case 2:
		result = sub_numbers(user_num1, user_num2)
	case 3:
		result = mul_numbers(user_num1, user_num2)
	case 4:
		result = div_numbers(user_num1, user_num2)

print("Result:", result)