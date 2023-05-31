#1
def number_of_food_groups():     # func declaration
    return 5                     # return value
print(number_of_food_groups())   # log func call 
# * Output: 5

#2
def number_of_military_branches(): # func declaration
    return 5                       # return value
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# ! NameError, name 'number_of_days_in_a_week_silicon_or_triangle_sides' (first func) NOT DEFINED

#3
def number_of_books_on_hold():    # func declaration
    return 5                      # return value
    return 10                     # NOT EXECUTED, func ENDS
print(number_of_books_on_hold())  # * Output: 5


#4
def number_of_fingers():          # func declaration
    return 5                      # return value
    print(10)                     # NOT EXECUTED, func ENDS
print(number_of_fingers())        # * Output: 5


#5
def number_of_great_lakes():     # func declaration
    print(5)                     # output: 5
x = number_of_great_lakes()      # var declaration, assigning func with var x
print(x)                         # (func does not return value, so output is None)
# * Output: None


#6
def add(b,c):                    # func declaration
    print(b+c)                   # log
# print(add(1,2) + add(2,3))       # add(1+2), add(2+3) = 3, 5
# ! TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'


#7
def concatenate(b,c):           # func declaration
    return str(b)+str(c)        # return value, func end
print(concatenate(2,5))         # * Output: 25


#8
def number_of_oceans_or_fingers_or_continents():    # func declaration
    b = 100                                # var declaration
    print(b)                                 # Output: 100
    if b < 10:                             # IF eval: return value, exit func
        return 5                             # NOT EXECUTED, condition not valid (100>10)
    else:                                  # ELSE eval: return value, exit func
        return 10
    return 7                               # NOT EXECUTED, func ends
print(number_of_oceans_or_fingers_or_continents())  # * Output: 100, 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):  # func declaration
    if b<c:
        return 7
    else:
        return 14
    return 3 # not executed
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))   # output: 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))   # output: 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))   # output: 7+14 = 21
# * All Outputs: 7, 14, 21

#10
def addition(b,c):       # func declaration
    return b+c           # return value, func ends
    return 10            # NOT EXECUTED, func ends
print(addition(3,5))     # * Output: 8


# #11
b = 500        # var declaration
print(b)       # output: 500
def foobar():  # func declaration
    b = 300      # var declaration
    print(b)     # output: 500
print(b)       # output: 300
foobar()       # calls function, func prints 300 when called
print(b)       # output: 500
# * All Outputs: 500, 500, 300, 500

# #12
b = 500        # var declaration
print(b)       # output: 500
def foobar():  # func declaration
    b = 300      # var declaration
    print(b)     # output: 500
    return b     # return value: 300, exit func
print(b)       # output: 300
foobar()       # call function
print(b)       # output: 500
# * All Outputs: 500, 500, 300, 500

# #13
b = 500        # var declaration
print(b)       # output: 500
def foobar():  # func declaration
    b = 300      # var declaration
    print(b)     # output: 500
    return b     # retrun value: 300, exit func
print(b)       # output: 300
b = foobar()     # var declaration
print(b)       # output: 300
# * All Outputs: 500, 500, 300, 300

# #14
def foo():     # func declaration
    print(1)        # output: 1
    bar()           # calls func
    print(2)        # output: 2
def bar():     # func def
    print(3)        # output: 3
foo()          # calls func
# * All Outputs: 1, 3, 2

# #15
def foo():     # func declaration
    print(1)        # output: 1
    x = bar()       # var declaration
    print(x)        # 1st: skips, 2nd: output: 5
    return 10       # return value: 10, exit func
def bar():     # func declaration
    print(3)        # output: 3
    return 5        # return value: 5, exit func
y = foo()        # var declaration: y = foo() = 10 
print(y)       # output: 10
# * All Outputs: 1, 3, 5, 10