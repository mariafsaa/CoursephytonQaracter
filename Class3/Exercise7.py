mult_3 = 0
mult_5 = 0
mult_3_5 = 0

while True:
    num = int(input("Enter a number (write -1 to stop): "))

    if num < 0:
        if num == -1:
            break
        continue

    if num % 3 == 0 and num % 5 == 0:
        mult_3_5 += 1
    elif num % 3 == 0:
        mult_3 += 1
    elif num % 5 == 0:
        mult_5 += 1

print("\nResults:")
print(f"Multiples of 3 and 5: {mult_3_5}")
print(f"Multiples of 3: {mult_3}")
print(f"Multiples of 5: {mult_5}")
