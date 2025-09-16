text = "hello world"
letters = {}
for char in text: 
    if char != " ":
         letters[char] = letters.get(char, 0) + 1
             
print(letters)

 
