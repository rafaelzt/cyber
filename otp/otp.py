# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    otp.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/24 11:22:09 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/28 17:44:40 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse, codecs, math, time

# Inputs
secret = "4e4556455220474f4e4e41204749564520594f55205550"
secret_time = time.time()

def hex_to_str(secret):
    # secret_hex = bytes(secret)
    secret_txt = codecs.decode(secret, "hex")

    # https://stackoverflow.com/questions/18815820/how-to-convert-string-to-binary
    # secret_binary = ' '.join(format(ord(x),'b') for x in secret_txt) # can bee done using bytearray
    secret_binary = ' '.join(format(x, 'b') for x in bytearray(secret_txt))

    # print(secret_hex)
    print(f"Plain text: {secret_txt}")
    print(f"Binary text: {secret_binary}")
    print(f"Binary text: 01001110 01000101 01010110 01000101 01010010 00100000 01000111 01001111 01001110 01001110 01000001 00100000 01000111 01001001 01010110 01000101 00100000 01011001 01001111 01010101 00100000 01010101 01010000")

def convert_to_binary(secret, expiration=30):
    secret_time = int(123)
    secret_time_bytes = (secret_time).to_bytes(8, byteorder='big')

    print(f"Binary current time: {secret_time_bytes}")


if __name__ == "__main__":
    # Create the parser
	#my_parser = argparse.ArgumentParser(description='Encrypt or decrypt using OTP')

	# Add the arguments
	#my_parser.add_argument('Message',
	#						metavar='message',
	#						type=str,
	#						help='the message to encrypt or decrypt')

	#my_parser.add_argument('Key',
	#						metavar='key',
	#						type=str,
	#						help='the encryption key')

	#my_parser.add_argument('Action',
	#						metavar='action',
	#						type=str,
	#						help='the action to perform (encrypt or decrypt)')

	# Execute the parse_args() method
	#args = my_parser.parse_args()

	#print('Message: ', args.Message)
	#print('Key: ', args.Key)
	#print('Action: ', args.Action)
    
    hex_to_str(secret)
    convert_to_binary(secret)
