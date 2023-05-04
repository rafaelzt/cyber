# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    using_totp.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/25 12:02:37 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/27 23:36:05 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import hashlib
import time
import hmac, base64, struct, hashlib, time, math

def is_valid_hex_string(hex_string):
    if len(hex_string) < 64:
        return False
    try:
        int(hex_string, 16)
        return True
    except ValueError:
        return False




def generate_key(hex_string):
    if not is_valid_hex_string(hex_string):
        return None
    sha256 = hashlib.sha256()
    sha256.update(hex_string.encode('utf-8'))
    return sha256.hexdigest()


def get_expiring_key(hex_string, expiration_seconds=30):
    key = generate_key(hex_string)
    if key is None:
        return None
    expiration_time = time.time() + expiration_seconds
    return key, expiration_time


def main():
    # hex_string = input("Digite uma string hexadecimal de no mínimo 64 caracteres: ")
    hex_string = "486f6c61207175652074616c2c20636f6d6f2065737461732e204573746520c3a920756d2074657374207061726120637265617220756e61206c6c617665206d6173206772616e646520717565203634206c6574726173"
    expiring_key = get_expiring_key(hex_string)

    if expiring_key is None:
        print("String hexadecimal inválida.")
    else:
        key, expiration_time = expiring_key
        print(f"A chave gerada é: {key}")
        while time.time() < expiration_time:
            time.sleep(1)
        print("A chave expirou.")

if __name__ == "__main__":
    main()