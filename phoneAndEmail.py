#! python3.11.2

import re, pyperclip

# create regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 5555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d)))?        # area code (optional)
(\s\-)        # first separator
\d\d\d       # first 3 digits
-        # separator
\d\d\d\d     # last 4 digits
(((ext(\.)?\s|x)         # extension word-part (optional)
 (\d{2,5}))?      #extension number-part (optional)
 )
''', re.VERBOSE)
           
# TODO: create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+    # name part
@    # @ symbol
[a-zA-Z0-9_.+]+     # domain name part

''', re.VERBOSE)


# TODO: get text off the clipboard
text = 'Lester Finch lfinch@gmail.com 511-768-9073 Mason Marquez masonm44@att.net 862-579-2515 Olen Boyer oboyer8@icloud.com 678-439-5117'


# TODO: extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


#  Copy extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
