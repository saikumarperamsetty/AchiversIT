# Regular Expressions:
# It is a declarative mechanism to represent a group of strings according to a particular format.

# Methods in Regular Expressions:
# 1. compile():
# 2. finditer():

# 1. compile():
# ===========
# i. start(): return the start index
# ii. end(): return the end index
# iii. group(): return the group index

# Ex:1 Basic Example to Pattern Find in Given String By Using Regular Expression?
import re
count = 0
# pattern = re.compile('ab')
matcher = re.finditer('ab','abaaababa')
for match in matcher:
    count += 1
    print(match.start(),'....',match.end(),'....',match.group())    # output = 0 .... 2 .... ab, 4 .... 6 .... ab, 6 .... 8 .... ab
print('The number of occurences of ab:',count)                      # output = 3


# Character Classes in Regular Expression:
# ========================================
# [abc] = only abc
# [^abc] = except abc
# [a-z] = only a-z
# [^a-z] = except a-z
# [A-Z] = ony A-Z 
# [^A-Z] = except A-Z 
# [a-zA-Z0-9] = only a-zA-Z0-9
# [^a-zA-Z0-9] = except a-zA-Z0-9

# Ex:2 Pattern Find in Given String By Using Character Classes in Regular Expression?
import re
x = '[abc]'
x = '[^abc]'
x = '[a-z]'
x = '[^a-z]'
x = '[A-Z]'
x = '[^A-Z]'
x = '[a-zA-Z0-9]'
x = '[^a-zA-Z0-9]'
pattern= re.compile(x)
matcher = pattern.finditer('a7N@k9bTd2R8$')
for match in matcher:
    print(match.start(),'....',match.group())


# Predefined Character Classes in Regular Expression:
# ==================================================
# \s = only space
# \S = Except space, any other char
# \d = only digits
# \D = Except digits, any other char
# \w - it represents the Alpha_numeric, Except Special Chars
# \W - # Except Alpha_numeric, But only Special Chars
# \. - only dot(.)
# . - include dot(.) all other chars

# Ex:3 Pattern Find By Using Predefined Character Classes in Regular Expression?
import re
x = '\s'    #only space
x = '\S'    #Except space, any other char
x = '\d'    #only digits
x = '\D'    #Except digits, any other char
x = '\w'    #it represents the Alpha_numeric, Except Special Chars
x = '\W'    # Except Alpha_numeric, only Special Chars
x = '\.'    #only dot(.)
x = '.'     #include dot(.), all other chars
pattern= re.compile(x)
matcher = pattern.finditer('a7N @k.9bT d2.R 8$')
for match in matcher:
    print(match.start(),'....',match.group())


# Quantifiers in Regular Expression:
# ==================================
# a = Exactly one time
# a+ = Min 1 time - Max any no of time
# a* = Min 0 time - Max any no of time
# a? = Min 0 time - Max 1 time
# a{m} = Exactly m time( m- means number we want to mention)
# a{m,n} = Exactly m,n time( m,n- means number we want to mention)


# Ex:4 Pattern Find By Using Quantifiers in Regular Expression?
import re
x = 'a'    # Exactly one time matching a string, it will return
x = 'a+'    # Min 1 time of a - Max any no of time of a, wherever a is came in String that will return
x = 'a*'    # Min 0 time of a - Max any no of time of a, wherever a is came in String that will return and include other chars(its hiding) also
x = 'a?'    # Min 0 time of a - Max 1 time of a, wherever a is came in String that will return
x = 'a{2}'    # Exactly m time( m- means number we want to mention), wherever a is came in String that will only return
x = 'a{2,5}'    # Exactly m,n time( m,n- means number we want to mention), wherever a is came in String that will only return
pattern= re.compile(x)
matcher = pattern.finditer('abaabaaab')
for match in matcher:
    print(match.start(),'....',match.group())


# Functons in re module:
# ======================
# 1. match():
import re
s = input('Enter Pattern to Check: ')
m = re.match(s,'abcfghqdnd')              #Exactly Not match the Given String
if m != None:
    print('Match String is available in Given string')
    print('Start index:',m.start(),'end index:',m.end())
else:
    print('Match String is Not available in Given string')


# 2. fullmatch():
import re
s = input('Enter Pattern to Check: ')
m = re.fullmatch(s,'abcfghqdnd')        #Exactly Match the Given String
if m != None:
    print('Match String is available in Given string')
    print('Start index:',m.start(),'end index:',m.end())
else:
    print('Match String is Not available in Given string')


# 3. finditer():
import re
itr = re.finditer('[a-z]','a0b2*be@kd%jo$')       # Wherever the Pattern matches only that elements will return.
for match in itr:
    print('index present at:',match.start(),'---',match.group())


# 4. sub():
# syntax = [regex,replacement,targetstring]
import re
substr = re.sub('[a-z]','$','a0b2*be@kd%jo$')       # Wherever the applied symbol($) Pattern matches only that elements will changed with new string.
print(substr)                                 # output = $0$2*$$@$$%$$$ (here Where a-z elements is there that only will Change)


# 5. subn():
# here 0 index represents the result String
# here 1 index represents the Occurences
import re
substrn = re.subn('[a-z]','$','a0b2*be@kd%jo$')       # Wherever the applied symbol($) Pattern matches only that elements will changed with new string.
print(substrn)                                 # output = ($0$2*$$@$$%$$$,8) (here Where a-z elements is there that only will Change), and return How many times that symbol is occured
print('The Result String:',substrn[0])      # output = $0$2*$$@$$%$$$                          
print('The no of Occurences: ',substrn[1])  # 8


# 6. split():
import re
regex_split = re.split('@','Apple,Watermelon,Orange,Cocumber,Tomato')   # here only that ',' only seperated
regex_split = re.split('@','Apple@Watermelon@Orange@Cocumber@Tomato')    # here only that '@' only seperated
print(regex_split)      # output = ['Apple', 'Watermelon', 'Orange', 'Cocumber', 'Tomato'] it will return ouput in the form of list as comma seperated.


# 7. ^symbol(): starts with
import re
regex_symbol = re.search('^Laerning','Learning Python is Very Easy!')       # output = False
if regex_symbol != None:
    print('True')
else:
    print('False')


# 8. $symbol(): ends with
import re
regex_symbol = re.search('Very Easy!$','Learning Python is Very Easy!')     # output = True
if regex_symbol != None:
    print('True')
else:
    print('False')