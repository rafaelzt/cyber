/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   corsair.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/04 12:10:54 by rzamolo-          #+#    #+#             */
/*   Updated: 2023/05/05 13:03:18 by rzamolo-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "corsair.h"

void	initialize_openssl(void)
{
	SSL_load_error_strings();
	OpenSSL_add_ssl_algorithms();
}

EVP_PKEY	*read_pem_file(const char *pem_filename)
{
	FILE		*pem_file;
	EVP_PKEY	*pkey;

	pem_file = fopen(pem_filename, "r");
	if (pem_file == NULL)
	{
		printf("Error: cannot open file %s\n", pem_filename);
		return (NULL);
	}
	pkey = PEM_read_PrivateKey(pem_file, NULL, NULL, NULL);
	if (!pkey)
	{
		fprintf(stderr, "Error: PEM_read_X509 returned NULL\n");
		ERR_print_errors_fp(stderr);
	}
	fclose(pem_file);
	return (pkey);
}


int	main(int argc, char *argv[])
{
	const char	*pem_filename;
	EVP_PKEY	*pkey;

	initialize_openssl();

	pem_filename = "public.pem";
	pkey = read_pem_file(pem_filename);

	if (!pkey)
	{
		printf("Error: cannot read file %s\n", pem_filename);
		return (1);
	}

	printf("ArgC: %d\n", argc);
	printf("ArgV[0]: %s\n", argv[0]);
	printf("ArgV[1]: %s\n", argv[1]);

	printf("OpenSSL version: %s\n", OPENSSL_VERSION_TEXT);
	printf("OpenSSL library compiled version: %s\n", \
			SSLeay_version(SSLEAY_VERSION));


    // Clean up
	EVP_PKEY_free(pkey);
	EVP_cleanup();
	ERR_free_strings();

	return (0);
}
