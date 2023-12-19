'''RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	Returns a list containing all matches
search	Returns a Match object if there is a match anywhere in the string
split	Returns a list where the string has been split at each match
sub	Replaces one or many matches with a string'''


'''
Metacharacters
Metacharacters are characters with a special meaning:

Character	Description	Example	Try it
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group
'''

import re

# Starts with and ends with

txt = "hello planet"
txt1 = "It's going to 68 dollars in 3 days"
txt2 = "It's going great"
# Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")

x = re.findall("planet$", txt)
if x:
    print("Yes, the string ends with 'planet'")
else:
    print("No match")

###########################

# print all characters form h-n in the order that appears in text
print(re.findall("[h-n]", txt2))
print(re.findall("\d", txt1))
# Search for a sequence that starts with "ol", followed by three (any) characters, and an "s":
print(re.findall("ol...s", txt1))
print(re.findall("o.*s", txt1))
print(re.findall("o*.s", txt1))

# Search for a sequence that starts with "h", followed by 1 or more  (any) characters, and an "o":
print(re.findall("h.+o", txt))
# Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
print(re.findall("he.?o", txt))
# This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

# Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
print(re.findall("he.{2}o", txt))

txt = "The rain in Spain falls mainly in the plain!"

# Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")



import re

txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

'''
Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	Description	Example	Try it
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string
'''

import re

txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")

#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bain", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if "ain" is present at the end of a WORD:

txt = "The rain in Spain"
x = re.findall(r"ain\b", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"
#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the end of a word:
x = re.findall(r"ain\B", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"
#Return a match at every no-digit character:
x = re.findall("\D", txt)
#output: ['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n']
# Yes, there is at least one match!
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"

#Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"
#Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

import re

txt = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

txt = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)
if x:
  print("Yes, there is a match!")
else:
  print("No match")

'''
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
'''

txt = "The rain in Spain"
#Check if the string has any a, r, or n characters:
x = re.findall("[arn]", txt)
print(x)

#Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
print(x)

#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)

#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)
print(x)

txt = "There are 4 seasons not 3"
#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[0123]", txt)
print(x)

txt = "8 times before 11:45 AM"
#Check if the string has any digits:
x = re.findall("[0-9]", txt)
print(x)

txt = "8 times before 11:45 AM"
#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
print(x)


#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", txt)
print(x)

#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)
print(x)

#Check if the string has any + characters:
x = re.findall("[+]", txt)
print(x)
