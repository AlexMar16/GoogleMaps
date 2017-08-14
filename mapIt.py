#! /usr/bin/env python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    arg = input('Have you copied the address? (y/n):')
    if(arg == 'n' or arg == 'N' or arg =='no' or arg == 'nO' or arg == 'No'):
        address = input('Enter an address: ')
    else:
        address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
