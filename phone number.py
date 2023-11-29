import re

message = 'Call me 415-555-1011 tomorrow, or at 434-466-2520 the next day'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))
