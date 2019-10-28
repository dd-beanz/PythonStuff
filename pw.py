#! python3
# pw.py - Insecure password locker program

#Dictionary data structure that creates keys of what password is saved for and values for passwd
PASSWORDS = {'email': 'PASSWORD123123123', 'blog': 'JAKLSDFJKSLA123', 'locker': '25-12-40'}

import sys, pyperclip

if len(sys.argv) < 2:
  print('Usage: python3 pw.py [account] - copy account password')
  sys.exit()

account = sys.argv[1]

#print(str(PASSWORDS.get(account, 'Not a valid key')))


if account in PASSWORDS:
  pyperclip.copy(PASSWORDS[account])
  print('Password has been copied to clipboard.')
else:
  print('Please use a valid account.')
  sys.exit()

