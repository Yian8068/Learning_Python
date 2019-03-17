import numpy as np
from math import cos, pi
import re
cos(pi)

np.cos(np.pi)

print(re.split(r'\s', "hi there ! eadsasd"))

regex = re.compile(r'\s+')
for s in ["         ", "abc ", " abc"]:
    if regex.match(s):
        print(repr(s), "matches")
    else:
        print(repr(s), "does not match")

email3 = re.compile(r'([\w.]+)@(\w+)\.([a-z]{3})')
text = "To email Guido, try guido@python.org or the older address "\
    "guido@google.com."
print(email3.findall(text))

email4 = re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+)\.(?P<suffix>[a-z]{3})')
match = email4.match('guido@python.org')

print(match.groupdict())
