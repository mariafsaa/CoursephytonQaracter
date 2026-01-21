# Solicitar dos entradas
cat1 = input("Hello user 1. Please input your category: ")
cat2 = input("Hello user 2. Please input your category: ")

# Clean Inputs
cat1_clean = cat1.strip().lower()
cat2_clean = cat2.strip().lower()

# Compare of inputs
if cat1_clean == cat2_clean:
    print(f"Both users have chosen the same category : {cat1_clean.capitalize()}.")  
else: 
   print(f"""Users have chosen different categories.
        User 1 chose: {cat1_clean.capitalize()}
        User 2 chose: {cat2_clean.capitalize()}""")