# Program to extract numbers from a string
import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

# split

result = re.split(pattern, string) 
print(result)

# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)

# multiline string
string = 'abc 12\
de 23 \n f45 6'

# matches all whitespace characters
pattern = '\s+'

# empty string
replace = ''

new_string = re.sub(pattern, replace, string) 
print(new_string)

new_string = re.sub(r'\s+', replace, string, 1) 
print(new_string)

# count the occurence
new_string = re.subn(pattern, replace, string) 
print(new_string)



string = "Python is fun"
# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found") 

if match:
  print(match.group())
else:
  print("pattern not found")
