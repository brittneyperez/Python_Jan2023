import random

print('大家好！ Welcome to Python!')


print('') # spacer between lines in terminal
print('This is a loop printing 5 times:')
#    start @ 1; end before 6
for x in range(1,6):
    print(f'x is: {x}')

print('')
print("Randomly choosing a day from a dictionary—a composite datatype.")
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)
print(f'Today is: {day}') # >>> Today is: { randomly generated day }

print('')
print('Below is are Conditional Statements:')
if day == 'Monday':
    print('It will be a long week!')
elif (day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')
