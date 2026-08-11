def reversed_number(numbers):
    numbers = str(numbers)
    reversed_num = list(reversed(numbers))
    return reversed_num


number_input = int(input("Enter the numbers : "))
print (reversed_number(number_input))
