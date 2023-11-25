import pyperclip
import random

try:
	with open('pettee.txt', mode='r', encoding='utf8') as pettee:
		list = []
		for i in pettee.readlines():
			list.append(i.strip())
except:
	with open('pettee.txt', mode='a', encoding='utf8'):
		pass
	input('pettee.txt has been created, please populate\npress any key to exit...')
	quit()

if list == []:
	input('No more entries\npress any key to exit...')
	quit()

rand = random.randint(0, len(list)-1)
name = list[rand]
leng = len(name)

pyperclip.copy(name)
print('\
   By order of Her Majesty\n\
  Queen Chrysalis, we shall\n\
 be bestowing the pets upon:\n\
  / \-----' + '-'*leng + '----,\n\
  \_,|    ' + ' '*leng + '    |\n\
     |    ' + name     + '    |\n\
     |  ,-' + '-'*leng + '------\n\
     \_/__' + '_'*leng + '____/\
')

with open('petted.txt', mode='a', encoding='utf8') as petted:
	petted.write(list[rand] + '\n')

list.pop(rand)
with open('pettee.txt', mode='w', encoding='utf8') as pettee:
	for i in list:
		pettee.write(i + '\n')

input('\nPress any key to exit...')