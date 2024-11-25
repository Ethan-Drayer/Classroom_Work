def retrieve_values():
    while True:
        digits = input("Enter the 4 digit integer: ")
        try:
            digits = int(digits)
        except:
            print("Integer value required")
            continue
        if digits < 0:
            print("Positive integers required")
            continue

        digits = [int(i) for i in str(digits)]

        if len(digits) != 4:
            print("4 digits required")
            continue

        while True:
            increment = input("By how many increments should it be shifted: ")
            try:
                increment = int(increment)
            except:
                print("Integer value required")
                continue

            if increment < 0:
                print("Positive integers required")
                continue

            digits.append(increment)
            return digits

def inigma(number):
    increment = number.pop(4)
    decimal_number = 0
    while increment > 0:
        increment -= 1
        if decimal_number == 15:
            decimal_number = 0
        else:
            decimal_number += 1

        for index in range(len(number)):
            if number[index] == 1:
                number[index] = 5
            elif number[index] == 2:
                number[index] = 3
            elif number[index] == 3:
                number[index] = 8
            elif number[index] == 4:
                number[index] = 6
            elif number[index] == 5:
                number[index] = 2
            elif number[index] == 6:
                number[index] = 1
            elif number[index] == 7:
                number[index] = 9
            elif number[index] == 8:
                number[index] = 7
            elif number[index] == 9:
                number[index] = 4

        binary_string = format(decimal_number, '04b')
        binary = [int(i) for i in str(binary_string)]
        binary = binary[::-1]
        if binary[0] == 1:
            if number[0] == 9:
                number[0] = 1
            else:
                number[0] += 1

        if binary[1] == 1:
            if number[1] == 9:
                number[1] = 1
            else:
                number[1] += 1

        if binary[2] == 1:
            if number[2] == 9:
                number[2] = 1
            else:
                number[2] += 1

        if binary[3] == 1:
            if number[3] == 9:
                number[3] = 1
            else:
                number[3] += 1
        print(number)
    return number


password = "K9fn1Q"
while True:
    attempt = input("Password(______): ")
    if attempt == password:
        listed_digits = retrieve_values()
        test = inigma(listed_digits)
        print("---------------")
        print(f"|{test}|")
        print("---------------")
        break
    else:
        print("Wrong")
        continue