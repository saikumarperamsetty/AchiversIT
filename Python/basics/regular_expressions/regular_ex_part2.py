# Regular Expression Part-2:
# ==========================

# Ex:9 escape():
import re
regex_escape = re.escape('Hello? (Are you There?)')  # Here ?,(, ), space are special symbols, it replaces with escape symbols
print(regex_escape)     # output = Hello\?\ \(Are\ you\ There\?\)


# Ex: 10 purge(): it will clear the Regular Expression cashe data
import re
print(re.purge())   # output = None


# Grouping() and Capturing() in Regular Expression:
import re
text = 'Sai: 123-456-3391'
pattern = r'(\w+): (\d{3})-(\d{3})-(\d{4})'
match = re.search(pattern,text)
if match:
    print('Group 1:',match.group(1))    # output = Sai:
    print('Group 2:',match.group(2))    # output = 123
    print('Group 3:',match.group(3))    # output = 456
    print('Group 3:',match.group(4))    # output = 3391
    print('Group 0:',match.group(0))    # output = Sai: 123-456-3391


# Anchors(): \b\b- it is boundary checking
import re
text = 'Hello World, Hello Python World'
pattern = r'\bWorld\b'
match = re.findall(pattern,text)    # it will result in list
print(match)                        # output = ['World', 'World']


# Lookahead and LookBehind:
# (?=) = asserts what follows
# (?<=) = asserts what preceds

# Ex:
import re
text = 'fool123 bar456'
pattern1 = re.findall(r'(?<=foo)\d+)',text)
pattern2 = re.findall(r'\w+(?=456)',text)
print(pattern1)
print(pattern2)


# Flags(Modifiers): 
import re
# pattern = r'Hello'  # for Multiline -> starts with
pattern = r'world'  # for Multiline -> ends with
text = """Hello orld
world Hello
Hello world
"""
match = re.search(pattern,text,re.IGNORECASE | re.MULTILINE)
print(match)    # output(re.IGNORECASE) = <re.Match object; span=(0, 4), match='Hello'> -->it is for starts with
print(match)    # output(re.MULTILINE) = <re.Match object; span=(11, 16), match='world'> -->it is for ends with
print(match.group())    # output = Whatever string we are going to find That String it will return.


# How to Define Format with a-z(a-k),digits(divisable by 3 only - 0369),a-zA-Z0-9#,A-Z{2} min 2 letters by using Regular Expression?
# a-z(means a-k) only
# digits(divisable by 3 only - 0369),
# a-zA-Z0-9#,
# A-Z{2} min 2 letters

# Ans:
# ---
import re
str = input('Enter String to verify format: ')
match = re.fullmatch('^[a-k][0369][a-zA-Z0-9#]{2,}$',str)
if match != None:
    print(match,"It's valid format")
else:
    print(match,"It's Not valid format")


# How to create Mobile Number Format using Regular Expression?
import re
while True:
    pattern = input('Enter Mobile Number format: ')
    matcher = re.fullmatch('^[6-9][0-9]{9}',pattern)
    if matcher != None:
        print(pattern,'its Valid Mobile number Format')
    else:
        print(pattern,'its Not a Valid Mobile number Format')


# How to extract one file data into another file by using Regular Expression?
import re
f1 = open('input.txt','r')
f2 = open('output.txt','w')
for line in f1:
    list = re.findall(r'^[7-9]\d{9}',f1)
    for n in list:
        print(n+'\n')
print('Extracted all numbers')
f1.close()
f2.close()


# Webscraping:
# =============
# Ex:
import re
import urllib.request
u = urllib.request.urlopen('http://www.redbus.in/info/contactus')
text = u.read()
numbers = re.findall('[0-9-]{7}[0-9-]+',str(text),re.i)
for n in numbers:
    print(n)