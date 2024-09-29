# Regular Expression Part-2:
# ==========================

# Ex:9 escape():
# import re
# regex_escape = re.escape('Hello? (Are you There?)')  # Here ?,(, ), space are special symbols, it replaces with escape symbols
# print(regex_escape)     # output = Hello\?\ \(Are\ you\ There\?\)


# Ex: 10 purge(): it will clear the Regular Expression cashe data
# import re
# print(re.purge())   # output = None


# Grouping() and Capturing() in Regular Expression:
# import re
# text = 'Sai: 123-456-3391'
# pattern = r'(\w+): (\d{3})-(\d{3})-(\d{4})'
# match = re.search(pattern,text)
# if match:
#     print('Group 1:',match.group(1))    # output = Sai:
#     print('Group 2:',match.group(2))    # output = 123
#     print('Group 3:',match.group(3))    # output = 456
#     print('Group 3:',match.group(4))    # output = 3391
#     print('Group 0:',match.group(0))    # output = Sai: 123-456-3391


# Anchors(): \b\b- it is boundary checking
# import re
# text = 'Hello World, Hello Python World'
# pattern = r'\bWorld\b'
# match = re.findall(pattern,text)    # it will result in list
# print(match)                        # output = ['World', 'World']


# Lookahead and LookBehind:
# (?=) = asserts what follows
# (?<=) = asserts what preceds

import re
text = 'fool123 bar456'
pattern1 = re.findall(r'(?<=foo)\d+)',text)
pattern2 = re.findall(r'\w+(?=456)',text)
print(pattern1)
print(pattern2)