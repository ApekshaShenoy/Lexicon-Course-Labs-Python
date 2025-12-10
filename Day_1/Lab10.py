"""
LAB 10 — Mini Project: Student Information Formatter 
Ask user for: 
• Name 
• Age 
• Favorite subject 
• Favorite quote 
Then: 
1. Use formatting (.format() or f-strings) to print a nicely formatted paragraph. 
2. Capitalize the name. 
3. Remove whitespace around inputs. 
4. Create a list of the letters from the name. 
5. Print the first and last letter from that list. 
Goal: Combine strings, formatting, indexing, list creation. 

"""
name = input("Enter your name:").strip()
age = input("Enter your age:").strip()
fav_subject = input("Enter your favorite subject:").strip()
fav_quote = input("Enter your favorite quote:").strip()

name = name.capitalize()

print(f"\nStudent Information:\nName: {name}\nAge: {age}\nFavorite Subject: {fav_subject}\nFavorite Quote: \"{fav_quote}\"")

name_letters = list(name)

print("First letter of name:", name_letters[0])
print("Last letter of name:", name_letters[-1])


