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
   
# Part2: Count occurrences of a word in a comment
comment_usrs = input ("\n Please enter a comment about your product: "
                      "ex| 'This product is good, I had a good experience.' ")
comment_clean = comment_usrs.strip().lower()
words = comment_clean.split(" ")
counter = words.count("good")
bad_count = words.count("bad")
if counter > 0 and bad_count == 0:
    print(f"The word 'good' appears {counter} times in the comment.")
else:
    print("It seems that the word 'good' does not appear in the comment.")

print(f" The comment was : {comment_clean.capitalize()}")