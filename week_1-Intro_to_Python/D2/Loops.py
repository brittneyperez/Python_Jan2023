print('*** For Loops ***')
# * --- For Loops --- *

cats = ['Maine Coon', 'Ragdoll', 'Norwegian Forest Cat']
for cat in cats: # name a variable to call everytime it loops
    print(cat) # the item i want to print
""" Print Output:
    Maine Coon
    Ragdoll
    Norwegian Forest Cat
"""

print('')

ages = [12, 18, 24]
for age in ages:
    if age >= 18:
        print(f"You're {age}-years-old? You are old enough")
    else:
        print(f"You're {age}-years-old? NOT old enough.")
""" Print Output:
    You're 12-years-old? NOT old enough.
    You're 18-years-old? You are old enough
    You're 24-years-old? You are old enough
"""
print('')

# * --- In Range --- *

print('In Range')
# Print 1-10 with JS like for loop
"""
for i in range(0, 10, 1): # ? Start at 1, end before 10, increment by 1
    print(i)

print('Above code is the same as below:')
"""
for i in range(10):
    print(i) # ? will print a number per line

print('')

#  for each index of the list, print the cat
for i in range(len(cats)):
    print("Index:", i) # Index; 0
    print("The cat per index:", cats[i]) 
    """ Print Output:
    # The cat per index: Maine Coon
    # The cat per index: Ragdoll
    # The cat per index: Norwegian Forest Cat
    """
print('')

# Add a "!" to every string in the list
for cat in cats:
    cat += "!"
    print(cat)
    """ Print Output:
    # Maine Coon!
    # Ragdoll!
    # Norwegian Forest Cat!
    """

# print index of every entry that begins with "H"
# * Functions ask for parameters, but all they get is arguments
def printH( arr ): # get an array of Strings
    # ? Method 1
    # for i in range(len(arr)):
    #     if arr[i][0] == 'H':
    #         print(arr[i])
    # ? Method 2
    for text in arr:
        if text[0] == "H":
            print(text)

print('')

dogs = ['Husky', 'Dalmation', 'Golden Retriever', 'Hound']
printH(dogs)
"""Print Output:
Husky
Hound
"""
print('')


# * Looping Over a Dictionary

danheng = {
    "Path": "The Hunt",
    "Element": "Wind",
    "Factions": ["Astral Express", "The Nameless"],
    "Traces": {
        "Basic_ATK": "Cloudlancer Art: North Wind",
        "Skill": "Cloudlancer Art: Torrent",
        "Ultimate": "Ethereal Dream",
        "Talent": "Superiority of Reach",
        "Technique": "Splitting Spearhead"
    }
}

# How do we loop over an object- ...er dictionary?
"""
for x in danheng:
    print(x) # ? for looping in a dict -> gives back the key names

Once we find that out, Rename it.
"""
"""
for key in danheng:
    print(danheng[key]) # ? this will give back the value per each key it loops over
Let's print the key with its corresponding value now.
"""
print("Dan Heng's Details:")
for key in danheng:
    print(f"{key} : {danheng[key]}")

print('')
'''
Make a function that creates an object/dictionary with the keys of name, age, and money with a default for age and money. This is similar to instantiating a class.
- Array (Python) = List (JavaScript)
- Dictionary (Python) = Object (JavaScript)
'''
honkai_sr_mains = [
    {
        "Name" : "Stelle",
        "Gender" : "Female",
        "Age" : 22,
        "Path" : ["Destruction", "Preservation"],
        "Element" : ["Physical", "Fire"],
        "Eidolons" : [6, 2],
    },
    {
        "Name" : "Dan Heng",
        "Gender" : "Male",
        "Age" : 24,
        "Path" : ["Hunt", "Destruction"],
        "Element" : ["Wind", "Imaginary"],
        "Eidolons" : [2, 0],
    },
    {
        "Name" : "March 7th",
        "Gender" : "Female",
        "Age" : 22,
        "Path" : "Preservation",
        "Element" : "Ice",
        "Eidolons" : 4,
    }
]

# This function should search for a person by name, gender, or a min value of other parameters. Use default parameters so that the user can input only variables that they wish to search by.

def find_by_name( name ):
    characters = [] # prepare a new list we want to make
    for person in honkai_sr_mains:
        if person['Name'] == name:
            characters.append(person)
    return characters
# print(find_by_name('Stelle'))

