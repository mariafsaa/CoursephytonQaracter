"""
PYTHON DATA ANALYSIS EXAM
Scenario: Simple sales records

Expected format after cleaning:
product_name,category,price
"""

VALID_CATEGORIES = ["food", "clothes", "electronics"]
MIN_PRICE = 0.0
HIGH_PRICE = 100.0


# =========================
# Objective 1 — Raw data (10 points)
# =========================
# Create a list with at least 12 raw sales records as strings.
# Include:
# - extra spaces
# - upper/lower case differences
# - prices with commas
# - invalid categories
# - negative prices
# - missing fields

raw_sales = [
    "  Apple , Food , 1,20 ",
    "T-shirt, Clothes, 19,99",
    "Laptop , Electronics , 899,99",
    "Bread,FOOD,0",
    "Shoes , clothes , -45",
    "Phone, electronics , 9,99",
    "Milk, food, 1,10",
    "TV, ELECTRONICS, 0",
    "Hat, clothes, 15",
    "Candy, food",
    "Book, education, 12",
    "Camera , electronics , 150"
]

print("Raw records:", len(raw_sales))


# =========================
# Objective 2 — Cleaning data (10 points)
# =========================
# Create a function that cleans ONE record:
# - remove extra spaces
# - convert text to lowercase
# - replace comma with dot in prices

def clean_record(record):
    cleaned = record.strip().lower()
    cleaned = cleaned.replace(" ", "")
    cleaned = cleaned.replace(",", ".")
    return cleaned

cleaned_sales = []

for record in raw_sales:
    cleaned_sales.append(clean_record(record))

for i in range(2):
    print("Cleaned:", cleaned_sales[i])


# =========================
# Objective 3 — Validation (15 points)
# =========================
# A record is valid if:
# - it has exactly 3 fields
# - category is valid
# - price is >= MIN_PRICE

products = []
categories = []
prices = []
invalid_records = []

for record in cleaned_sales:
    if record.count(";") == 0:
        parts = record.split(",")
    else:
        parts = record.split(";")

    if len(parts) != 3:
        invalid_records.append(record)
        continue

    product = parts[0]
    category = parts[1]
    price = float(parts[2])

    if category not in VALID_CATEGORIES:
        invalid_records.append(record)
        continue

    if price < MIN_PRICE:
        invalid_records.append(record)
        continue

    products.append(product)
    categories.append(category)
    prices.append(price)

print("Valid records:", len(products))
print("Invalid records:", len(invalid_records))


# =========================
# Objective 4 — Category filter (10 points)
# =========================
# Extract prices of products that belong to the "food" category.

food_prices = []

for i in range(len(categories)):
    if categories[i] == "food":
        food_prices.append(prices[i])

print("Food products:", len(food_prices))


# =========================
# Objective 5 — Total and average price (10 points)
# =========================
# Calculate:
# - total price of food products
# - average price of food products
# If the list is empty, the result must be 0.

def calculate_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return calculate_total(numbers) / len(numbers)

food_total = calculate_total(food_prices)
food_average = calculate_average(food_prices)

print("Food total:", food_total)
print("Food average:", food_average)


# =========================
# Objective 6 — Most expensive product (10 points)
# =========================
# Find the product with the highest price.
# Print:
# - product name
# - category
# - price

max_price = prices[0]
max_index = 0

for i in range(len(prices)):
    if prices[i] > max_price:
        max_price = prices[i]
        max_index = i

print("Most expensive product:")
print("Name:", products[max_index])
print("Category:", categories[max_index])
print("Price:", prices[max_index])


# =========================
# Objective 7 — Price classification (10 points)
# =========================
# Count how many products are:
# - cheap (price < HIGH_PRICE)
# - expensive (price >= HIGH_PRICE)

cheap_count = 0
expensive_count = 0

for price in prices:
    if price < HIGH_PRICE:
        cheap_count += 1
    else:
        expensive_count += 1

print("Cheap products:", cheap_count)
print("Expensive products:", expensive_count)


# =========================
# Objective 8 — Suspicious products (10 points)
# =========================
# A product is suspicious if:
# - price is 0
# OR
# - category is "electronics" and price < 10

warnings = []

for i in range(len(products)):
    if prices[i] == 0:
        warnings.append("Suspicious: " + products[i])
    elif categories[i] == "electronics" and prices[i] < 10:
        warnings.append("Suspicious: " + products[i])

print("Suspicious products:", len(warnings))


# =========================
# Objective 9 — Final summary (10 points)
# =========================
# Create a multi-line text summary including:
# - total raw records
# - valid records
# - invalid records
# - total and average food price
# - most expensive product
# - suspicious product count

summary = (
    "SALES SUMMARY\n"
    "--------------\n"
    f"Raw records: {len(raw_sales)}\n"
    f"Valid records: {len(products)}\n"
    f"Invalid records: {len(invalid_records)}\n"
    f"Food total: {food_total}\n"
    f"Food average: {food_average}\n"
    f"Most expensive: {products[max_index]} ({prices[max_index]})\n"
    f"Suspicious products: {len(warnings)}"
)

print(summary)


# =========================
# Objective 10 — User category query (5 points)
# =========================
# Ask the user for a category.
# If valid, calculate and print the total price for that category.
# If not valid, print an error message.

chosen_category = input("Enter a category: ").strip().lower()

if chosen_category not in VALID_CATEGORIES:
    print("Invalid category")
else:
    total = 0
    for i in range(len(categories)):
        if categories[i] == chosen_category:
            total += prices[i]
    print(f"Total price for {chosen_category}: {total}")
