print('''
	                                                                  d8b          888                       
                                                                  Y8P          888                       
                                                                               888                       
 .d8888b .d88b.   8888b.  .d8888b   .d88b.  888d888       .d8888b 888 88888b.  88888b.   .d88b.  888d888 
d88P"   d8P  Y8b     "88b 88K      d8P  Y8b 888P"        d88P"    888 888 "88b 888 "88b d8P  Y8b 888P"   
888     88888888 .d888888 "Y8888b. 88888888 888          888      888 888  888 888  888 88888888 888     
Y88b.   Y8b.     888  888      X88 Y8b.     888          Y88b.    888 888 d88P 888  888 Y8b.     888     
 "Y8888P "Y8888  "Y888888  88888P'  "Y8888  888           "Y8888P 888 88888P"  888  888  "Y8888  888     
                                                                      888                                
                                                                      888                                
                                                                      888                                
	''')

alps = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
		'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encoder(msg,shift_by):
	encoded_msg = ''
	for char in msg:
		if char in alps:
			new_char = alps[alps.index(char)+shift]
			encoded_msg+=new_char
		else:
			encoded_msg+=char
	return encoded_msg

def decoder(msg,unshift_by):
	decoded_msg = ''
	for char in msg:
		if char in alps:
			new_char = alps[alps.index(char)-shift]
			decoded_msg+=new_char
		else:
			decoded_msg+=char
	return decoded_msg


enc_msg = input('Enter your message: ')
shift = int(input('Enter the num of positions to shift: '))
e_msg=encoder(enc_msg,shift)
print(e_msg)
de_msg=decoder(e_msg,shift)
print(de_msg)