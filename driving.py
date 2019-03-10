country = input('what is your country: ')
age = input('how old are you: ')
if country == 'taiwan':
	if float(age) >= 18:
		print('you can get a drive license')
	else:
		print('you cannot get a drive license')
elif country == 'us':
	if float(age) >= 16:
		print('you can get a drive license')
	else:
		print('you cannot get a drive license')
else:
	print('ask your government, you idiot.')