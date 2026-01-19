total = 0

while True:
    number = int(input("Enter a number (write -1 to stop): "))

    if number == -1:
        break

    if number > 0:
        total += number

print("Total sum of positive numbers:", total)
