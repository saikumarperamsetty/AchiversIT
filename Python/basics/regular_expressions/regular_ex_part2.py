# Regular Expression Part-2:
# ==========================

# Ex:9 escape():
import re
regex_escape = re.escape('Hello? (Are you There?)')  # Here ?,(, ), space are special symbols, it replaces with escape symbols
print(regex_escape)     # output = Hello\?\ \(Are\ you\ There\?\)