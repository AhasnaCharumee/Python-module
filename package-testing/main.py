# import my_calculator.addition
# import my_calculator.substraction 

# sum = my_calculator.addition.add(10, 5)
# difference = my_calculator.substraction.sub(10, 5)
# print(f"Sum: {sum}")
# print(f"Difference: {difference}")

# from my_calculator import addition, substraction
# sum = addition.add(10, 5)
# difference = substraction.sub(10, 5)
# print(f"Sum: {sum}")
# print(f"Difference: {difference}")


#industry standard way
# from my_calculator.addition import add
# from my_calculator.substraction import sub
# sum = add(10, 5)
# difference = sub(10, 5)
# print(f"Sum: {sum}")
# print(f"Difference: {difference}")

from my_calculator import add, sub
sum = add(10, 5)
difference = sub(10, 5)
print(f"Sum: {sum}")
print(f"Difference: {difference}")
