Num_1 = float(input("enter number 1 ="))
Num_2 = float(input("enter number 2 ="))

choise = input("enter your choise + - * /")

if choise == '+':
    print(f"Addition: {Num_1 + Num_2}")

elif choise == '-':  
    print(f"subtraction: {Num_1 - Num_2}")

elif choise == '*':
    print(f"multiplication: {Num_1 * Num_2}")

elif choise == '/':
    print("divide: {Num_1 / Num_2")

else:
    print("invalid choise")
    print("Thank you")            