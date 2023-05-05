# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_otp.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/24 11:22:09 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/24 19:32:32 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import argparse

if __name__ == "__main__":
    # Create the parser
	my_parser = argparse.ArgumentParser(description='Encrypt or decrypt using OTP')

	# Add the arguments
	my_parser.add_argument('Message',
							metavar='message',
							type=str,
							help='the message to encrypt or decrypt')

	my_parser.add_argument('Key',
							metavar='key',
							type=str,
							help='the encryption key')

	my_parser.add_argument('Action',
							metavar='action',
							type=str,
							help='the action to perform (encrypt or decrypt)')

	# Execute the parse_args() method
	args = my_parser.parse_args()

	print('Message: ', args.Message)
	print('Key: ', args.Key)
	print('Action: ', args.Action)