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