# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    using_totp.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/25 12:02:37 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/27 15:40:59 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import hmac, base64, struct, hashlib, time, math

# TODO: Test input (ishexa and lenght > 64)
# TODO: Generate OTP (30 sec.)

import random

def generate_key(length):
    """Generate a random binary key of a given length."""
    key = []
    for i in range(length):
        key.append(random.randint(0, 1))
    return key

def otp_encrypt(plaintext, key):
    """Encrypt plaintext using the OTP algorithm."""
    ciphertext = []
    for i in range(len(plaintext)):
        ciphertext.append(plaintext[i] ^ key[i])
    return ciphertext

def otp_decrypt(ciphertext, key):
    """Decrypt ciphertext using the OTP algorithm."""
    plaintext = []
    for i in range(len(ciphertext)):
        plaintext.append(ciphertext[i] ^ key[i])
    return plaintext

# Example usage
plaintext = ["1","0","1","0","0","1", "0", "0"]
# plaintext = " ".join(map(bin, bytearray(plaintext, "utf-8"))) # Binary representation of "Hello"
print(plaintext)
key = generate_key(len(plaintext))
ciphertext = otp_encrypt(plaintext, key)
decrypted_plaintext = otp_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
