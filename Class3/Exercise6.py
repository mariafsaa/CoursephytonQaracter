count_1_50 = 0
count_mayor_50 = 0

while True:
    num = int(input("Enter an integer number (Write 0 to stop): "))

    if num == 0:
        break
    if num < 0:
        continue

    count_mayor_50 += num > 50
    count_1_50 += 1 <= num <= 50

print("\nResults:")
print(f"Numbers between 1 and 50: {count_1_50}")
print(f"Numbers greater than 50: {count_mayor_50}")