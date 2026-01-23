"""
PYTHON DATA ANALYSIS EXAM (2 hours)
Scenario: E-commerce order records audit

Expected logical structure per record:
order_id ; email ; amount ; status
"""

# =========================
# Objective 1 — Raw data setup (8 points)
# =========================
# Create a list containing at least 14 raw order records (strings).
# Include both correct and incorrect records.
# Examples of issues to include:
# - extra spaces
# - mixed upper/lower case
# - currency symbols or text
# - comma decimals
# - invalid status
# - missing fields
# - negative amounts

# TODO:
# 1) Store the raw records in a list
# 2) Print how many raw records exist


# =========================
# Objective 2 — Cleaning records (10 points)
# =========================
# Define a function that receives ONE raw record and returns a cleaned version.
# Cleaning rules:
# - remove leading/trailing spaces
# - convert text to lowercase
# - remove currency symbols/text
# - replace comma decimals with dot decimals
# - remove spaces around separators

# TODO:
# 1) Define the cleaning function
# 2) Create a new list with all cleaned records
# 3) Print the first three cleaned records


# =========================
# Objective 3 — Validation and separation (14 points)
# =========================
# Separate valid and invalid records.
# A record is valid if:
# - it contains exactly 4 fields
# - the order id starts with "ord_"
# - the email contains "@"
# - the status is one of the valid statuses
# - the amount is a number >= MIN_VALID_AMOUNT

# TODO:
# 1) Create empty lists for valid data (ids, emails, amounts, statuses)
# 2) Create a list for invalid records
# 3) Loop through cleaned records and validate them
# 4) Store valid data in separate lists
# 5) Store invalid records separately
# 6) Print how many valid and invalid records exist


# =========================
# Objective 4 — Filter completed orders (10 points)
# =========================
# From the valid data, extract only the amounts of completed orders.

# TODO:
# 1) Create a list with amounts of completed orders
# 2) Print how many completed orders exist


# =========================
# Objective 5 — Total and average calculation (12 points)
# =========================
# Create reusable functions to calculate:
# - total
# - average
# If a list is empty, return 0.

# TODO:
# 1) Define a function to calculate a total
# 2) Define a function to calculate an average
# 3) Calculate and print total and average of completed orders


# =========================
# Objective 6 — Highest completed order (10 points)
# =========================
# Find the completed order with the highest amount.
# Show:
# - order id
# - email
# - amount
# If there are no completed orders, show a message.

# TODO:
# 1) Check if completed orders exist
# 2) Find the highest amount manually
# 3) Retrieve related order id and email
# 4) Print the result


# =========================
# Objective 7 — Email domain analysis (8 points)
# =========================
# Count how many valid emails are Gmail and how many are not.

# TODO:
# 1) Count gmail addresses
# 2) Count other addresses
# 3) Print both results


# =========================
# Objective 8 — Suspicious orders (12 points)
# =========================
# Mark orders as suspicious if:
# - amount >= HIGH_VALUE_THRESHOLD and status is not completed
# - status is pending and amount is 0
#
# Store warning messages as strings.

# TODO:
# 1) Create a list for warning messages
# 2) Loop through valid records and apply the rules
# 3) Print how many suspicious orders were found


# =========================
# Objective 9 — Final report (10 points)
# =========================
# Create a multi-line text report containing:
# - total raw records
# - valid records
# - invalid records
# - completed total and average
# - highest completed order (or message)
# - email domain counts
# - suspicious order count

# TODO:
# 1) Build the report as a string
# 2) Print the report


# =========================
# Objective 10 — User query by status (6 points)
# =========================
# Ask the user for a status to analyze.
# Validate the input.
# If valid, calculate and print the total amount for that status.

# TODO:
# 1) Ask the user for a status
# 2) Validate it
# 3) Calculate and print the total amount
