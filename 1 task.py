word1 = input("Enter some value:")
word2 = input("Enter another value:")
word1.lower()
word2.lower()
basket1 = set()
basket2 = set()
for item in word1:
    if item.isalpha():
        basket1.add(item)
        
for item in word2:
    if item.isalpha():
        basket2.add(item)

if basket2.issubset(basket1):
    print("You can use the letters of the first phrase to make a second phrase.")
else:
    print("You can't use the letters of the first phrase to make a second phrase")
    
print("Plural of letters of the first phrase:" , basket1)
print("Plural of letters of the second phrase:" , basket2)



