# Recoginizing Python Concepts

# This is a single line comment
"""
This is
a multiline
comment
"""
'''
As well as
this one
'''

# * Variable Declaration
num1 = 42 #? var declaration; number initialized
num2 = 2.3 #? var declaration; decimal/float initialized
boolean = True #? var declaration; boolean initialized
string = 'Hello World' #? var declaration; string initialized

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #? var declaration; list initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #? var declaration; dictionary initialized
fruit = ('blueberry', 'strawberry', 'banana') #? var declaration; tuple initialized

# * Printing to Console
print(type(fruit)) # <class 'tuple'> #? print to console, type check
print(pizza_toppings[1]) # Sausage #? print to console, accessing List value
pizza_toppings.append('Mushrooms') #? adding value to List
print(person['name']) # John #? print to console, accessing a Dictionary value
person['name'] = 'George' #? changing Dictionary value
person['eye_color'] = 'blue' #? changing Dictionary value
print(fruit[2]) # Banana #? print to console, accessing Tuple data

# * Conditional Statements
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
""" 
>>> It's lower 
#? Conditional "if" and "else" Evaluation
#? print to console
"""


if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
""" 
>>> Just right! 
#? Conditional "if" - "elif" - "else" Evaluation
#? print to console
"""

# * For Loops
for x in range(5):
    print(x) #? For Loop: start at 0 & goes up to until 5 >>> (prints per line)
for x in range(2,5):
    print(x) #? For Loop: start at 2 & goes up to until 5 >>> (prints per line)
for x in range(2,10,3):
    print(x) #? For Loop: start at 2 & goes up to until 10, increments by 3 >>> (prints per line)

# * While Loop
x = 0 #? var declaration, number initialized
while(x < 5):
    print(x) #? print to console
    x += 1 #? incrementing x

# * Deleting List Value
pizza_toppings.pop() #? deleting List value at end
# ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
pizza_toppings.pop(1) #? deleting List value at index
# ['Pepperoni', 'Jalepenos', 'Cheese', 'Olives']

print(person) #? printing Dictionary to console
# {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color') #? deleting value at index
print(person) #? printing edited Dictionary to console
# {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# * For Loop Through a List
for topping in pizza_toppings:
    if topping == 'Pepperoni': #? Conditional "if" statement
        continue #? continues
    print('After 1st if statement') #? print to console
    """(per line)
    This will print the statement: "After 1st if statement"
    three times.
    """
    
    if topping == 'Olives': #? Conditional "if" statement
        break #? stops the loop (at Olives)

# * Function Declaration
def print_hello_ten_times(): #? Function Declaration (no parameters)
    for num in range(10): #? for each loop until 10...
        print('Hello') #? ...print to console (per line) >>> Hello

print_hello_ten_times() #? Function call

def print_hello_x_times(x): #? Function Declaration with Parameter "x"
    for num in range(x): #? For Loop up until a given number "x"...
        print('Hello') #? ...print to console (per line) >>> Hello

print_hello_x_times(4) #? Function call w/ argument of 4

def print_hello_x_or_ten_times(x = 10): #? Function call w/ default parameter
    for num in range(x): #? For Loop until x...
        print('Hello') #? ...print to console (per line) >>> Hello

print_hello_x_or_ten_times() #? Function call goes to 10
print_hello_x_or_ten_times(4) #? Function call goes to 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)