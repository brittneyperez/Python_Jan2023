# Basic - Print all integers from 0 to 150.
print('basics'.upper())
for i in range(0, 151):
    print(i)

print('-------')
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
print('multiples of five'.upper())
for x in range(5, 1001, 5):
    print(x)


print('-------')
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
print('counting, the dojo way'.upper())
for y in range(1, 101):
    if y % 10 == 0:   # if divisible by 5
        print('Coding Dojo')
    elif y % 5 == 0:   # if divisible by 10
        print('Coding')
    else:
        print(y)


print('-------')
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
print('whoa. that sucker\'s huge'.upper())
final_sum = 0
for z in range(1, 500001, 2):
    final_sum += z   # final_sum = final_sum + all odd int of z
print(final_sum)


print('-------')
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
print('countdown by 4'.upper() + 's')
for n in range(2018, 0, -4):
    print(n)


print('-------')
# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
print('flexible counter'.upper())
lowNum = 2
highNum = 9
mult = 3
#           range(2,    9,   )
for q in range(lowNum, highNum+1):
    if q % mult == 0:   # q % 3
        print(q)