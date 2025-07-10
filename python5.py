def divide_8_digit_numbers(num1, num2):
    if len(str(num1)) != 8 or len(str(num2)) != 8:
         print("Both numbers must be 8 digits long.")
        return
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        return
