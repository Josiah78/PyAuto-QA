import re

sentence = "My number is 971-302-0357"

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(sentence)
print(mo.group())

phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search(sentence)

print(mo.group(1))
print(mo.group(2))

# sentence = "this is a sentence"
# gangRegex = re.compile(r'320,|gang')
# mo = gangRegex.search(sentence)
# print(mo.group())

# mo = gangRegex.search("this and sentence")
# print(mo.group())

phoneNumberRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('This is my number 123-456-7890')
print(mo.group())

mo = phoneNumberRegex.search('This is my number 456-7890')
print(mo.group())

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('I am Batman')
print(mo.group())

mo = batRegex.search('I am Batwoman')
print(mo.group())

mo = batRegex.search('I am Batwowowowowowowoman')
print(mo.group())

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumberRegex.findall('Josiah is 971-302-0357 and Kenna is 503-960-3543'))

phoneNumberRegex = re.compile(r'\D\D\D')
mo = phoneNumberRegex.search('123 sup')
print(mo.group())

phoneNumberRegex = re.compile(r'\w\w\w')
mo = phoneNumberRegex.search('sup')
print(mo.group())

phoneNumberRegex = re.compile(r'\s\w+')
print(phoneNumberRegex.findall(' this is some text'))

phoneNumberRegex = re.compile(r'\d+\s\w+')
print(phoneNumberRegex.findall('14 apples 4 bananas and 10 oranges'))

vowelRegex = re.compile(r'[AEIOUaeiou]')
print(vowelRegex.findall('This is a sentence exapmple for vowels'))

consonantRegex = re.compile(r'[^AEIOUaeiou]')
print(consonantRegex.findall('This is a sentence exapmple for vowels'))

numberRegex = re.compile(r'\d+$')
print(numberRegex.search('your number is 14'))
print(numberRegex.search('Your number is fourteen') == None)

matchingRegex = re.compile(r'.at')
print(matchingRegex.findall('The fat cat sat on a mat'))

nameRegex = re.compile(r'First Name: (.*)')
mo = nameRegex.search('First Name: Josiah')
print(mo.group())
print(mo.group(1))

alligatorRegex = re.compile(r'<.*>')
mo = alligatorRegex.search('< This is > some text >')
print(mo.group())

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('< This is > some text >')
print(mo.group())

regexNew = re.compile('banana', re.I)
mo = regexNew.search('baNANA BAnana')
print(mo.group())
print(regexNew.findall('baNANA BAnana'))

agentRegex = re.compile(r'Agent \w+')
print(agentRegex.sub('CENSORED', 'Today at 5 PM it was reported that Agent Josiah had a joint'))
 
sent = "Hello World"
print("Hello" in sent)