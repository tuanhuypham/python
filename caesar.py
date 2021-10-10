
#text ='CHOI'''
'''
Thô:    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Mật mã: 'FGHIJKLMNOPQRSTUVWXYZABC'''

text = input()
basic  ='abcdefghijklmnopqrstuvwxyz'
encode ='DEFGHIJKLMNOPQRSTUVWXYZABC'

crytedtex =' '

for x in text :
	if x in encode:
		index = encode.index(x)
		crytedtex += basic[index]
	else:
		if x in basic:
			index =basic.index(x)
			crytedtex += encode[index]
		else:		
			crytedtex += x

print('ten can tim')
print(text)
print(crytedtex)

