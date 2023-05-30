print("Hello World") # Print Output in Terminal: Hello World

# * DATA TYPES
print('')
print('Primitve Data Types')
age = 18 # * Number
AGE = 18 # technically const but no gurantee someone else won't change the data

age = '18' # * String

is_coder = True # * Boolean

my_age = 22
print(my_age + 5) # Print Output: 27

my_age = '22'
# print(my_age + 5) # ! this will make an error because age needs to be a number

# Change data type as such:
print(int(my_age) + 3) # 25 # ? This will convert the String -> Number

print('')
print('Composite Data Types')

# * LISTS
# index       0          1        2
hello = ['こんにちは', '안녕하세요', '你好']
print("Ways to Say Hello:", hello)
print("Hello in Japanese:", hello[0] + "。")

# * DICTIONARY
my_first_character = {
    "name" : "Keqing",
    "vision" : "Electro",
    "weapon" : "Sword",
    "rarity (in stars)" : 5,
    "my_favorite" : True
}

hello[1] = '안녕~' # Reassignment
print(hello)

# * TUPLE
goodbye = ('さようなら', '안녕히 가세요', '再见') # ! these are immutable
print("Goodbye in Mandarin Japanese:", goodbye[2])
# goodbye[2] = "拜拜" # ! data in a tuple CANNOT be changed
goodbye = '拜拜，我的猫。'
print("Index 3 of goodbye:", goodbye[3]) # Print Output: 我 
# ? prints an index of a String, i.e., index 3 = the 4th character in the String
"""
# indexes  0 1 2 3 4 5 6
goodbye = '拜拜，我的猫。'
"""

# * FUNCTIONS
print("")
print("Functions")

def say_hello( name ):
    greeting = f"안녕하세요. 제 이름은 {name}입니다. 마나서 반갑습니다."
    print(greeting)
say_hello('Bri') # 안녕하세요. 제 이름은 Bri입니다. 마나서 반갑습니다.
