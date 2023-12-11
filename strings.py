print('Hello Python Interprepter!')

message = 'Hello, we are learning Python now...'
print(message)
str = 'pen'
print(str)
print("\t")

# https://bobbyhadz.com/blog/python-replace-first-character-in-string
my_str = 'bobbyhadz.com'
list_of_chars = list(my_str) #convert string into a list
# 👇️ ['b', 'o', 'b', 'b', 'y', 'h', 'a', 'd', 'z', '.', 'c', 'o', 'm']
print(list_of_chars)

list_of_chars[0] = '_' #change the first character of the list and then convert back into string again
new_str = ''.join(list_of_chars)
print(new_str)  # 👉️ _obbyhadz.com
['b', 'o', 'b', 'b', 'y', 'h', 'a', 'd', 'z', '.', 'c', 'o', 'm']

print("\t")
name = 'ewa barczykowska'
print(name.title())

print(name.upper())
print(name.lower())

print("\t")
first_name = 'ada'
last_name =  'lovelace'
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

print("\t")
url = "http://axisbank.com"
print(url.removeprefix('http://'))

word = "homeless"
print(word.removesuffix("less"))

print("\t")
str = 'sea'
print(len(str))


