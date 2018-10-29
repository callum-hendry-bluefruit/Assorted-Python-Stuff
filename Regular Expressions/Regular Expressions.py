# From https://automatetheboringstuff.com/chapter7/
# ---- Regular Expressions ---- #

# Checking a (American) phone number without REs
def isPhoneNumber(text):
    if len(text) != 12:   # Phone number is only 12 characters, so if it's longer or shorter than 12 it can't be a phone number
        return False
    for i in range(0, 3):   # Are all of the first 3 characters a number?
        if not text[i].isdecimal():
            return False
    if text[3] != '-':   # 4th character MUST be a hyphen
        return False
    for i in range(4, 7):   # Are the middle 3 characters numbers?
        if not text[i].isdecimal():
            return False
    if text[7] != '-': # 8th character MUST be a hyphen
        return False
    for i in range(8, 12):   # Last 4 characters must be numbers too
        if not text[i].isdecimal():
            return False
    return True

# Quite long-winded, lots of steps which makes it easy to make mistakes.

# Finding a phone number in a longer string (i.e. a string generated from interpretating voice input)
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
    for i in range(len(message)):
        chunk = message[i:i+12]
        if isPhoneNumber(chunk):
            print('Phone number found: ' + chunk)
    print('Done')
# This takes a 12 character long chunk of the message every loop iteration, getting nudged down the message by one every time. Very inefficient way to do it.

# Above is a lot of code for a small task, and is also very limited. It cannot detect extensions or numbers formatted differently (. instead of -, etc.)
# It can't detect other types of phone numbers either, i.e. UK ones

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

# Checking for a phone number via Regular Expression (aka Regex)
# Handy-dandy Regex guide: https://www.regular-expressions.info/

# Regex is a description for a pattern of text.
# \d = digit character, a single numeral from 0 to 9
# This regex covers the large chunk of code above: \d\d\d-\d\d\d-\d\d\d\d
    # 3 digits, a hyphen, another 3 digits and a hyphen, then the final 4 digits
    # This would also cover it: \d{3}-\d{3}-\d{4}
    # using {NUMBER} will do the action multiple times, so \d{3} is shorthand for \d\d\d

# In Python, regex is stored in the "re" module
import re

# Passing a string representing a regular expression to re.compile() returns a Regex pattern object (or simply, a Regex object).
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # the "r" is to make the string into a raw string, 
                                                      # which means the backslashes are interpreted as just backslashes, 
                                                      # not as a part of a special character (i.e \n for newline)

mo = phoneNumRegex.search('My number is 415-555-4242.')
# mo means "Match Object", just a generic variable name
# Regex objects have a search() method that checks the string (string only!) that then returns a Match object if something is found, or None if it doesn't.

# Match objects have a group() method that will return the actual matched text from the searched string.
print(mo.group()) # This would print "415-555-4242"

# Alternatively, if we don't want to create a Regex object, we can skip straight to the Match object by using search() like this:
    # re.search(pattern, string, flags=0) 
        # flags are optional
mo = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', 'My number is 415-555-4242.')
# This returns a Match object without requiring the creation of a Regex object first
    # Useful if you only need to regex one thing once