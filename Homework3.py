operation = input("Izberi operacijo: + seštevanje, - odštevanje, * množenje, / deljenje! Izbrana operacija je:  ")

number_1 = int(input("Vnesi prvo številko: "))
number_2 = int(input("Vnesi drugo številko: "))

if operation == "+":
    print(number_1 + number_2)

elif operation == "-":
    print(number_1 - number_2)

elif operation == "*":
    print(number_1 * number_2)

elif operation == "/":
    print(number_1 / number_2)

else:
    print("Napačna izbira! Poskusi ponovno")