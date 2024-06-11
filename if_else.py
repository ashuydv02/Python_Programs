# If Else
number = 10
if number > 0:
    print('Positive number')

else:
    print('Negative number')


# If...Elif...Else

number = 0
if number > 0:
    print('Positive number')

elif number <0:
    print('Negative number')

else:
    print('Zero')


# Nested If...Else

number = 5
if number >= 0:
    if number == 0:
      print('Number is 0')
   
    else:
        print('Number is positive')
else:
    print('Number is negative')

# If else with logical operators :-
    
age = 35
salary = 6000

if age >= 30 and salary >= 5000:
    print('Eligible for the premium membership.')
else:
    print('Not eligible for the premium membership')