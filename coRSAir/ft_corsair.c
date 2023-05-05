/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_corsair.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rzamolo- <rzamolo-@student.42madrid.com>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/04 12:10:54 by rzamolo-          #+#    #+#             */
/*   Updated: 2023/05/04 13:12:28 by rzamolo-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <openssl/evp.h>
#include <openssl/aes.h>
#include <openssl/rsa.h>
#include <openssl/pem.h>
#include <openssl/ssl.h>
#include <openssl/err.h>


int decrypt_file(const char *input_file, const char * output_file, const char *private_key_file)
{
	FILE *key_file = fopen(private_key_file, "rb");
	if (!key_file)
	{
		perror("Unable to open private key file");
		return (-1);
	}

	RSA *rsa = NULL;
	rsa = PEM_read_RSAPrivateKey(key_file, &rsa, NULL, NULL);
	fclose(key_file);

	if (!rsa)
	{
		fprintf(stderr, "Unable to read private key: ");
		ERR_print_errors_fp(stderr);
		fprintf(stderr, "\n");
		// perror("Unable to read private key");
		return (-1);
	}

	FILE *in_file = fopen(input_file, "rb");
	if (!in_file)
	{
		perror("Unable to open input file");
		RSA_free(rsa);
		return (-1);
	}

	FILE *out_file = fopen(output_file, "wb");
	if (!out_file)
	{
		perror("Unable to open output file");
		fclose(in_file);
		RSA_free(rsa);
		return (-1);
	}

	int rsa_size = RSA_size(rsa);
	unsigned char buffer[rsa_size];
	unsigned char output_buffer[rsa_size];
	int bytes_read;
	int output_len;

	while ((bytes_read = fread(buffer, 1, rsa_size, in_file)) > 0)
	{
		output_len = RSA_private_decrypt(bytes_read, buffer, output_buffer, rsa, RSA_PKCS1_PADDING);
		if (output_len == -1)
		{
			perror("Error during decryption");
			fclose(in_file);
			fclose(out_file);
			RSA_free(rsa);
			return (-1);
		}
		fwrite(output_buffer, 1, output_len, out_file);
	}
	fclose(in_file);
	fclose(out_file);
	RSA_free(rsa);

	return (0);
}

int main(void)
{
	const char *input_file = "3.bin";
	const char *private_key_file = "3.pem";
	const char *output_file = "decrypted.txt";

    if (decrypt_file(input_file, output_file, private_key_file) == 0)
	{
        printf("Decryption successful. Output saved in %s\n", output_file);

	}
	else
	{
        printf("Decryption failed.\n");

	}
	return (0);
}
