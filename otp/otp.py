# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    otp.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/24 11:22:09 by rzamolo-          #+#    #+#              #
#    Updated: 2023/05/03 11:34:22 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse, codecs, math, time

# Inputs
secret = "4e4556455220474f4e4e41204749564520594f55205550"
secret_time = time.time()

def hex_to_bin(secret):
    secret_txt = ""

    for char in secret:
        hex_value = int(char, 16)
        binary_char = bin(hex_value)[2:]
        binary_char = binary_char.zfill(4)
        secret_txt += binary_char + " "

    secret_binary = secret_txt.rstrip()
    return ((secret_binary))

def convert_to_binary(secret, expiration=30):
    hex_to_bin(secret)

    current_time = time.time()
    current_time_int = int(current_time)
    binary_time = format(current_time_int, "b")
    big_endian_bytes = struct.pack(">Q", current_time_int)


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
